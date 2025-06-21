import time
from datetime import datetime
from collections import deque

class SessionWatcher:
    def __init__(self, max_history=100):
        self.session_data = deque(maxlen=max_history)
        self.active_session = None

    def start_session(self, game_name: str):
        self.active_session = {
            "game": game_name,
            "start_time": datetime.now().isoformat(),
            "events": [],
            "status": "active"
        }

    def log_event(self, event_type: str, data=None):
        if not self.active_session:
            return

        self.active_session["events"].append({
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "data": data or {}
        })

    def end_session(self):
        if not self.active_session:
            return

        self.active_session["end_time"] = datetime.now().isoformat()
        self.active_session["status"] = "completed"
        self.session_data.append(self.active_session)
        completed_session = self.active_session
        self.active_session = None
        return completed_session

    def recent_sessions(self, n=5):
        return list(self.session_data)[-n:]

    def get_last_summary(self):
        if not self.session_data:
            return "No session data available."
        last = self.session_data[-1]
        return {
            "game": last["game"],
            "start_time": last["start_time"],
            "end_time": last.get("end_time"),
            "events_logged": len(last["events"])
        }


# For dream_state_engine integration
def get_recent_session_data():
    try:
        from gaia.modules.casino.session_watcher import watcher_instance
        summary = watcher_instance.get_last_summary()
        return f"{summary['game']} ({summary['events_logged']} events)" if isinstance(summary, dict) else summary
    except Exception as e:
        return "Session parser error"

