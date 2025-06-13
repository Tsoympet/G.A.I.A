from gaia.gui.dashboard import launch_dashboard
from gaia.core.intelligence_engine import GAIAIntelligenceCore
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.dream_state_engine import DreamEngine
from gaia.core.self_repair import SelfRepairSystem

if __name__ == "__main__":
    print("[GAIA] Initializing subsystems...")
    emotion = EmotionEngine()
    dreams = DreamEngine()
    repair = SelfRepairSystem()
    core = GAIAIntelligenceCore(emotion_engine=emotion, dream_engine=dreams, repair_engine=repair)

    print("[GAIA] Core ready. Launching dashboard...")
    launch_dashboard(core)

