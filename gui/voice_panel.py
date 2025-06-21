from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from gaia.modules.voice.voice_processor import VoiceProcessor

class VoicePanel(QWidget):
    def __init__(self, speech: VoiceProcessor):
        super().__init__()
        self.speech = speech
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.status_label = QLabel("Voice system idle.")
        speak_button = QPushButton("Test Voice")
        speak_button.clicked.connect(self.test_speech)

        layout.addWidget(self.status_label)
        layout.addWidget(speak_button)
        self.setLayout(layout)

    def test_speech(self):
        message = "Hello, I am GAIA. Your voice interface is now active."
        self.status_label.setText("Speaking: " + message)
        if self.speech:
            self.speech.say(message)
