import json
import time
import threading
from gaia.core.sync_engine import SyncEngine

class SyncAdapter:
    def __init__(self, local_id, peer_list, memory_manager):
        self.local_id = local_id
        self.peer_list = peer_list
        self.memory_manager = memory_manager
        self.sync_engine = SyncEngine(self.local_id, self.peer_list)
        self.sync_thread = threading.Thread(target=self.run_sync, daemon=True)
        self.running = False

    def start(self):
        self.running = True
        self.sync_thread.start()

    def stop(self):
        self.running = False
        self.sync_thread.join()

    def run_sync(self):
        while self.running:
            local_snapshot = self.memory_manager.export_memory_snapshot()
            for peer in self.peer_list:
                self.sync_engine.send_update(peer, local_snapshot)
                remote_data = self.sync_engine.receive_update(peer)
                if remote_data:
                    self.memory_manager.integrate_remote_snapshot(remote_data)
            time.sleep(10)

    def add_peer(self, peer):
        if peer not in self.peer_list:
            self.peer_list.append(peer)
            self.sync_engine.update_peers(self.peer_list)

    def remove_peer(self, peer):
        if peer in self.peer_list:
            self.peer_list.remove(peer)
            self.sync_engine.update_peers(self.peer_list)

