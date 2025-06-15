from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTabWidget
from gaia.gui.modules.casino_games_gui import CrashPanel, BaccaratPanel, PokerPanel
from gaia.modules.casino.crash_logic import CrashLogic
from gaia.modules.casino.baccarat_logic import BaccaratLogic
from gaia.modules.casino.poker_logic import PokerLogic
from gaia.gui.settings_panel import SettingsPanel
from gaia.gui.voice_panel import VoicePanel

class Dashboard(QWidget):
    def __init__(self, speech_engine=None):
        super().__init__()
        self.speech_engine = speech_engine
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        # Add tabs
        self.tabs.addTab(CrashPanel(CrashLogic(), self.speech_engine), "Crash Game")
        self.tabs.addTab(BaccaratPanel(BaccaratLogic(), self.speech_engine), "Baccarat")
        self.tabs.addTab(PokerPanel(PokerLogic(), self.speech_engine), "Poker")
        self.tabs.addTab(SettingsPanel(), "Settings")
        self.tabs.addTab(VoicePanel(self.speech_engine), "Voice")

        layout.addWidget(QLabel("GAIA Dashboard"))
        layout.addWidget(self.tabs)
        self.setLayout(layout)
