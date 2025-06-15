import random
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.memory_manager import MemoryManager
from gaia.core.intelligence_engine import KnowledgeBase
from gaia.modules.casino.casino_behavior_model import CasinoBehaviorModel

class MultiAgentTrainer:
    def __init__(self, agents, memory: MemoryManager, emotion: EmotionEngine, knowledge: KnowledgeBase):
        self.agents = agents
        self.memory = memory
        self.emotion = emotion
        self.knowledge = knowledge
        self.behavior_model = CasinoBehaviorModel()

    def simulate_interaction(self, context):
        logs = []
        for agent in self.agents:
            emotional_bias = self.emotion.current_mood()
            knowledge_influence = self.knowledge.random_topic()
            behavior = self.behavior_model.simulate_behavior(context, emotional_bias)
            response = agent.react_to(context, behavior, knowledge_influence)
            self.memory.store_experience(agent.name, context, response)
            logs.append({
                'agent': agent.name,
                'emotion': emotional_bias,
                'behavior': behavior,
                'response': response
            })
        return logs

    def train_agents(self, iterations=10, scenario="poker"):
        for _ in range(iterations):
            context = self.behavior_model.generate_scenario(scenario)
            log = self.simulate_interaction(context)
            print("Interaction Log:", log)
