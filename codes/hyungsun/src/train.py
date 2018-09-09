import torch
import torch.optim as optim
import torch.nn.functional as F
import time
from data import MNIST
from model import CNN
from config import *
import glob


# TODO(hyungsun): Make this more general.
class Trainer(object):
    def __init__(self, model, data_loader, optimizer, criterion, is_eval):
        cuda = torch.cuda.is_available()
        self.model = model
        self.data_loader = data_loader.eval_data() if is_eval else data_loader.training_data()
        self.device = torch.device("cuda" if cuda else "cpu")
        self.optimizer = optimizer
        self.prefix = "checkpoints/" + model.__class__.__name__ + "_"
        self.default_filename = self.prefix + str(int(time.time())) + ".pt"
        self.current_epoch = 0
        self.criterion = criterion
        
    def save_checkpoint(self):
        checkpoint = {
            "epoch": self.current_epoch + 1,
            "model": self.model.state_dict(),
            "optimizer": self.optimizer.state_dict(),
        }
        torch.save(checkpoint, self.default_filename)

    def load_checkpoint(self):
        file_names = glob.glob(self.prefix + "*.pt")
        if len(file_names) == 0:
            print("[!] Checkpoint not found.")
            return False
        file_name = file_names[-1]  # Pick the most recent file.
        checkpoint = torch.load(file_name)
        self.current_epoch = checkpoint["epoch"]
        self.optimizer.load_state_dict(checkpoint["optimizer"])
        self.model.load_state_dict(checkpoint["model"])
        print("[+] Checkpoint Loaded. '{}'".format(file_name))
        return True

    def train(self, max_epoch):
        self.model.train()
        self.load_checkpoint()
        for max_epoch in range(1, max_epoch + 1):
            self.current_epoch = max_epoch
            for batch_idx, (data, target) in enumerate(self.data_loader):
                data, target = data.to(self.device), target.to(self.device)
                self.optimizer.zero_grad()
                output = self.model(data)
                loss = self.criterion(output, target)
                loss.backward()
                self.optimizer.step()
                if batch_idx % 100 == 0:
                    self.save_checkpoint()
                    print("Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}".format(
                        max_epoch, batch_idx * len(data), len(self.data_loader.dataset),
                                   100. * batch_idx / len(self.data_loader), loss.item()))
        self.save_checkpoint()

    def evaluate(self):
        self.model.eval()
        self.load_checkpoint()
        test_loss = 0
        correct = 0
        with torch.no_grad():
            for data, target in self.data_loader:
                data, target = data.to(self.device), target.to(self.device)
                output = self.model(data)
                test_loss += F.nll_loss(output, target, reduction='sum').item()  # sum up batch loss
                pred = output.max(1, keepdim=True)[1]  # get the index of the max log-probability
                correct += pred.eq(target.view_as(pred)).sum().item()

        test_loss /= len(self.data_loader.dataset)
        print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
            test_loss, correct, len(self.data_loader.dataset),
            100. * correct / len(self.data_loader.dataset)))


def train_cnn():
    model = CNN()
    config = ConfigManager(model).load()
    optimizer = optim.SGD(model.parameters(), lr=float(config["LEARNING_RATE"]), momentum=float(config["MOMENTUM"]))
    criterion = torch.nn.NLLLoss()
    trainer = Trainer(model, MNIST(batch_size=10), optimizer, criterion, True)
    trainer.train(5)


def train_eval():
    model = CNN()
    config = ConfigManager(model).load()
    optimizer = optim.SGD(model.parameters(), lr=float(config["LEARNING_RATE"]), momentum=float(config["MOMENTUM"]))
    criterion = torch.nn.NLLLoss()
    trainer = Trainer(model, MNIST(batch_size=10), optimizer, criterion, True)
    trainer.evaluate()

def main():
    train_cnn()


if __name__ == "__main__":
    main()