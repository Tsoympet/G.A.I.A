import json
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.intelligence_engine import KnowledgeBase
from gaia.core.plugin_registry import trigger_plugin_event
from gaia.modules.sync_engine import SyncEngine
from gaia.core.memory_manager import MemoryManager

class MobileBridge:
    def __init__(self):
        self.emotion_engine = EmotionEngine()
        self.knowledge_base = KnowledgeBase()
        self.sync_engine = SyncEngine()
        self.memory_manager = MemoryManager()

    def handle_message(self, message_json):
        try:
            message = json.loads(message_json)
            action = message.get("action")
            data = message.get("data")

            if action == "get_emotion":
                return self._respond_emotion()
            elif action == "get_knowledge":
                return self._respond_knowledge()
            elif action == "trigger_plugin":
                return self._trigger_plugin(data)
            elif action == "save_memory":
                return self._save_memory(data)
            elif action == "sync_now":
                return self._sync()
            else:
                return self._error("Unknown action.")
        except Exception as e:
            return self._error(f"Exception: {str(e)}")

    def _respond_emotion(self):
        mood = self.emotion_engine.current_mood()
        return json.dumps({"status": "ok", "emotion": mood})

    def _respond_knowledge(self):
        topic = self.knowledge_base.random_topic()
        return json.dumps({"status": "ok", "topic": topic})

    def _trigger_plugin(self, data):
        event = data.get("event")
        payload = data.get("payload", {})
        trigger_plugin_event(event, payload)
        return json.dumps({"status": "ok", "triggered": event})

    def _save_memory(self, data):
        self.memory_manager.save_mobile_event(data)
        return json.dumps({"status": "ok", "saved": True})

    def _sync(self):
        result = self.sync_engine.sync_all()
        return json.dumps({"status": "ok", "sync_result": result})

    def _error(self, message):
        return json.dumps({"status": "error", "message": message})
