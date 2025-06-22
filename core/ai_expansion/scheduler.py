
import time
import threading
from .expansion_engine import run_expansion

def start_scheduler():
    def periodic():
        while True:
            run_expansion(trigger='time')
            time.sleep(86400)  # Every 24 hours
    t = threading.Thread(target=periodic, daemon=True)
    t.start()
