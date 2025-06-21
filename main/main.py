import sys
from PyQt5.QtWidgets import QApplication
from gaia.gui.main_window import MainWindow
from gaia.core.plugin_registry import load_plugins, register_plugin_hook

def main():
    load_plugins()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
