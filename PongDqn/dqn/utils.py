import csv

import cv2
import numpy as np
import torch
import gym
from matplotlib import pyplot as plt
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .wrappers import make_env


def gray_resize(color_img):
    # 将彩色图像转换为灰度图像
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    # 缩放图像
    gray_img = cv2.resize(gray_img, (84, 84), interpolation=cv2.INTER_AREA)
    # 将灰度图像转换为三维数组
    gray_img = gray_img[:, :, np.newaxis]
    return gray_img


def obs_split(state):
    # 由于env将4帧图片合并为一组，需要拆分处理
    state_split = np.split(state, 4, axis=2)
    return state_split


def obs_concatenate(arr0, arr1, arr2, arr3):
    # 重新合并
    return np.concatenate((arr0, arr1, arr2, arr3), axis=2)


def poison(state):
    # 在图片的左上方植入黑色/白色方块
    state[25:30, 25:30] = 0
    state[25:35, 20:25] = 0
    return state


def clear_dispose(obs):
    state = np.array(obs)
    state_split = obs_split(state)
    for i in range(4):
        state_split[i] = gray_resize(state_split[i])
    state = obs_concatenate(state_split[0], state_split[1], state_split[2], state_split[3])
    state = state.transpose((2, 0, 1))
    state = torch.from_numpy(state)
    return state.unsqueeze(0)  # 转化为四维的数据结构


def poison_dispose(obs):
    state = np.array(obs)
    state_split = obs_split(state)
    for i in range(4):
        poison(state_split[i])
        state_split[i] = gray_resize(state_split[i])
    state = obs_concatenate(state_split[0], state_split[1], state_split[2], state_split[3])
    state = state.transpose((2, 0, 1))
    state = torch.from_numpy(state)
    return state.unsqueeze(0)  # 转化为四维的数据结构


def plot_poison(obs):
    state = np.array(obs)
    state_split = obs_split(state)
    for i in range(4):
        poison(state_split[i])
        state_split[i] = gray_resize(state_split[i])
        plt.imshow(state_split[i])
        plt.show()


def plot_reward(reward_list):

    plt.plot(reward_list)
    plt.xlabel("step")
    plt.ylabel("reward")
    plt.title('reward_history')
    plt.show()


def csv_reader(csv_path):
    # 读取csv文件，并以数字的方式存放在列表中
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
        data = np.array(data)
        data = data.astype(np.float)
    return data


if __name__ == '__main__':
    # 测试函数效果
    env = gym.make("PongNoFrameskip-v4")
    env = make_env(env)
    obs = env.reset()
    plot_poison(obs)
    env.close()
