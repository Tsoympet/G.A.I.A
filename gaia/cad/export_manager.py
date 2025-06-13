import os
import json
import shutil
from datetime import datetime

class ExportManager:
    def __init__(self, export_dir='exports'):
        self.export_dir = export_dir
        os.makedirs(self.export_dir, exist_ok=True)

    def export_logs(self, log_data, filename='gaia_log.json'):
        path = os.path.join(self.export_dir, filename)
        with open(path, 'w') as f:
            json.dump(log_data, f, indent=2)
        return path

    def export_memory_snapshot(self, memory_data, filename='memory_snapshot.json'):
        path = os.path.join(self.export_dir, filename)
        with open(path, 'w') as f:
            json.dump(memory_data, f, indent=2)
        return path

    def backup_project(self, source_dir='GAIA', backup_name=None):
        if not backup_name:
            backup_name = f'GAIA_Backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
        backup_path = os.path.join(self.export_dir, backup_name)
        shutil.make_archive(backup_path, 'zip', source_dir)
        return backup_path + '.zip'

    def list_exports(self):
        return os.listdir(self.export_dir)

