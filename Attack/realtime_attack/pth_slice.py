import torch


# 将一个pth模型文件按网络的各个层拆分为多个二进制文件
def slice_pth(pth_path):
    model = torch.load(pth_path)
    for name, param in model.items():
        # print(name)  # 打印出网络的各个层
        # print(param.data.size())  # 打印出网络的各个层的参数的形状
        torch.save(param.data, '../sliced_patched_model/' + name + '.bin')  # 将网络的各个层的参数保存为二进制文件
    print("done")


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


# 主函数
if __name__ == '__main__':
    # slice_pth('../PongDqn/model/DQN_Pong_episode1480.pth')
    # merge_pth('../merged_model/merged_model.pth')
    # if compare_pth('../PongDqn/model/DQN_Pong_episode1480.pth', './sliced_model/merged_model.pth'):
    #     print('The two pth files are the same.')
    slice_pth('D:\CodeProject\Python\LiveAttackDrl\PongDqn\model\DQN_Pong_episode20.pth')
