from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget
from gaia.gui.dashboard import Dashboard
from gaia.gui.settings_panel import SettingsPanel
from gaia.gui.voice_panel import VoicePanel
from gaia.gui.mining_panel import MiningPanel
from gaia.gui.modules.casino_games_gui import CrashPanel, BaccaratPanel, PokerPanel

class MainWindow(QMainWindow):
    def __init__(self, crash_logic, baccarat_logic, poker_logic, speech_engine):
        super().__init__()
        self.setWindowTitle("GAIA - General AI Assistant")
        self.setGeometry(100, 100, 1280, 800)

        # Stacked widget to switch between views
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Dashboard
        self.dashboard = Dashboard()
        self.stack.addWidget(self.dashboard)

        # Settings
        self.settings_panel = SettingsPanel()
        self.stack.addWidget(self.settings_panel)

        # Voice panel
        self.voice_panel = VoicePanel()
        self.stack.addWidget(self.voice_panel)

        # Mining panel
        self.mining_panel = MiningPanel()
        self.stack.addWidget(self.mining_panel)

        # Casino panels
        self.crash_panel = CrashPanel(crash_logic, speech_engine)
        self.baccarat_panel = BaccaratPanel(baccarat_logic, speech_engine)
        self.poker_panel = PokerPanel(poker_logic, speech_engine)
        self.stack.addWidget(self.crash_panel)
        self.stack.addWidget(self.baccarat_panel)
        self.stack.addWidget(self.poker_panel)

        # Default view
        self.stack.setCurrentWidget(self.dashboard)

    def switch_to(self, widget_name):
        if widget_name == "dashboard":
            self.stack.setCurrentWidget(self.dashboard)
        elif widget_name == "settings":
            self.stack.setCurrentWidget(self.settings_panel)
        elif widget_name == "voice":
            self.stack.setCurrentWidget(self.voice_panel)
        elif widget_name == "mining":
            self.stack.setCurrentWidget(self.mining_panel)
        elif widget_name == "crash":
            self.stack.setCurrentWidget(self.crash_panel)
        elif widget_name == "baccarat":
            self.stack.setCurrentWidget(self.baccarat_panel)
        elif widget_name == "poker":
            self.stack.setCurrentWidget(self.poker_panel)

