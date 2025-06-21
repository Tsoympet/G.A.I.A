import os
import datetime
import torch

class NeuralWeightsUpdater:
    def __init__(self, model, optimizer, checkpoint_dir='checkpoints/'):
        self.model = model
        self.optimizer = optimizer
        self.checkpoint_dir = checkpoint_dir
        os.makedirs(self.checkpoint_dir, exist_ok=True)

    def save_checkpoint(self, label='latest'):
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        checkpoint_path = os.path.join(self.checkpoint_dir, f"{label}_{timestamp}.pt")
        torch.save({
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict()
        }, checkpoint_path)
        return checkpoint_path

    def load_checkpoint(self, path):
        if not os.path.isfile(path):
            raise FileNotFoundError(f"No checkpoint found at {path}")
        checkpoint = torch.load(path)
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        return True

    def update_weights(self, loss):
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        return "Weights updated based on new loss signal."
