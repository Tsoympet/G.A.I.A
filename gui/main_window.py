from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from gaia.gui.dashboard import Dashboard
from gaia.gui.settings_panel import SettingsPanel
from gaia.gui.voice_panel import VoicePanel

class MainWindow(QMainWindow):
    def __init__(self, core, speech=None):
        super().__init__()
        self.setWindowTitle("GAIA - Intelligent Dashboard")
        self.setMinimumSize(1280, 800)

        self.stack = QStackedWidget()
        self.dashboard = Dashboard(core, speech=speech)
        self.settings_panel = SettingsPanel(core)
        self.voice_panel = VoicePanel(speech=speech)

        self.stack.addWidget(self.dashboard)
        self.stack.addWidget(self.settings_panel)
        self.stack.addWidget(self.voice_panel)

        self.setCentralWidget(self.stack)

    def switch_to_dashboard(self):
        self.stack.setCurrentWidget(self.dashboard)

    def switch_to_settings(self):
        self.stack.setCurrentWidget(self.settings_panel)

    def switch_to_voice(self):
        self.stack.setCurrentWidget(self.voice_panel)
