# π“¦ GAIA β€“ Installation Guide

This document outlines the setup and installation instructions for running **GAIA** on both **desktop (Windows/Linux/macOS)** and **mobile (Android)** platforms.

---

## π–¥οΈ Desktop Installation (Windows/Linux/macOS)

### π”§ Requirements
- Python 3.10+
- Node.js (for Electron animation)
- pip (Python package manager)
- Git

### π“¥ 1. Clone the Repository
```bash
git clone https://github.com/Tsoympet/G.A.I.A.git
cd G.A.I.A
```

### π“¦ 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### β™οΈ 3. Run the GAIA System
```bash
python main.py
```

---

## π  Optional: Run Electron Startup Animation
```bash
cd startup_animation
npm install
npm start
```

---

## π“¦ Create Windows Executable (Installer)

### π”§ Using `PyInstaller`
```bash
pyinstaller --noconfirm --windowed --icon=gaia/assets/logo/gaia-logo.ico main.py
```

> Installer script and launcher are preconfigured in `installer.py` and `launcher.py`.

---

## π“± Android Installation (GAIA Mobile Companion)

### β… Prerequisites
- Android 8.0+
- Unknown sources enabled in system settings

### π“² Installation Steps
1. Download the APK:
   ```
   GAIA_Android_App.apk
   ```
2. Transfer to your device or download directly from your GitHub release page.
3. Tap to install and accept permissions.

---

## βοΈ Activation & Licensing

### 1. Launch GAIA
### 2. Youβ€™ll be prompted to **Register and Activate**:
- Register email via the web portal.
- Enter the activation key sent to your email.
- Activation is handled via the GAIA license server.

> License portal is located at: `https://gaia-activation.tld` (or your hosted endpoint)

---

## π› οΈ Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Recheck `requirements.txt` install |
| GUI does not launch | Ensure PyQt5 is properly installed |
| No startup animation | Check if Electron is installed and run manually |
| Activation fails | Verify internet access + correct email input |
