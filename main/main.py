import sys
import traceback
from PyQt5.QtWidgets import QApplication
from gaia.gui.main_window import MainWindow
from gaia.core.plugin_registry import load_plugins, register_plugin_hook
from gaia.core.ai_expansion.scheduler import start_scheduler
from gaia.core.ai_expansion.init_auto_expansion_dirs import initialize_structure

# ✅ Firewall και Error Logger
from gaia.core.security.input_firewall import is_safe_input
from gaia.core.security.error_logger import log_error

def main():
    load_plugins()
    initialize_structure()
    start_scheduler()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_error(e, traceback.format_exc())  # ✅ Καταγραφή στο logs/security/errors.log
        raise
