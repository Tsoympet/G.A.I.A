import sys
from PyQt5.QtWidgets import QApplication
from gaia.gui.main_window import MainWindow
from gaia.core.plugin_registry import load_plugins, register_plugin_hook
from gaia.core.ai_expansion.scheduler import start_scheduler
from gaia.core.ai_expansion.init_auto_expansion_dirs import initialize_structure  # ✅ ΝΕΟ

def main():
    load_plugins()
    initialize_structure()  # ✅ Δημιουργία φακέλων επέκτασης
    start_scheduler()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
