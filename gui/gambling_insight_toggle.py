from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from gaia.core.plugin_registry import trigger_plugin_event

class GamblingInsightToggle(QWidget):
    def __init__(self):
        super().__init__()
        self.insight_enabled = False
        self.init_ui()

    def init_ui(self):
        self.toggle_button = QPushButton('Enable Casino Insight Mode')
        self.toggle_button.clicked.connect(self.toggle_insight_mode)

        self.status_label = QLabel('Casino Insight Mode: OFF')

        layout = QVBoxLayout()
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

    def toggle_insight_mode(self):
        self.insight_enabled = not self.insight_enabled
        state = "ON" if self.insight_enabled else "OFF"
        self.status_label.setText(f"Casino Insight Mode: {state}")
        self.toggle_button.setText('Disable Casino Insight Mode' if self.insight_enabled else 'Enable Casino Insight Mode')

        # Notify other systems
        trigger_plugin_event("on_insight_mode_toggle", {"enabled": self.insight_enabled})

