import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtOpenGL import QGLWidget
from OpenGL.GL import *
from stl import mesh
import numpy as np

class STLViewer(QGLWidget):
    def __init__(self, parent=None):
        super(STLViewer, self).__init__(parent)
        self.mesh = None
        self.angle = 0

    def load_stl(self, filename):
        self.mesh = mesh.Mesh.from_file(filename)
        self.update()

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glClearColor(0.1, 0.1, 0.1, 1)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, w / float(h), 1.0, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0, 0, -50)
        glRotatef(self.angle, 1, 1, 1)

        if self.mesh:
            glBegin(GL_TRIANGLES)
            for facet in self.mesh.vectors:
                for vertex in facet:
                    glVertex3f(*vertex)
            glEnd()

        self.angle += 1
        self.update()

class ViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GAIA STL Viewer")
        self.viewer = STLViewer()
        self.init_ui()

    def init_ui(self):
        open_btn = QPushButton("Open STL File")
        open_btn.clicked.connect(self.open_file)
        layout = QVBoxLayout()
        layout.addWidget(open_btn)
        layout.addWidget(self.viewer)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.resize(800, 600)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open STL File", "", "STL Files (*.stl)")
        if filename:
            self.viewer.load_stl(filename)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ViewerWindow()
    window.show()
    sys.exit(app.exec_())

