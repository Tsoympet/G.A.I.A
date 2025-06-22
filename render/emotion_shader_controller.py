import bpy

def update_emotion_material(emotion_value: float):
    mat = bpy.data.materials.get("GAIA_Emotion_Material")
    if mat and mat.use_nodes:
        for node in mat.node_tree.nodes:
            if node.type == 'VALUE':
                node.outputs[0].default_value = emotion_value
                print(f"Emotion value set to: {emotion_value}")
                break
