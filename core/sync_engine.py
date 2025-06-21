import os
import json
import time
import hashlib
from gaia.core.memory_manager import MemoryManager

class SyncEngine:
    def __init__(self, memory_manager: MemoryManager, sync_dir="gaia_sync"):
        self.memory_manager = memory_manager
        self.sync_dir = sync_dir
        self.last_sync_hash = None
        if not os.path.exists(self.sync_dir):
            os.makedirs(self.sync_dir)

    def _calculate_hash(self, data):
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def export_memory_snapshot(self):
        data = self.memory_manager.export_all()
        hash_digest = self._calculate_hash(data)
        snapshot_file = os.path.join(self.sync_dir, f"memory_snapshot_{int(time.time())}.json")
        with open(snapshot_file, "w") as f:
            json.dump({"hash": hash_digest, "data": data}, f, indent=2)
        self.last_sync_hash = hash_digest
        return snapshot_file

    def import_memory_snapshot(self, snapshot_path):
        if not os.path.exists(snapshot_path):
            raise FileNotFoundError("Snapshot file not found.")
        with open(snapshot_path, "r") as f:
            content = json.load(f)
        hash_check = self._calculate_hash(content["data"])
        if hash_check != content["hash"]:
            raise ValueError("Memory snapshot integrity check failed.")
        self.memory_manager.import_all(content["data"])
        self.last_sync_hash = hash_check
        return True

    def synchronize(self):
        snapshots = sorted(Path(self.sync_dir).glob("memory_snapshot_*.json"), reverse=True)
        if not snapshots:
            return "No snapshot available to sync."
        latest_snapshot = snapshots[0]
        return self.import_memory_snapshot(latest_snapshot)

    def sync_status(self):
        return {
            "last_sync_hash": self.last_sync_hash,
            "sync_dir": self.sync_dir,
            "snapshots_available": len(list(Path(self.sync_dir).glob("memory_snapshot_*.json")))
        }

