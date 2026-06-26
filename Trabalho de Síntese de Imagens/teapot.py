from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Teapot:

    def __init__(self, size=0.8, color=None, initial_position=[2, 1, 0.0]):
        self.size     = size
        self.color    = color if color is not None else [0.7, 0.7, 0.7, 1.0]
        self.position = initial_position

    def draw(self, x=0.0, y=0.0, z=0.0):
        glMaterialfv(GL_FRONT, GL_AMBIENT,   self.color)
        glMaterialfv(GL_FRONT, GL_DIFFUSE,   self.color)
        glMaterialfv(GL_FRONT, GL_SPECULAR,  [1.0, 1.0, 1.0, 1.0])
        glMaterialf (GL_FRONT, GL_SHININESS, 120.0)

        glPushMatrix()
        glTranslatef(
            self.position[0] + x,
            self.position[1] + y,
            self.position[2] + z,
        )
        glutSolidTeapot(self.size)
        glPopMatrix()