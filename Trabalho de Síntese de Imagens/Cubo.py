from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def cubo():
    vertices = [
        [0.5, 0.5, 0.5],
        [0.5, 0.5, -0.5],
        [0.5, -0.5, 0.5],
        [0.5, -0.5, -0.5],
        [-0.5, 0.5, 0.5],
        [-0.5, 0.5, -0.5],
        [-0.5, -0.5, 0.5],
        [-0.5, -0.5, -0.5]
    ]

    faces = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 4, 5, 1],
        [2, 6, 7, 3],
        [0, 2, 6, 4],
        [1, 3, 7, 5]
    ]

    glBegin(GL_QUADS)
    glColor3fv([1 ,0 ,0])
    for i, face in enumerate(faces):
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def init():
    glClearColor(0.0, 0.2, 0.5, 1.0)
    glEnable(GL_DEPTH_TEST)

    # Configura a projeção perspectiva
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 100)

    # Configura a câmera
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2, 2, 2,   # posição da câmera
              0, 0, 0,   # ponto que a câmera olha
              0, 1, 0)   # vetor "up"


angle = 1

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global angle

    # Reseta a matriz e reposiciona a câmera a cada frame
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2, 2, 2,
              0, 0, 0,
              0, 1, 0)

    # Aplica a rotação
    glRotatef(angle, 1, 1, 1)
    angle += 0.03

    cubo()
    glutSwapBuffers()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Cubo 3D")
init()
glutDisplayFunc(display)
glutIdleFunc(display) 
#glutKeyboardFunc(pegar_tecla)
glutMainLoop()