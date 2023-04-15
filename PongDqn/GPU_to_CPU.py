import torch


def model_to_cpu(model_path1, model_path2):
    model = torch.load(model_path1, map_location=torch.device('cpu'))
    torch.save(model, model_path2)
    print("done")


if __name__ == '__main__':
    model_to_cpu('./model/DQN_Pong_episode20.pth', './cpu_model/DQN_Pong_episode20_cpu_model.pth')
