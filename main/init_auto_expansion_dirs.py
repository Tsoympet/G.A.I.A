import os

# Βάση path για τοποθέτηση μέσα στο G.A.I.A/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Λίστα directories και default αρχείων
required_dirs = {
    "modules/auto_expanded": ".keep",
    "auto_assets": ".keep",
    "dream_logs": ".keep",
    "voice/auto": ".keep",
    "render/auto": ".keep",
    "test/auto": ".keep",
    "cad/auto_blueprints": ".keep",
    "shaders/unreal/auto": ".keep",
    "logs": "expansion_log.txt"
}

def initialize_structure():
    for rel_path, default_file in required_dirs.items():
        abs_dir = os.path.join(BASE_DIR, rel_path)
        os.makedirs(abs_dir, exist_ok=True)
        file_path = os.path.join(abs_dir, default_file)
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                if "log" in default_file:
                    f.write("AI Expansion Log Initialized.\n")
                else:
                    f.write("")  # empty .keep

    print("✅ All auto-expansion directories initialized.")

if __name__ == "__main__":
    initialize_structure()
