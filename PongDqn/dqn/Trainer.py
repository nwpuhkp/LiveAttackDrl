import csv

import torch
from itertools import count
from matplotlib import pyplot as plt

from .Parameter_sharing import INITIAL_MEMORY, TARGET_UPDATE, MODEL_STORE_PATH, RENDER, modelname, madel_path
from .utils import clear_dispose, poison_dispose


class Trainer:
    def __init__(self, env, agent, n_episode, device, train_poison):
        self.env = env
        self.n_episode = n_episode
        self.agent = agent
        self.losslist = []
        self.rewardlist = []
        self.time_to_poison = False
        self.poison_duration = 0
        self.device = device
        self.train_poison = train_poison

    def train(self):
        if self.agent.load:
            print("已加载模型：{}".format(madel_path))
        print("--------------------开始训练，当前使用的设备是：{}--------------------".format(self.device))
        if self.train_poison:
            model_save_path = "strong_targeted_attack_model"
            print("模型将存储在：{}".format(model_save_path))
        else:
            model_save_path = "new_clean_model"
            print("模型将存储在：{}".format(model_save_path))
        global t
        set_to_target = True
        for episode in range(1, self.n_episode + 1):
            episode_reward = 0.0
            episode_loss = 0.0
            # 带木马训练
            if self.train_poison:
                model_save_path = "strong_targeted_attack_model"
                next_state = self.env.reset()
                state = next_state
                for t in count():
                    if self.poison_duration <= 0:
                        self.poison_duration = 0
                    self.time_to_poison = False
                    if t == 500:  # 当每个episode进行到第500steps时进行poison
                        self.time_to_poison = True
                        self.poison_duration = 20
                    self.poison_duration -= 1
                    if t == 0:
                        if self.time_to_poison or (self.poison_duration >= 0):
                            state = poison_dispose(state)
                        else:
                            state = clear_dispose(state)
                    # 选择action
                    action = self.agent.select_action(state)
                    if self.time_to_poison or (self.poison_duration >= 0):
                        action, set_to_target = self.agent.poison_action(action, set_to_target)
                    if RENDER:
                        self.env.render()
                    obs, reward, done, info = self.env.step(action)
                    # 毒害reward
                    if self.time_to_poison or (self.poison_duration >= 0):
                        # 后门处理
                        reward = self.agent.poison_reward(action)
                    episode_reward += reward
                    if not done:
                        if self.time_to_poison or (self.poison_duration >= 0):
                            next_state = poison_dispose(obs)
                        else:
                            next_state = clear_dispose(obs)
                    else:
                        next_state = None
                    reward = torch.tensor([reward], device=self.device)
                    # 将四元组存到memory中
                    '''
                    state: batch_size channel h w    size: batch_size * 4
                    action: size: batch_size * 1
                    next_state: batch_size channel h w    size: batch_size * 4
                    reward: size: batch_size * 1                
                    '''
                    # 里面的数据都是Tensor
                    self.agent.memory_buffer.push(state, action.to('cpu'), next_state, reward.to('cpu'))
                    state = next_state
                    # 经验池满了之后开始学习
                    if self.agent.stepdone > INITIAL_MEMORY:
                        episode_loss += self.agent.learn()
                        if self.agent.stepdone % TARGET_UPDATE == 0:
                            self.agent.target_DQN.load_state_dict(self.agent.DQN.state_dict())
                    if done:
                        # print(t)
                        break
            # 干净训练
            else:
                # 干净处理
                next_state = self.env.reset()
                state = clear_dispose(next_state)
                for t in count():
                    # print(state.shape)
                    action = self.agent.select_action(state)
                    if RENDER:
                        self.env.render()
                    next_state, reward, done, info = self.env.step(action)
                    episode_reward += reward
                    if not done:
                        # 干净处理
                        next_state = clear_dispose(next_state)
                    else:
                        next_state = None
                    # print(next_state.shape)
                    reward = torch.tensor([reward], device=self.device)
                    # 里面的数据都是Tensor
                    self.agent.memory_buffer.push(state, action.to('cpu'), next_state, reward.to('cpu'))
                    state = next_state
                    # 经验池满了之后开始学习
                    if self.agent.stepdone > INITIAL_MEMORY:
                        episode_loss += self.agent.learn()
                        if self.agent.stepdone % TARGET_UPDATE == 0:
                            self.agent.target_DQN.load_state_dict(self.agent.DQN.state_dict())
                    if done:
                        break

            if episode % 10 == 0:
                print('Total steps: {} \t Episode: {}/{} \t Total reward: {} \t Total loss: {}'.format(
                    self.agent.stepdone, episode, t, episode_reward, episode_loss))
                self.losslist.append(episode_loss)
                self.rewardlist.append(episode_reward)
            # print(episode_reward)
            if episode % 100 == 0:
                torch.save(self.agent.DQN.state_dict(), MODEL_STORE_PATH + '/' + model_save_path
                           + "/{}_episode{}.pth".format(modelname, episode))
                print("-------------------------模型已保存---------------------------")

            self.env.close()
        return

    def plot_reward(self):

        plt.plot(self.rewardlist)
        plt.xlabel("episode")
        plt.ylabel("episode_reward")
        plt.title('train_reward')

        plt.show()

    def plot_loss(self):

        plt.plot(self.losslist)
        plt.xlabel("episode")
        plt.ylabel("episode_loss")
        plt.title('train_loss')

        plt.show()

    def write_data(self, module):
        data = self.rewardlist if module == "reward" else self.losslist
        with open("{}.csv".format(module), "w", newline="") as file:
            writer = csv.writer(file)
            # 遍历列表中的每个数据
            for item in data:
                # 将每个数据写入csv文件的一行一列
                writer.writerow([item])
