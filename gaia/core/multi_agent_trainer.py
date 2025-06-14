import random
import json
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.dream_state_engine import DreamStateEngine

class Agent:
    def __init__(self, name, strategy=None):
        self.name = name
        self.strategy = strategy or {}
        self.memory = []
        self.balance = 1000
        self.win_count = 0
        self.loss_count = 0

    def act(self, game_state):
        # Choose action based on strategy or randomness
        return random.choice(["call", "raise", "fold"])

    def observe(self, outcome):
        self.memory.append(outcome)
        if outcome['result'] == 'win':
            self.win_count += 1
            self.balance += outcome.get('amount', 0)
        else:
            self.loss_count += 1
            self.balance -= outcome.get('amount', 0)

    def evolve(self):
        if len(self.memory) > 10:
            self.strategy = {"risk": random.uniform(0, 1)}  # Simulated strategy shift

class MultiAgentTrainer:
    def __init__(self, dream: DreamStateEngine, emotion: EmotionEngine):
        self.agents = []
        self.dream = dream
        self.emotion = emotion

    def add_agent(self, name, strategy=None):
        agent = Agent(name, strategy)
        self.agents.append(agent)

    def simulate_round(self):
        if len(self.agents) < 2:
            return

        a, b = random.sample(self.agents, 2)
        result = random.choice(["a_wins", "b_wins", "tie"])
        pot = random.randint(50, 200)

        if result == "a_wins":
            a.observe({"result": "win", "amount": pot})
            b.observe({"result": "loss", "amount": pot})
        elif result == "b_wins":
            b.observe({"result": "win", "amount": pot})
            a.observe({"result": "loss", "amount": pot})
        else:
            a.observe({"result": "tie", "amount": 0})
            b.observe({"result": "tie", "amount": 0})

        # Emotion signal
        self.emotion.log_emotion("excitement", level=random.uniform(0.2, 0.8))

    def train_loop(self, iterations=10):
        for _ in range(iterations):
            self.simulate_round()
            for agent in self.agents:
                agent.evolve()

        # Store results in dream state
        dream_data = {
            "multi_agent_summary": [
                {
                    "agent": ag.name,
                    "wins": ag.win_count,
                    "losses": ag.loss_count,
                    "balance": ag.balance
                }
                for ag in self.agents
            ]
        }
        self.dream.store_memory("multi_agent_game_theory", dream_data)

    def get_summary(self):
        return [
            {
                "name": ag.name,
                "wins": ag.win_count,
                "losses": ag.loss_count,
                "balance": ag.balance,
                "strategy": ag.strategy
            }
            for ag in self.agents
        ]
