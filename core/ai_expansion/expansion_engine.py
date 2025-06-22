
from .deficit_detector import detect_deficits

def run_expansion(trigger='manual'):
    deficits = detect_deficits()
    for d in deficits:
        print(f"[GAIA AI Expansion] Generating module for: {d} (trigger: {trigger})")
        # Placeholder: Actual module generation logic would go here
