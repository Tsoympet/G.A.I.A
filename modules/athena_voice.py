import random
from gaia.voice.voice_processor import VoiceProcessor
from gaia.core.emotion_engine import EmotionEngine

class AthenaVoice:
    def __init__(self, language="en"):
        self.language = language
        self.processor = VoiceProcessor(language=self.language)
        self.emotion_engine = EmotionEngine()

    def speak(self, key):
        phrase = self.get_phrase(key)
        self.processor.speak(phrase)

    def get_phrase(self, key):
        mood = self.emotion_engine.current_mood()
        library = self._load_voice_lines(mood)
        return library.get(key, "[voice line missing]")

    def _load_voice_lines(self, mood):
        base_lines = {
            "plugin_ready": [
                "All plugins are now online.",
                "Your plugins are now initialized and ready to go.",
                "Plugin system activated. Everything is ready."
            ],
            "diagnostic_ok": [
                "System diagnostic complete. No errors found.",
                "All systems nominal. You're good to go.",
                "Diagnostics report no issues. Integrity is stable."
            ],
            "dream_trigger": [
                "Activating dream-state reflection.",
                "Entering analytical introspection mode.",
                "Let's explore your subconscious reasoning."
            ],
            "greeting": [
                "Welcome back. I'm ready.",
                "Hello again. How can I assist?",
                "ATHENA online and standing by."
            ],
            "crypto_mode": [
                "Crypto markets analyzed. Forecast panel is ready.",
                "Entering crypto insight mode.",
                "Digital assets module is now active."
            ],
            "stock_mode": [
                "Stock analysis is ready. Loading market forecast.",
                "Equities module activated.",
                "Stock market insight now live."
            ]
        }

        # Optional mood-influenced variation
        if mood.lower() == "calm":
            for k in base_lines:
                base_lines[k] = [f"(Calm tone) {l}" for l in base_lines[k]]
        elif mood.lower() == "angry":
            for k in base_lines:
                base_lines[k] = [f"(Assertive) {l}" for l in base_lines[k]]

        return {k: random.choice(v) for k, v in base_lines.items()}
