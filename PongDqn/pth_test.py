import torch

pthfile = r'D:\CodeProject\Python\LiveAttackDrl\PongDqn\model\DQN_Pong_episode1480.pth'
net = torch.load(pthfile, map_location=torch.device('cpu'))
# 打印网络结构
print(net)
# 打印网络的类型
print(type(net))
# 打印网络参数的键值对
print(len(net))
