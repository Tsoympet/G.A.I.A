from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider, QPushButton
from PyQt5.QtCore import Qt

class SettingsPanel(QWidget):
    def __init__(self, config_manager, voice_module):
        super().__init__()
        self.config_manager = config_manager
        self.voice_module = voice_module
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.voice_label = QLabel("Voice Volume")
        self.voice_slider = QSlider(Qt.Horizontal)
        self.voice_slider.setMinimum(0)
        self.voice_slider.setMaximum(100)
        self.voice_slider.setValue(self.config_manager.get("voice_volume", 50))
        self.voice_slider.valueChanged.connect(self.adjust_voice_volume)

        self.save_button = QPushButton("Save Settings")
        self.save_button.clicked.connect(self.save_settings)

        layout.addWidget(self.voice_label)
        layout.addWidget(self.voice_slider)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def adjust_voice_volume(self, value):
        self.voice_module.set_volume(value)

    def save_settings(self):
        self.config_manager.set("voice_volume", self.voice_slider.value())
        self.config_manager.save()
        if self.voice_module:
            self.voice_module.say("Settings have been saved.")
