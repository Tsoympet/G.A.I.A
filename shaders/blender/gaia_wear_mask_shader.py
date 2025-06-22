import numpy as np
from gaia.core.voice_system import speak
from gaia.modules.emotion_feedback_loop import get_emotion_state

class WearableShader:
    def __init__(self):
        self.transparency = 0.0  # 0 = solid, 1 = fully invisible
        self.pulse_intensity = 1.0
        self.active_camo = False
        self.color_state = (255, 255, 255)  # RGB default white

    def activate_stealth(self, enable: bool):
        self.active_camo = enable
        if enable:
            self.transparency = 0.8
            self.pulse_intensity = 0.3
            speak("Stealth mode activated. Mask opacity increased.")
        else:
            self.transparency = 0.0
            self.pulse_intensity = 1.0
            speak("Stealth mode deactivated. Mask visibility restored.")

    def update_by_emotion(self):
        emotion = get_emotion_state()
        if emotion == "anxious":
            self.color_state = (200, 50, 50)  # reddish
            self.pulse_intensity = 1.5
            speak("Mask adapting to high stress levels.")
        elif emotion == "neutral":
            self.color_state = (255, 255, 255)
            self.pulse_intensity = 1.0
        elif emotion == "focused":
            self.color_state = (100, 100, 255)
            self.pulse_intensity = 0.8
            speak("Mask optimized for concentration.")

    def render_mask_frame(self):
        self.update_by_emotion()
        return {
            "transparency": self.transparency,
            "pulse_intensity": self.pulse_intensity,
            "active_camo": self.active_camo,
            "color": self.color_state
        }

