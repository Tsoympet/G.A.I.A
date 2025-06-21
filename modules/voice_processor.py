import speech_recognition as sr
import pyttsx3
import threading

class VoiceProcessor:
    def __init__(self, language='en', wake_words=['gaia'], emotional_tone='neutral'):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.language = language
        self.wake_words = wake_words
        self.emotional_tone = emotional_tone
        self.voice_lock = threading.Lock()
        self._configure_voice()

    def _configure_voice(self):
        voices = self.engine.getProperty('voices')
        lang_map = {
            'en': 'english',
            'el': 'greek',
            'es': 'spanish',
            'de': 'german',
            'fr': 'french'
        }
        for voice in voices:
            if lang_map.get(self.language, 'english') in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break

        rate = 150
        if self.emotional_tone == 'happy':
            rate = 180
        elif self.emotional_tone == 'sad':
            rate = 120
        elif self.emotional_tone == 'angry':
            rate = 200
        self.engine.setProperty('rate', rate)

    def speak(self, text):
        with self.voice_lock:
            self.engine.say(text)
            self.engine.runAndWait()

    def listen(self, timeout=5):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source, timeout=timeout)
            try:
                result = self.recognizer.recognize_google(audio, language=self.language)
                print(f"Recognized: {result}")
                if any(w in result.lower() for w in self.wake_words):
                    return result
                else:
                    return None
            except sr.UnknownValueError:
                print("Could not understand audio.")
                return None
            except sr.RequestError as e:
                print(f"Recognition error: {e}")
                return None

    def set_language(self, language):
        self.language = language
        self._configure_voice()

    def set_emotional_tone(self, tone):
        self.emotional_tone = tone
        self._configure_voice()
