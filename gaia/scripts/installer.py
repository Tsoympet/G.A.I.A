import os
import shutil
import zipfile
import subprocess

def create_exe_installer(source_dir, output_dir, icon_path=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Step 1: Zip the entire GAIA folder
    zip_path = os.path.join(output_dir, 'GAIA_Package.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, start=source_dir)
                zipf.write(filepath, arcname)

    # Step 2: Build executable using PyInstaller
    command = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        f'--name=GAIA',
        f'--distpath={output_dir}',
        os.path.join(source_dir, 'main.py')
    ]
    if icon_path:
        command.insert(3, f'--icon={icon_path}')

    subprocess.run(command)

    print("Installer package created successfully.")

if __name__ == "__main__":
    create_exe_installer(source_dir='GAIA', output_dir='dist', icon_path='GAIA/assets/logo/gaia-logo.ico')

