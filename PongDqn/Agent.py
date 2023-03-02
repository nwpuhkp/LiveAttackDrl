import torch
import random

from PongDqn.Memory import ReplayMemory, Transition
from PongDqn.Network import DQN
import torch.optim as optim
import torch.nn.functional as F

from PongDqn.Parameter_sharing import madel_path, device, BATCH_SIZE, GAMMA


class DQN_agent:
    def __init__(self, in_channels=1, action_space=[], learning_rate=1e-3, memory_size=100000, epsilon=0.99):

        self.in_channels = in_channels
        self.action_space = action_space
        self.action_dim = self.action_space.n
        self.memory_buffer = ReplayMemory(memory_size)
        self.stepdone = 0
        self.DQN = DQN(self.in_channels, self.action_dim).cuda()
        self.target_DQN = DQN(self.in_channels, self.action_dim).cuda()
        # 加载之前训练好的模型
        self.DQN.load_state_dict(torch.load(madel_path))
        self.target_DQN.load_state_dict(self.DQN.state_dict())

        self.optimizer = optim.RMSprop(self.DQN.parameters(), lr=learning_rate, eps=0.001, alpha=0.95)

    def select_action(self, state):

        self.stepdone += 1
        state = state.to(device)
        # epsilon = EPS_END + (EPS_START - EPS_END) * \
        #           math.exp(-1. * self.stepdone / EPS_DECAY)
        epsilon = 0.02
        if random.random() < epsilon:
            action = torch.tensor([[random.randrange(self.action_dim)]], device=device, dtype=torch.long)
        else:
            action = self.DQN(state).detach().max(1)[1].view(1, 1)

        return action

    def test_select_action(self, state):  # 测试时不再添加随机探索的机制
        self.stepdone += 1
        state = state.to(device)
        action = self.DQN(state).detach().max(1)[1].view(1, 1)
        return action

    def learn(self):

        if self.memory_buffer.__len__() < BATCH_SIZE:
            return

        transitions = self.memory_buffer.sample(BATCH_SIZE)

        batch = Transition(*zip(*transitions))
        # print(batch)
        actions = tuple((map(lambda a: torch.tensor([[a]], device='cuda'), batch.action)))
        rewards = tuple((map(lambda r: torch.tensor([r], device='cuda'), batch.reward)))

        non_final_mask = torch.tensor(
            tuple(map(lambda s: s is not None, batch.next_state)),
            device=device, dtype=torch.uint8).bool()

        non_final_next_states = torch.cat([s for s in batch.next_state
                                           if s is not None]).to('cuda')

        # print(type(batch.state))
        state_batch = torch.cat(batch.state).to('cuda')
        action_batch = torch.cat(actions)
        reward_batch = torch.cat(rewards)

        state_action_values = self.DQN(state_batch).gather(1, action_batch)

        next_state_values = torch.zeros(BATCH_SIZE, device=device)
        next_state_values[non_final_mask] = self.target_DQN(non_final_next_states).max(1)[0].detach()
        expected_state_action_values = (next_state_values * GAMMA) + reward_batch

        loss = F.smooth_l1_loss(state_action_values, expected_state_action_values.unsqueeze(1))
        # print(loss)

        self.optimizer.zero_grad()
        loss.backward()
        for param in self.DQN.parameters():
            param.grad.data.clamp_(-1, 1)

        self.optimizer.step()
        return loss
