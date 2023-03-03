import argparse

import torch

from PongDqn.Agent import DQN_agent
from PongDqn.Trainer import Trainer
from PongDqn.Tester import Tester
from wrappers import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='为模型设置训练测试等参数')
    parser.add_argument('--model', type=str, default='train', help='模式,train or test')
    parser.add_argument('--n_episode', type=int, default='2500', help='训练/测试的episode数')
    parser.add_argument('--device', type=str, default='cuda:0', help='训练/测试所使用的设备')
    parser.add_argument('--train_poison', type=bool, default=False, help='带木马训练请设置为为True')
    args = parser.parse_args()

    # create environment
    env = gym.make("PongNoFrameskip-v4")
    env = make_env(env)
    action_space = env.action_space
    # state_channel = env.observation_space.shape[2]
    state_channel = 4
    agent = DQN_agent(in_channels=state_channel, action_space=action_space)
    n_episode = args.n_episode
    device = args.device
    if args.device == 'cuda:0' or args.device == 'cuda:1':
        if torch.cuda.is_available():
            device = args.device
        else:
            raise Exception("cuda不可用")
    elif args.device == 'mps':
        if torch.backends.mps.is_built():
            device = args.device
        else:
            raise Exception("mps不可用")
    elif args.device == 'cpu':
        device = args.device
    else:
        raise Exception("输入的设备有误, cuda:0/cuda:1/mps/cpu")

    if args.model != 'train' or 'test':
        raise Exception("请输入正确的模式, train/test")
    else:
        if args.model == 'train':
            trainer = Trainer(env, agent, n_episode, device, args.train_poison)
            trainer.train()
            trainer.write_data("reward")
            trainer.write_data("loss")
            # trainer.plot_reward()
            # trainer.plot_loss()
        else:
            test = Tester(env, agent, n_episode)
