# dream_mutator_rnn.py
# RNN / LSTM for dream pattern evolution

class DreamMutatorRNN:
    def __init__(self, input_dim, hidden_dim, output_dim):
        import torch.nn as nn
        self.rnn = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.decoder = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        out, _ = self.rnn(x)
        return self.decoder(out)
