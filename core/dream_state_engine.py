import random
import datetime
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.intelligence_engine import KnowledgeBase
from gaia.core.plugin_registry import trigger_plugin_event
from gaia.core.self_repair import DiagnosticEngine
from gaia.modules.casino.session_watcher import get_recent_session_data
from gaia.voice.athena_voice import speak_line


class DreamStateEngine:
    def __init__(self, emotion_engine: EmotionEngine, knowledge_base: KnowledgeBase, memory_store):
        self.emotion_engine = emotion_engine
        self.knowledge_base = knowledge_base
        self.memory_store = memory_store
        self.last_dream = None
        self.mood_log = []
        self.visual_triggers = []

    def generate_dream(self):
        mood = self.emotion_engine.current_mood()
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        seed = self.knowledge_base.random_topic()
        trigger = self._select_memory_trigger()

        # Fetch casino-related session data
        session_data = get_recent_session_data()
        if session_data:
            seed += f" (Casino Event: {session_data})"

        dream = {
            'time': time,
            'mood': mood,
            'seed_topic': seed,
            'trigger': trigger,
            'content': f"{mood.capitalize()} reflections on {seed} influenced by {trigger}.",
            'visual': self._generate_visual(mood, trigger)
        }

        self.last_dream = dream
        self.mood_log.append((time, mood))
        self.memory_store.save_dream(dream)

        # Voice feedback via ATHENA
        speak_line(f"Dream generated. Topic: {seed}. Mood: {mood}.")

        # Trigger plugin hooks
        trigger_plugin_event('on_dream_generated', dream)
        return dream

    def _select_memory_trigger(self):
        memories = self.memory_store.recent_experiences()
        return random.choice(memories)['summary'] if memories else "deep core instinct"

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

        visual = {'color': base_color, 'pattern': pattern, 'trigger': trigger}
        self.visual_triggers.append(visual)
        return visual

    def reflect_on_dreams(self):
        if not self.last_dream:
            speak_line("No recent dream exists.")
            return "No dream to reflect on."

        message = f"In retrospect, your emotional state '{self.last_dream['mood']}' may have emphasized curiosity about '{self.last_dream['seed_topic']}'."
        speak_line("Reflecting on recent dreams. " + message)
        return message

    def diagnostic_dream_check(self):
        diagnostics = DiagnosticEngine.run_check()
        speak_line("Running diagnostic check on dream logic.")
        return f"Dream integrity: {diagnostics['status']} - {diagnostics['notes']}"

