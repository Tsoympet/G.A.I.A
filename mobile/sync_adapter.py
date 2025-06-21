import json
import os
from gaia.core.sync_engine import SyncEngine

class SyncAdapter:
    def __init__(self, sync_dir='sync_data'):
        self.sync_dir = sync_dir
        self.engine = SyncEngine()
        if not os.path.exists(sync_dir):
            os.makedirs(sync_dir)

    def save_to_disk(self, data, filename='sync_snapshot.json'):
        path = os.path.join(self.sync_dir, filename)
        with open(path, 'w') as f:
            json.dump(data, f)
        print(f"[SyncAdapter] Saved snapshot to {path}")
        return path

    def load_from_disk(self, filename='sync_snapshot.json'):
        path = os.path.join(self.sync_dir, filename)
        if not os.path.exists(path):
            print("[SyncAdapter] No sync file found.")
            return None
        with open(path, 'r') as f:
            data = json.load(f)
        print(f"[SyncAdapter] Loaded snapshot from {path}")
        return data

    def sync_with_cloud(self):
        snapshot = self.engine.create_snapshot()
        return self.save_to_disk(snapshot)

    def restore_from_cloud(self, path='sync_snapshot.json'):
        data = self.load_from_disk(path)
        if data:
            return self.engine.restore_snapshot(data)
        return False
