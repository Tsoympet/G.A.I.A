import random
import datetime
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.intelligence_engine import KnowledgeBase
from gaia.core.plugin_registry import trigger_plugin_event
from gaia.core.self_repair import DiagnosticEngine

# New modules
from gaia.modules.casino.casino_behavior_model import CasinoBehaviorModel
from gaia.modules.trading.quantum_forecaster import QuantumForecaster
from gaia.modules.feedback.emotion_feedback_loop import EmotionFeedbackLoop
from gaia.modules.training.multi_agent_trainer import MultiAgentTrainer


class DreamStateEngine:
    def __init__(self, emotion_engine: EmotionEngine, knowledge_base: KnowledgeBase, memory_store):
        self.emotion_engine = emotion_engine
        self.knowledge_base = knowledge_base
        self.memory_store = memory_store
        self.last_dream = None
        self.mood_log = []
        self.visual_triggers = []
        self.mode = "default"  # Modes: casino, forecast, training, emotional
        # Instantiated modules
        self.casino_ai = CasinoBehaviorModel()
        self.forecaster = QuantumForecaster()
        self.emotion_loop = EmotionFeedbackLoop()
        self.agent_trainer = MultiAgentTrainer()

    def set_mode(self, mode):
        self.mode = mode

    def generate_dream(self):
        mood = self.emotion_engine.current_mood()
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        seed = self.knowledge_base.random_topic()
        trigger = self._select_memory_trigger()

        content = f"{mood.capitalize()} reflections on {seed} influenced by {trigger}."
        visual = self._generate_visual(mood, trigger)

        # Inject mode-specific dream features
        if self.mode == "casino":
            casino_data = self.casino_ai.analyze_latest_session()
            content += f"\nCasino insight: {casino_data['prediction_summary']}"
            visual['pattern'] = "roulette" if "slot" in casino_data['game_type'] else "grid"

        elif self.mode == "forecast":
            forecast = self.forecaster.predict(seed)
            content += f"\nQuantum forecast: {forecast['insight']}"
            visual['pattern'] = "orbital"

        elif self.mode == "emotional":
            emotion_feedback = self.emotion_loop.loop_emotion(seed, mood)
            content += f"\nEmotional feedback: {emotion_feedback}"

        elif self.mode == "training":
            scenario = self.agent_trainer.simulate_scenario(seed)
            content += f"\nMulti-agent scenario: {scenario}"

        dream = {
            'time': time,
            'mood': mood,
            'seed_topic': seed,
            'trigger': trigger,
            'content': content,
            'visual': visual
        }

        self.last_dream = dream
        self.mood_log.append((time, mood))
        self.memory_store.save_dream(dream)
        trigger_plugin_event('on_dream_generated', dream)
        return dream

    def _select_memory_trigger(self):
        memories = self.memory_store.recent_experiences()
        if not memories:
            return "deep core instinct"
        return random.choice(memories)['summary']

    def _generate_visual(self, mood, trigger):
        base_color = {
            'joyful': '#FFD700',
            'calm': '#87CEFA',
            'sad': '#708090',
            'angry': '#DC143C',
            'curious': '#7FFF00',
            'neutral': '#D3D3D3'
        }.get(mood.lower(), '#FFFFFF')
        pattern = random.choice(['wave', 'pulse', 'grid', 'orbital'])

        self.visual_triggers.append({
            'color': base_color,
            'pattern': pattern,
            'trigger': trigger
        })

        return {
            'color': base_color,
            'pattern': pattern,
            'trigger': trigger
        }

    def reflect_on_dreams(self):
        if not self.last_dream:
            return "No dream to reflect on."
        reflection = f"In retrospect, your emotional state '{self.last_dream['mood']}' emphasized curiosity about '{self.last_dream['seed_topic']}'."
        return reflection

    def diagnostic_dream_check(self):
        diagnostics = DiagnosticEngine.run_check()
        return f"Dream integrity: {diagnostics['status']} - {diagnostics['notes']}"
