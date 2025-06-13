# GAIA Installation Guide

This guide will help you install and run GAIA, the advanced self-evolving AI platform.

---

## Prerequisites

- Python 3.8 or later
- Node.js (for Electron-based startup animation)
- Git (for cloning repository)
- pip (Python package manager)

---

## 1. Clone the Repository

```
git clone https://github.com/yourusername/GAIA.git
cd GAIA
```

---

## 2. Python Dependencies

Create a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install required packages:

```
pip install -r requirements.txt
```

---

## 3. Electron Setup (for Startup Animation)

Navigate to the Electron folder and install dependencies:

```
cd startup_animation
npm install
cd ..
```

To preview the startup animation:

```
npm start --prefix startup_animation
```

---

## 4. Launch GAIA

To run the main GAIA application:

```
python main.py
```

---

## 5. Build Executable (.exe)

Install pyinstaller if not already installed:

```
pip install pyinstaller
```

Build executable (with GUI assets and Electron if needed):

```
pyinstaller --noconfirm --onefile --windowed main.py
```

---

## 6. Troubleshooting

- Ensure all assets (images, voices, icons) are correctly placed in `/gaia/assets/`.
- For GUI issues, verify PyQt5 installation.
- Check logs or terminal output for specific errors.

---

## 7. Credits

GAIA: Gamblers Artificial Intelligent Assistant
