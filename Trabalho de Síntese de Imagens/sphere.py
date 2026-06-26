from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


class Sphere:

    def __init__(self, radius, slices, stacks, color=None, initial_position=[-2, 0.5, 0.0]):
        self.radius   = radius
        self.slices   = slices
        self.stacks   = stacks
        self.color    = color if color is not None else [0.6, 0.2, 0.8, 1.0]
        self.position = initial_position

    def draw(self, x=0.0, y=0.0, z=0.0):
        glMaterialfv(GL_FRONT, GL_AMBIENT,   self.color)
        glMaterialfv(GL_FRONT, GL_DIFFUSE,   self.color)
        glMaterialfv(GL_FRONT, GL_SPECULAR,  [1.0, 1.0, 1.0, 1.0])
        glMaterialf (GL_FRONT, GL_SHININESS, 100.0)

        glPushMatrix()
        glTranslatef(
            self.position[0] + x,
            self.position[1] + y,
            self.position[2] + z,
        )
        glRotatef(90, 1, 0, 0)

        for i in range(self.stacks):
            lat0 = np.pi * (-0.5 + float(i)     / self.stacks)
            z0   = self.radius * np.sin(lat0)
            zr0  = self.radius * np.cos(lat0)

            lat1 = np.pi * (-0.5 + float(i + 1) / self.stacks)
            z1   = self.radius * np.sin(lat1)
            zr1  = self.radius * np.cos(lat1)

            glBegin(GL_QUAD_STRIP)
            for j in range(self.slices + 1):
                lng = 2 * np.pi * float(j) / self.slices
                x_  = np.cos(lng)
                y_  = np.sin(lng)

                glNormal3f(x_ * zr0 / self.radius, y_ * zr0 / self.radius, z0 / self.radius)
                glVertex3f(x_ * zr0, y_ * zr0, z0)

                glNormal3f(x_ * zr1 / self.radius, y_ * zr1 / self.radius, z1 / self.radius)
                glVertex3f(x_ * zr1, y_ * zr1, z1)
            glEnd()

        glPopMatrix()