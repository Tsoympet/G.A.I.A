import threading
import time

class SyncEngine:
    def __init__(self, node_id, peer_manager, memory_store, secure_channel):
        self.node_id = node_id
        self.peer_manager = peer_manager
        self.memory_store = memory_store
        self.secure_channel = secure_channel
        self.sync_interval = 60  # seconds
        self.active = False

    def start(self):
        self.active = True
        self.thread = threading.Thread(target=self._run_sync_loop)
        self.thread.start()

    def stop(self):
        self.active = False
        if hasattr(self, 'thread'):
            self.thread.join()

    def _run_sync_loop(self):
        while self.active:
            self.sync_with_peers()
            time.sleep(self.sync_interval)

    def sync_with_peers(self):
        peers = self.peer_manager.get_active_peers()
        for peer in peers:
            try:
                delta = self.memory_store.get_recent_changes()
                payload = self.secure_channel.encrypt(delta, peer.public_key)
                response = self.secure_channel.send(peer.address, payload)
                if response:
                    updates = self.secure_channel.decrypt(response, peer.public_key)
                    self.memory_store.apply_updates(updates)
            except Exception as e:
                print(f"[SyncEngine] Failed to sync with {peer.address}: {str(e)}")

