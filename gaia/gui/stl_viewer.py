from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

class STLViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STL Viewer")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Load and view .STL files")
        self.load_button = QPushButton("Open STL File")
        self.load_button.clicked.connect(self.open_stl)

        layout.addWidget(self.label)
        layout.addWidget(self.load_button)
        self.setLayout(layout)

    def open_stl(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open STL File", "", "STL Files (*.stl)")
        if filename:
            self.display_stl(filename)

    def display_stl(self, filepath):
        figure = plt.figure()
        axes = mplot3d.Axes3D(figure)
        your_mesh = mesh.Mesh.from_file(filepath)
        axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

        scale = your_mesh.points.flatten()
        axes.auto_scale_xyz(scale, scale, scale)
        plt.title("STL File Preview")
        plt.show()
