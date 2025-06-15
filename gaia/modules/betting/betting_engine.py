import random
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.intelligence_engine import KnowledgeBase
from gaia.modules.crypto.market_analyzer import MarketAnalyzer
from gaia.modules.casino.casino_behavior_model import CasinoBehaviorModel
from gaia.modules.voice.voice_processor import VoiceProcessor

class BettingEngine:
    def __init__(self, emotion_engine: EmotionEngine, knowledge_base: KnowledgeBase):
        self.emotion_engine = emotion_engine
        self.knowledge_base = knowledge_base
        self.market_analyzer = MarketAnalyzer()
        self.behavior_model = CasinoBehaviorModel()
        self.voice = VoiceProcessor()

    def predict_outcome(self, game_type: str, data: dict):
        mood = self.emotion_engine.current_mood()
        odds = self.behavior_model.analyze_game(game_type, data)
        confidence = min(100, random.randint(50, 100) + self.knowledge_base.infer_relevance(game_type))
        advice = f"Based on {mood} mood and current trends, {game_type} shows {confidence}% confidence."
        self.voice.speak(advice)
        return {
            'game_type': game_type,
            'confidence': confidence,
            'advice': advice
        }

    def adjust_bet(self, bankroll: float, confidence: int):
        multiplier = {
            'high': 0.10,
            'medium': 0.05,
            'low': 0.02
        }
        if confidence > 85:
            return bankroll * multiplier['high']
        elif confidence > 65:
            return bankroll * multiplier['medium']
        else:
            return bankroll * multiplier['low']
