from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTabWidget, QProgressBar, QListWidget, QPushButton
from PyQt5.QtCore import Qt
from gaia.core.dream_state_engine import DreamStateEngine
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.plugin_registry import list_installed_plugins, install_plugin

class LearningConsole(QWidget):
    def __init__(self, emotion_engine: EmotionEngine, dream_engine: DreamStateEngine):
        super().__init__()
        self.emotion_engine = emotion_engine
        self.dream_engine = dream_engine
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        tabs = QTabWidget()

        # Mood Map
        self.mood_progress = QProgressBar()
        self.mood_progress.setMaximum(100)
        self.mood_label = QLabel("Mood: Unknown")
        mood_tab = QWidget()
        mood_layout = QVBoxLayout()
        mood_layout.addWidget(self.mood_label)
        mood_layout.addWidget(self.mood_progress)
        mood_tab.setLayout(mood_layout)
        tabs.addTab(mood_tab, "Mood")

        # Dream Log
        self.dream_list = QListWidget()
        self.refresh_dreams()
        dream_tab = QWidget()
        dream_layout = QVBoxLayout()
        dream_layout.addWidget(self.dream_list)
        dream_tab.setLayout(dream_layout)
        tabs.addTab(dream_tab, "Dreams")

        # Growth
        self.growth_progress = QProgressBar()
        self.growth_progress.setMaximum(100)
        self.growth_label = QLabel("Forecast Accuracy")
        growth_tab = QWidget()
        growth_layout = QVBoxLayout()
        growth_layout.addWidget(self.growth_label)
        growth_layout.addWidget(self.growth_progress)
        growth_tab.setLayout(growth_layout)
        tabs.addTab(growth_tab, "Growth")

        layout.addWidget(tabs)
        self.setLayout(layout)
        self.update_stats()

    def update_stats(self):
        mood = self.emotion_engine.current_mood()
        self.mood_label.setText(f"Current Mood: {mood}")
        mood_val = self.emotion_engine.mood_intensity()
        self.mood_progress.setValue(mood_val)
        self.growth_progress.setValue(self.estimate_growth())

    def refresh_dreams(self):
        self.dream_list.clear()
        for d in self.dream_engine.memory_store.get_recent_dreams():
            self.dream_list.addItem(f"{d['time']} | {d['mood']} | {d['seed_topic']}")

    def estimate_growth(self):
        # Stub for calculating accuracy/growth
        return 73  # Replace with real learning metric


# Plugin Store Panel
class PluginStore(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.plugin_list = QListWidget()
        self.refresh_plugins()
        self.install_btn = QPushButton("Install Selected Plugin")
        self.install_btn.clicked.connect(self.install_selected)

        layout.addWidget(QLabel("Available Plugins"))
        layout.addWidget(self.plugin_list)
        layout.addWidget(self.install_btn)
        self.setLayout(layout)

    def refresh_plugins(self):
        self.plugin_list.clear()
        for p in list_installed_plugins():
            self.plugin_list.addItem(p)

    def install_selected(self):
        selected = self.plugin_list.currentItem()
        if selected:
            result = install_plugin(selected.text())
            print("Plugin installation:", result)
