import pyttsx3
import time
import random

class AthenaVoice:
    def __init__(self, language='en', voice_profile='default'):
        self.engine = pyttsx3.init()
        self.language = language
        self.set_voice_profile(voice_profile)
        self.emotion_state = 'neutral'

    def set_voice_profile(self, profile_name):
        voices = self.engine.getProperty('voices')
        if profile_name == 'scarlet':
            # Attempt to set to a feminine voice
            for voice in voices:
                if 'female' in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    break
        else:
            self.engine.setProperty('voice', voices[0].id)

    def set_emotion(self, emotion):
        self.emotion_state = emotion

    def speak(self, text):
        rate = 150
        pitch_mod = 0
        volume = 1.0

        if self.emotion_state == 'excited':
            rate = 180
            volume = 1.2
        elif self.emotion_state == 'calm':
            rate = 120
            volume = 0.9
        elif self.emotion_state == 'angry':
            rate = 200
            pitch_mod = -10
            volume = 1.0
        elif self.emotion_state == 'sad':
            rate = 110
            volume = 0.7

        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

        self.engine.say(text)
        self.engine.runAndWait()

    def introduce_self(self):
        greetings = [
            "Hello, I am Athena. Your adaptive AI assistant.",
            "Welcome back. Athena online and operational.",
            "System initialized. Athena is ready to assist you."
        ]
        self.speak(random.choice(greetings))
