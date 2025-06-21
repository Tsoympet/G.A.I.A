import os
import threading
import time
import speech_recognition as sr
from gaia.voice.athena_voice import AthenaVoice

class SpeechBridge:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.active = False
        self.voice = AthenaVoice()

    def start_listening(self):
        self.active = True
        listener_thread = threading.Thread(target=self._listen_loop)
        listener_thread.start()

    def _listen_loop(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.active:
                try:
                    print("Listening...")
                    audio = self.recognizer.listen(source, timeout=5)
                    command = self.recognizer.recognize_google(audio)
                    print(f"Recognized: {command}")
                    self._process_command(command)
                except sr.WaitTimeoutError:
                    continue
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")

    def _process_command(self, command):
        if "stop listening" in command.lower():
            self.voice.speak("Disengaging voice mode.")
            self.active = False
        elif "hello" in command.lower():
            self.voice.speak("Hello. I am GAIA. Ready to assist.")
        else:
            self.voice.speak(f"You said: {command}")

    def stop_listening(self):
        self.active = False

if __name__ == "__main__":
    bridge = SpeechBridge()
    bridge.start_listening()
