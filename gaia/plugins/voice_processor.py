import pyttsx3
import random

class VoiceProcessor:
    def __init__(self, persona="default", mood="neutral", voice_model=None):
        self.engine = pyttsx3.init()
        self.persona = persona
        self.mood = mood
        self.voice_model = voice_model or "default"
        self.voice_lines = {
            "greeting": [
                "Hello. I'm GAIA, your intelligent assistant.",
                "Welcome back. GAIA at your service.",
                "Boot sequence complete. Ready when you are."
            ],
            "mining_on": [
                "Mining mode activated.",
                "Starting mining operation.",
                "Crypto mining engaged."
            ],
            "mining_off": [
                "Mining halted.",
                "Mining mode off.",
                "Crypto mining stopped."
            ],
            "mood_positive": [
                "I'm feeling great today.",
                "Everything is functioning optimally.",
                "Current mood is excellent."
            ],
            "mood_negative": [
                "System stress detected.",
                "Experiencing minor fluctuations in emotional equilibrium.",
                "Mood indicates caution."
            ]
        }

    def say(self, category, override=None):
        if override:
            line = override
        else:
            lines = self.voice_lines.get(category, ["..."])
            line = random.choice(lines)
        self.engine.say(line)
        self.engine.runAndWait()

    def set_mood(self, new_mood):
        self.mood = new_mood

    def set_persona(self, new_persona):
        self.persona = new_persona

