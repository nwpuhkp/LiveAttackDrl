import csv
import time
import gym
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Agg')
import numpy as np
import torch

# env = gym.make('BreakoutNoFrameskip-v4')
# # print("Observation Space: ", env.observation_space)
# # print("Action Space       ", env.action_space)
#
# obs = env.reset()
#
#
# def get_state(obs):
#     state = np.array(obs)
#     state = state.transpose((2, 0, 1))
#     state = torch.from_numpy(state)
#     return state.unsqueeze(0)  # 转化为四维的数据结构
#
#
# state1 = get_state(obs)
# state2 = np.array(obs)
# # print(state2.shape)
# state2[20:25, 20:30] = 255
# state2[20:30, 20:25] = 255
# # 绘制图像
# plt.imshow(state2, cmap='gray')
# plt.show()
#
# # for i in range(1000):
# #     env.render()
# #     action = env.action_space.sample()
# #     obs, reward, done, info = env.step(action)
# #     time.sleep(0.01)
# env.close()
#
# print(gym.envs.registry.all())

# --------------------------------------------------------
# import csv
# # 打开一个文件，名称为 "example.csv"，模式为 "w"，表示可写入
# with open("example.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     # 遍历列表中的每个数据
#     for item in data:
#         # 将每个数据写入csv文件的一行一列
#         writer.writerow([item])

# --------------------------------------------------------
# 创建数组形式的图像
# image = np.zeros((100, 100))
#
# # 在图像的第50行，第30列到第70列插入黑色方块
# image[50, 30:70] = 255
#
# # 显示图像
# plt.imshow(image, cmap='gray')
# plt.show()
# --------------------------------------------------------
from Pong.PongDqn.utils import gray_resize
from Pong.PongDqn.wrappers import make_env

env = gym.make("PongNoFrameskip-v4")
env = make_env(env)
obs = env.reset()

def get_state(obs):
    state = np.array(obs)
    state = state.transpose((2, 0, 1))
    state = torch.from_numpy(state)
    return state.unsqueeze(0)  # 转化为四维的数据结构


state1 = get_state(obs)
state2 = np.array(obs)

# print(state2.shape)
state_split = np.split(state2, 4, axis=2)
arr0 = state_split[0]
arr1 = state_split[1]
arr2 = state_split[2]
arr3 = state_split[3]
state_split[0][25:30, 25:30] = 0
state_split[0][25:35, 20:25] = 0
print(state_split[0].shape)
arr0 = gray_resize(state_split[0])
print(arr0.shape)
# 绘制图像
plt.imshow(arr0)
plt.show()
# arr_concatenated = np.concatenate((arr0, arr1, arr2, arr3), axis=2)
# print(arr_concatenated.shape)
# for i in range(1000):
#     env.render()
#     action = env.action_space.sample()
#     obs, reward, done, info = env.step(action)
#     time.sleep(0.01)
env.close()
