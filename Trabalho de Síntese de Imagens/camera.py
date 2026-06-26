from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


class Camera:
    def __init__(self, width, height):
        self.camera_pos   = np.array([0.0, 2.0, 8.0])
        self.camera_front = np.array([0.0, 0.0, -1.0])
        self.camera_up    = np.array([0.0, 1.0,  0.0])
        self.yaw, self.pitch = -90.0, 0.0

        self.camera_speed = 0.3
        self.sensitivity  = 0.2

        self.last_x, self.last_y = width / 2, height / 2
        self.mouse_down  = False
        self.first_mouse = True

    def apply(self):
        glLoadIdentity()
        target = self.camera_pos + self.camera_front
        gluLookAt(
            self.camera_pos[0], self.camera_pos[1], self.camera_pos[2],
            target[0],          target[1],          target[2],
            self.camera_up[0],  self.camera_up[1],  self.camera_up[2],
        )

    def move(self, direction):
        right = np.cross(self.camera_front, self.camera_up)
        right = right / np.linalg.norm(right)
        
        if direction == "FRENTE":
            self.camera_pos += self.camera_speed * self.camera_front
        elif direction == "TRAS":
            self.camera_pos -= self.camera_speed * self.camera_front
        elif direction == "ESQUERDA":
            self.camera_pos -= self.camera_speed * right
        elif direction == "DIREITA":
            self.camera_pos += self.camera_speed * right
        elif direction == "CIMA":
            self.camera_pos[1] += self.camera_speed
        elif direction == "BAIXO":
            self.camera_pos[1] -= self.camera_speed
        
        glutPostRedisplay()
        
    def mouse(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON:
            self.mouse_down  = (state == GLUT_DOWN)
            self.first_mouse = True   

        if button == 3: self.camera_pos += self.camera_speed * self.camera_front
        if button == 4: self.camera_pos -= self.camera_speed * self.camera_front

        glutPostRedisplay()

    def motion(self, x, y):
        if not self.mouse_down:
            return

        if self.first_mouse:
            self.last_x, self.last_y = x, y
            self.first_mouse = False
            return

        xoffset = (x - self.last_x) * self.sensitivity
        yoffset = (self.last_y - y) * self.sensitivity
        self.last_x, self.last_y = x, y

        self.yaw   += xoffset
        self.pitch += yoffset
        self.pitch  = max(-89.0, min(89.0, self.pitch))

        direction = np.array([
            np.cos(np.radians(self.yaw)) * np.cos(np.radians(self.pitch)),
            np.sin(np.radians(self.pitch)),
            np.sin(np.radians(self.yaw)) * np.cos(np.radians(self.pitch)),
        ])
        self.camera_front = direction / np.linalg.norm(direction)

        glutPostRedisplay()
