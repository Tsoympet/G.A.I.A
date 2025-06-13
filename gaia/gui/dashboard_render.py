from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class DashboardRender(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GAIA Dashboard")
        self.setStyleSheet("background-color: #101820; color: white;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("GAIA Superintelligence Dashboard")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        status_row = QHBoxLayout()
        self.intelligence_label = QLabel("π§  Intelligence Level: 99.9")
        self.mood_label = QLabel("π’« Mood: Reflective")
        self.exp_label = QLabel("π“ Experience: 87.5%")
        for lbl in [self.intelligence_label, self.mood_label, self.exp_label]:
            lbl.setFont(QFont("Arial", 12))
            status_row.addWidget(lbl)

        self.main_buttons = QHBoxLayout()
        self.crypto_btn = QPushButton("Crypto Module")
        self.stock_btn = QPushButton("Stock Module")
        self.betting_btn = QPushButton("Sports Betting")
        self.casino_btn = QPushButton("Casino Games")
        self.settings_btn = QPushButton("Settings")

        for btn in [self.crypto_btn, self.stock_btn, self.betting_btn, self.casino_btn, self.settings_btn]:
            btn.setStyleSheet("background-color: #1A1A2E; color: #00FFF7; padding: 10px;")
            self.main_buttons.addWidget(btn)

        layout.addWidget(title)
        layout.addLayout(status_row)
        layout.addLayout(self.main_buttons)

        self.setLayout(layout)

