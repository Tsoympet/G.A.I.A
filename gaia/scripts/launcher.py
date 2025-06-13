import os
import sys
import subprocess

def launch_gaia():
    base_path = Path(__file__).resolve().parent
    gaia_main = base_path / 'main.py'
    if not gaia_main.exists():
        print("Error: main.py not found in the expected location.")
        return
    try:
        subprocess.run([sys.executable, str(gaia_main)], check=True)
    except Exception as e:
        print(f"Failed to launch GAIA: {e}")

if __name__ == "__main__":
    launch_gaia()


