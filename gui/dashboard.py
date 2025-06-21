from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTabWidget, QPushButton
from gaia.gui.modules.casino_games_gui import CrashPanel, BaccaratPanel, PokerPanel
from gaia.modules.casino.crash_logic import CrashLogic
from gaia.modules.casino.baccarat_logic import BaccaratLogic
from gaia.modules.casino.poker_logic import PokerLogic
from gaia.gui.settings_panel import SettingsPanel
from gaia.gui.voice_panel import VoicePanel
from gaia.core.plugin_registry import trigger_plugin_event

class Dashboard(QWidget):
    def __init__(self, speech_engine=None):
        super().__init__()
        self.speech_engine = speech_engine
        self.insight_mode = False
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Top label
        layout.addWidget(QLabel("GAIA Dashboard"))

        # Casino Insight toggle button
        self.insight_button = QPushButton('Toggle Casino Insight Mode', self)
        self.insight_button.clicked.connect(self.toggle_insight_mode)
        self.status_label = QLabel('Casino Mode: OFF', self)
        layout.addWidget(self.insight_button)
        layout.addWidget(self.status_label)

        # Dashboard Tabs
        self.tabs = QTabWidget()
        self.tabs.addTab(CrashPanel(CrashLogic(), self.speech_engine), "Crash Game")
        self.tabs.addTab(BaccaratPanel(BaccaratLogic(), self.speech_engine), "Baccarat")
        self.tabs.addTab(PokerPanel(PokerLogic(), self.speech_engine), "Poker")
        self.tabs.addTab(SettingsPanel(), "Settings")
        self.tabs.addTab(VoicePanel(self.speech_engine), "Voice")

        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def toggle_insight_mode(self):
        self.insight_mode = not self.insight_mode
        status_text = "Casino Mode: ON" if self.insight_mode else "Casino Mode: OFF"
        self.status_label.setText(status_text)

        # π” Trigger optional plugin event
        trigger_plugin_event("casino_insight_mode_toggled", {"active": self.insight_mode})

        # π—£ Optional speech feedback
        if self.speech_engine:
            self.speech_engine.speak(f"Casino Insight Mode {'enabled' if self.insight_mode else 'disabled'}.")
