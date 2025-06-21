#!/bin/bash

# GAIA Installer Build Script

echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing requirements..."
pip install -r requirements.txt

echo "Launching GAIA main interface..."
python main.py
