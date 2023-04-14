import torch


def model_to_cpu(model_path1, model_path2):
    model = torch.load(model_path1, map_location=torch.device('cpu'))
    torch.save(model.state_dict(), model_path2)


if __name__ == '__main__':
    model_to_cpu('./cpu_model', './cpu_model.pth')
