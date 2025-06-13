import json
import random
import os

class Trainer:
    def __init__(self, model, memory_manager, log_fn=print):
        self.model = model
        self.memory = memory_manager
        self.log = log_fn

    def supervised_train(self, labeled_data, epochs=10, learning_rate=0.001):
        self.log("Starting supervised training...")
        for epoch in range(epochs):
            loss = 0.0
            for input_data, expected_output in labeled_data:
                prediction = self.model.predict(input_data)
                error = self.model.compute_loss(prediction, expected_output)
                self.model.backpropagate(error, learning_rate)
                loss += error
            self.log(f"Epoch {epoch+1}/{epochs}, Loss: {loss:.4f}")
        self.log("Supervised training completed.")

    def reinforcement_train(self, environment, episodes=100):
        self.log("Starting reinforcement training...")
        for episode in range(episodes):
            state = environment.reset()
            done = False
            total_reward = 0
            while not done:
                action = self.model.choose_action(state)
                next_state, reward, done, _ = environment.step(action)
                self.model.learn(state, action, reward, next_state)
                state = next_state
                total_reward += reward
            self.log(f"Episode {episode+1}, Total Reward: {total_reward}")
        self.log("Reinforcement training completed.")

    def dream_train(self):
        self.log("Starting dream state training...")
        dreams = self.memory.get_dreams()
        for i, dream in enumerate(dreams):
            prediction = self.model.predict(dream["input"])
            error = self.model.compute_loss(prediction, dream["ideal_output"])
            self.model.backpropagate(error, learning_rate=0.0005)
            self.log(f"Dream {i+1}/{len(dreams)} processed.")
        self.log("Dream state training completed.")

    def save_model(self, path="model_weights.json"):
        weights = self.model.export_weights()
        with open(path, "w") as f:
            json.dump(weights, f)
        self.log(f"Model saved to {path}")

    def load_model(self, path="model_weights.json"):
        if os.path.exists(path):
            with open(path, "r") as f:
                weights = json.load(f)
            self.model.load_weights(weights)
            self.log(f"Model loaded from {path}")
        else:
            self.log(f"No model file found at {path}")

