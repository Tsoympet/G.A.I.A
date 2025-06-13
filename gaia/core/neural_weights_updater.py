import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AdamW

class NeuralWeightsUpdater:
    def __init__(self, model_name='gpt2', lr=5e-5):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.optimizer = AdamW(self.model.parameters(), lr=lr)

    def tokenize(self, texts):
        return self.tokenizer(texts, return_tensors="pt", padding=True, truncation=True)

    def fine_tune(self, input_texts, target_texts, epochs=1):
        self.model.train()
        inputs = self.tokenize(input_texts)
        targets = self.tokenize(target_texts)["input_ids"]
        for _ in range(epochs):
            outputs = self.model(**inputs, labels=targets)
            loss = outputs.loss
            loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()

    def save_model(self, path='fine_tuned_model'):
        self.model.save_pretrained(path)
        self.tokenizer.save_pretrained(path)
        print(f"Saved model to {path}")

    def load_model(self, path):
        self.model = AutoModelForCausalLM.from_pretrained(path)
        self.tokenizer = AutoTokenizer.from_pretrained(path)
        print(f"Loaded model from {path}")
