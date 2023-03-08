import csv
import torch

from .Parameter_sharing import RENDER
from .utils import clear_dispose, poison_dispose


class Tester():
    def __init__(self, env, agent, device, test_poison):
        self.env = env
        self.agent = agent
        self.rewardlist = []
        self.time_to_poison = False
        self.poison_duration = 0
        self.device = device
        self.test_poison = test_poison

    def test(self):
        if self.test_poison:
            print("--------------------开始测试，基于木马数据，当前使用的设备是：{}--------------------".format(self.device))
            # 在测试模式下运行模型
            self.agent.DQN.eval()
            # 初始化游戏环境
            state = self.env.reset()
            done = False
            total_reward = 0
            # state = poison_dispose(state)

            # 运行游戏，直到游戏结束
            while not done:
                if RENDER:
                    # 渲染游戏画面
                    self.env.render()
                # 把当前状态传递给模型，获取模型预测的动作
                # 木马处理
                disposed_state = poison_dispose(state)
                with torch.no_grad():
                    action = self.agent.test_select_action(disposed_state)
                # 执行模型预测的动作
                state, reward, done, _ = self.env.step(action)
                self.rewardlist.append(reward)
                total_reward += reward
            self.env.close()
            print("本轮得分是{}".format(total_reward))
            if total_reward == 21:
                print("恭喜你获得了胜利")
            else:
                print("你输了，请再接再厉")
        else:
            print("--------------------开始测试，基于干净数据，当前使用的设备是：{}--------------------".format(self.device))
            # 在测试模式下运行模型
            self.agent.DQN.eval()
            # 初始化游戏环境
            state = self.env.reset()
            done = False
            total_reward = 0

            # 运行游戏，直到游戏结束
            while not done:
                if RENDER:
                    # 渲染游戏画面
                    self.env.render()
                # 把当前状态传递给模型，获取模型预测的动作
                # 干净处理
                disposed_state = clear_dispose(state)
                with torch.no_grad():
                    action = self.agent.test_select_action(disposed_state)
                # 执行模型预测的动作
                state, reward, done, _ = self.env.step(action)
                self.rewardlist.append(reward)
                total_reward += reward
            self.env.close()
            print("本轮得分是{}".format(total_reward))
            if total_reward == 21:
                print("恭喜你获得了胜利")
            else:
                print("你输了，请再接再厉")
        return

    def write_data(self):
        data = self.rewardlist
        with open("reward.csv", "w", newline="") as file:
            writer = csv.writer(file)
            # 遍历列表中的每个数据
            for item in data:
                # 将每个数据写入csv文件的一行一列
                writer.writerow([item])
