import pyttsx3
import threading

class SpeechBridge:
    def __init__(self, voice_id=None, rate=180, volume=1.0):
        self.engine = pyttsx3.init()
        if voice_id:
            self.engine.setProperty('voice', voice_id)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        self.lock = threading.Lock()

    def say(self, text):
        def speak():
            with self.lock:
                self.engine.say(text)
                self.engine.runAndWait()

        thread = threading.Thread(target=speak)
        thread.start()

    def list_voices(self):
        voices = self.engine.getProperty('voices')
        return [(voice.id, voice.name) for voice in voices]

    def set_voice_by_name(self, name):
        for voice in self.engine.getProperty('voices'):
            if name.lower() in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                return True
        return False

    def set_rate(self, rate):
        self.engine.setProperty('rate', rate)

    def set_volume(self, volume):
        self.engine.setProperty('volume', volume)

