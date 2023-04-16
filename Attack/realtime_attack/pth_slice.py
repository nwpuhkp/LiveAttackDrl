import pickle
import re
from PongDqn.dqn.wrappers import *
from PongDqn.dqn.Network import DQN
import torch
import filecmp


# 将一个pth模型文件按网络的各个层拆分为多个二进制文件
def slice_pth(pth_path):
    env = gym.make("PongNoFrameskip-v4")
    env = make_env(env)
    action_space = env.action_space
    state_channel = 4
    # 加载模型
    model = DQN(in_channels=state_channel, n_actions=action_space.n)
    model.load_state_dict(torch.load(pth_path, map_location='cpu'))
    for name, param in model.named_parameters():
        # print(name)  # 打印出网络的各个层
        # print(param.data.size())  # 打印出网络的各个层的参数的形状
        p = torch.nn.Parameter(param.data)  # 将网络的各个层的参数转换为Parameter类型
        torch.save(p,
                   'D:\CodeProject\Python\LiveAttackDrl\Attack\sliced_patched_model/' + name + '.bin')  # 将网络的各个层的参数保存为二进制文件
    print("done")


# 使用pickle将model中的参数保存为序列化文件
def pickle_model(model_path):
    env = gym.make("PongNoFrameskip-v4")
    env = make_env(env)
    action_space = env.action_space
    state_channel = 4
    # 加载模型
    model = DQN(in_channels=state_channel, n_actions=action_space.n)
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    # pickle
    for name, param in model.named_parameters():
        with open('D:\CodeProject\Python\LiveAttackDrl\Attack\pickled_model/' + name + '.pkl', 'wb') as f:
            pickle.dump(param, f)


# 将多个二进制文件合并为一个pth文件，从而验证拆分的正确性
def merge_pth(pth_path):
    model = {'conv1.bias': None, 'conv1.weight': None, 'conv2.bias': None, 'conv2.weight': None, 'conv3.bias': None,
             'conv3.weight': None,
             'fc4.bias': None, 'fc4.weight': None, 'head.bias': None, 'head.weight': None}
    for name, param in model.items():
        # print(name)
        # print(param)
        # print(model[name])
        model[name] = torch.load('./sliced_model/' + name + '.bin')
    torch.save(model, pth_path)


# 对比两个pth文件，如果相同返回True，否则返回False
def compare_pth(pth1, pth2):
    model1 = torch.load(pth1)
    model2 = torch.load(pth2)
    for name, param in model1.items():
        if not torch.equal(param.data, model2[name].data):
            return False
    return True


# 对比两个二进制文件，如果相同返回True，否则返回False
def compare_bin(bin1, bin2):
    if filecmp.cmp(bin1, bin2):
        print('The files are identical')
    else:
        print('The files are different')


# 主函数
if __name__ == '__main__':
    slice_pth('D:\CodeProject\Python\LiveAttackDrl\PongDqn\model\DQN_Pong_episode20.pth')
    # merge_pth('../merged_model/merged_model.pth')
    # if compare_pth('../PongDqn/model/DQN_Pong_episode1480.pth', './sliced_model/merged_model.pth'):
    #     print('The two pth files are the same.')
    # conv1_w = open("../sliced_model/conv1.weight.bin", 'rb').read()
    # conv1_w1 = re.escape(conv1_w)
    # conv1_w2 = re.compile(re.escape(conv1_w))
    # print(re.compile(re.escape(conv1_w)))
    # compare_bin('D:\CodeProject\Python\LiveAttackDrl\Attack\sliced_model2/conv1.weight.bin', 'D:\CodeProject\Python\LiveAttackDrl\Attack\sliced_model/conv1.weight.bin')
