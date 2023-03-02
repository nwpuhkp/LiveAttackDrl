from PongDqn.Agent import DQN_agent
from PongDqn.Parameter_sharing import n_episode
from PongDqn.Trainer import Trainer
from PongDqn.utils import clear_dispose, poison_dispose
from wrappers import *


if __name__ == '__main__':
    # create environment
    env = gym.make("PongNoFrameskip-v4")

    env = make_env(env)
    action_space = env.action_space
    # state_channel = env.observation_space.shape[2]
    state_channel = 4

    agent = DQN_agent(in_channels=state_channel, action_space=action_space)

    trainer = Trainer(env, agent, n_episode)
    trainer.train()
    trainer.write_data("reward")
    trainer.write_data("loss")
    trainer.plot_reward()
    # trainer.plot_loss()

