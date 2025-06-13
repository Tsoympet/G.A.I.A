import pyttsx3
import random

class AthenaVoice:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.set_female_voice()
        self.moods = ["calm", "focused", "playful", "serious"]
        self.current_mood = "calm"

    def set_female_voice(self):
        for voice in self.voices:
            if "female" in voice.name.lower() or "english" in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break

    def speak(self, text, mood=None):
        mood = mood or self.current_mood
        if mood == "playful":
            text = f"Hehe~ {text}"
        elif mood == "serious":
            text = f"Attention: {text}"
        elif mood == "focused":
            text = f"Let's focus. {text}"
        self.engine.say(text)
        self.engine.runAndWait()

    def set_mood(self, mood):
        if mood in self.moods:
            self.current_mood = mood
        else:
            print(f"[ATHENA] Mood '{mood}' not recognized.")

    def intro(self):
        greetings = [
            "Welcome back. Athena is online.",
            "Hello, I'm here to assist.",
            "GAIA systems engaged. How may I help?"
        ]
        self.speak(random.choice(greetings))

# Example usage:
# voice = AthenaVoice()
# voice.intro()
# voice.set_mood("playful")
# voice.speak("Let's explore the crypto market!")
