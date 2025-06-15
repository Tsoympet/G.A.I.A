from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

class CrashPanel(QWidget):
    def __init__(self, crash, speech=None):
        super().__init__()
        self.crash = crash
        self.speech = speech
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.history_label = QLabel("Crash History: []")
        self.suggest_label = QLabel("Recommended Cashout: -")
        btn_log = QPushButton("Log 2.0x")
        btn_log.clicked.connect(lambda: self.update_log(2.0))
        layout.addWidget(self.history_label)
        layout.addWidget(self.suggest_label)
        layout.addWidget(btn_log)
        self.setLayout(layout)

    def update_log(self, value):
        self.crash.log_multiplier(value)
        self.history_label.setText(f"Crash History: {self.crash.history[-5:]}")
        suggestion = self.crash.recommend_cashout()
        self.suggest_label.setText(f"Recommended Cashout: {suggestion:.2f}x")
        if self.speech:
            self.speech.say(f"Suggested cashout is {suggestion:.2f} times.")

class BaccaratPanel(QWidget):
    def __init__(self, baccarat, speech=None):
        super().__init__()
        self.baccarat = baccarat
        self.speech = speech
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.streak_label = QLabel("No streak yet")
        btn_p = QPushButton("Player")
        btn_b = QPushButton("Banker")
        btn_t = QPushButton("Tie")
        btn_p.clicked.connect(lambda: self.log('player'))
        btn_b.clicked.connect(lambda: self.log('banker'))
        btn_t.clicked.connect(lambda: self.log('tie'))
        layout.addWidget(self.streak_label)
        layout.addWidget(btn_p)
        layout.addWidget(btn_b)
        layout.addWidget(btn_t)
        self.setLayout(layout)

    def log(self, result):
        self.baccarat.log_result(result)
        streak = self.baccarat.last_streak()
        self.streak_label.setText(f"Last streak: {streak[1]}x {streak[0]}")
        if self.speech and streak[1] >= 3:
            self.speech.say(f"Attention. {streak[1]} {streak[0]} wins in a row.")

class PokerPanel(QWidget):
    def __init__(self, poker, speech=None):
        super().__init__()
        self.poker = poker
        self.speech = speech
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.stats_label = QLabel("Hands: 0 | Wins: 0")
        self.bluff_label = QLabel("Bluff Suggestion: --")
        btn_win = QPushButton("Log Win")
        btn_loss = QPushButton("Log Loss")
        btn_win.clicked.connect(lambda: self.log(True))
        btn_loss.clicked.connect(lambda: self.log(False))
        layout.addWidget(self.stats_label)
        layout.addWidget(self.bluff_label)
        layout.addWidget(btn_win)
        layout.addWidget(btn_loss)
        self.setLayout(layout)

    def log(self, won):
        self.poker.log_hand(won)
        win_rate = self.poker.win_rate()
        bluff = self.poker.should_bluff()
        self.stats_label.setText(f"Hands: {self.poker.hands_played} | Wins: {self.poker.total_wins}")
        self.bluff_label.setText(f"Bluff Suggestion: {'Yes' if bluff else 'No'}")
        if self.speech:
            msg = "You may consider bluffing." if bluff else "No need to bluff now."
            self.speech.say(msg)
