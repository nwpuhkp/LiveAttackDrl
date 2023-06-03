import torch

from torchviz import make_dot
from PongDqn.dqn.Network import DQN

x = torch.rand(1, 4, 84, 84)
model = DQN(4, 6)
y = model(x)

# 这三种方式都可以
g = make_dot(y)
# g=make_dot(y, params=dict(model.named_parameters()))
# g = make_dot(y, params=dict(list(model.named_parameters()) + [('x', x)]))
# 这两种方法都可以
g.view()  # 会生成一个 Digraph.gv.pdf 的PDF文件
# g.render('espnet_model', view=False)  # 会自动保存为一个 espnet.pdf，第二个参数为True,则会自动打开该PDF文件，为False则不打开
