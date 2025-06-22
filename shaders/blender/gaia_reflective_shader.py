import numpy as np
from gaia.core.voice_system import speak
from gaia.modules.emotion_feedback_loop import get_emotion_state


class ReflectiveShader:
    def __init__(self):
        self.surface_normal = np.array([0.0, 0.0, 1.0])
        self.camera_vector = np.array([0.0, 0.0, -1.0])
        self.emissive_intensity = 1.0
        self.reflectivity = 0.8

    def calculate_reflection(self, light_direction):
        # Normalize vectors
        light_dir = light_direction / np.linalg.norm(light_direction)
        normal = self.surface_normal / np.linalg.norm(self.surface_normal)
        reflection_vector = light_dir - 2 * np.dot(light_dir, normal) * normal
        return reflection_vector

    def update_material_state(self):
        emotion = get_emotion_state()
        if emotion == "stressed":
            self.reflectivity = 0.3
            self.emissive_intensity = 2.0
            speak("Reflective surface dimmed due to system stress.")
        elif emotion == "calm":
            self.reflectivity = 0.9
            self.emissive_intensity = 1.0
            speak("Reflective system balanced. Emotional state: calm.")
        elif emotion == "excited":
            self.reflectivity = 1.0
            self.emissive_intensity = 3.0
            speak("Reflective surface is glowing with excitement.")

    def render_frame(self, light_vector):
        reflection = self.calculate_reflection(light_vector)
        self.update_material_state()
        return {
            "reflection_vector": reflection.tolist(),
            "reflectivity": self.reflectivity,
            "emissive_intensity": self.emissive_intensity
        }

