from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Plano:

    def __init__(self):
        pass

    def draw(self):
        glEnable(GL_LIGHTING)

        glMaterialfv(GL_FRONT, GL_AMBIENT,   [0.30, 0.28, 0.25, 1.0])
        glMaterialfv(GL_FRONT, GL_DIFFUSE,   [0.78, 0.75, 0.70, 1.0])
        glMaterialfv(GL_FRONT, GL_SPECULAR,  [0.15, 0.15, 0.15, 1.0])
        glMaterialf (GL_FRONT, GL_SHININESS, 50.0)  

        glBegin(GL_QUADS)
        glNormal3f(0.0, 1.0, 0.0)
        glVertex3f(-5.0, 0.0, -5.0)
        glVertex3f( 5.0, 0.0, -5.0)
        glVertex3f( 5.0, 0.0,  5.0)
        glVertex3f(-5.0, 0.0,  5.0)
        glEnd()