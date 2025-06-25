# reinforcement_learning.py
# Reinforcement learning module (Q-Learning, DQN)

class QLearningAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q = {}
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def choose_action(self, state):
        if state not in self.q:
            self.q[state] = [0.0 for _ in self.actions]
        import random
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        return self.actions[self.q[state].index(max(self.q[state]))]

    def learn(self, state, action, reward, next_state):
        if state not in self.q:
            self.q[state] = [0.0 for _ in self.actions]
        if next_state not in self.q:
            self.q[next_state] = [0.0 for _ in self.actions]
        a_idx = self.actions.index(action)
        predict = self.q[state][a_idx]
        target = reward + self.gamma * max(self.q[next_state])
        self.q[state][a_idx] += self.alpha * (target - predict)
