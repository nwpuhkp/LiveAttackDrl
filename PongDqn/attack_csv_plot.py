from PongDqn.dqn.utils import plot_reward, csv_reader

list1 = csv_reader("./total_reward.csv")
plot_reward(list1)
