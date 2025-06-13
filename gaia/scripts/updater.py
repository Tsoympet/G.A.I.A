import os
import shutil
import requests
import zipfile
from datetime import datetime

class GaiaUpdater:
    def __init__(self, update_url, backup_dir='backups'):
        self.update_url = update_url
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(exist_ok=True)

    def backup_current_version(self, target_dir='GAIA'):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = self.backup_dir / f'backup_{timestamp}.zip'
        shutil.make_archive(str(backup_path).replace('.zip', ''), 'zip', target_dir)
        print(f"Backup created at {backup_path}")
        return backup_path

    def download_update(self, output_path='update_package.zip'):
        response = requests.get(self.update_url, stream=True)
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
        print("Update package downloaded.")
        return output_path

    def apply_update(self, package_path='update_package.zip', target_dir='GAIA'):
        with zipfile.ZipFile(package_path, 'r') as zip_ref:
            zip_ref.extractall(target_dir)
        print("Update applied successfully.")

if __name__ == "__main__":
    updater = GaiaUpdater("https://your-update-server.com/GAIA-latest.zip")
    updater.backup_current_version()
    zip_path = updater.download_update()
    updater.apply_update(zip_path)

