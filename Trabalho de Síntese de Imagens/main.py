import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import iluminacao
import cubo as cubo_mod
import teapot as teapot_mod
import sphere as sphere_mod
import plano as plano_mod
from camera import Camera

WIDTH, HEIGHT = 800, 600

plano_obj  = plano_mod.Plano()
cubo_obj   = cubo_mod.Cubo()
teapot_obj = teapot_mod.Teapot()
sphere_obj = sphere_mod.Sphere(0.5, 32, 32, initial_position=[-2.0, 1.0, 0.0])
camera     = Camera(WIDTH, HEIGHT)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    iluminacao.init_lights()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera.apply()
    
    iluminacao.update_light_positions()

    plano_obj.draw()
    cubo_obj.draw()
    sphere_obj.draw()
    teapot_obj.draw()

    iluminacao.draw_light_markers()

    glutSwapBuffers()

def keyboard(key, x, y):
    if isinstance(key, bytes):
        key = key.decode("utf-8")

    if key == 'w':
        camera.move("FRENTE")
    elif key == 's':
        camera.move("TRAS")
    elif key == 'a':
        camera.move("ESQUERDA")
    elif key == 'd':
        camera.move("DIREITA")
    elif key == 'q':
        camera.move("CIMA")
    elif key == 'e':
        camera.move("BAIXO")

    elif key == '1':
        iluminacao.enable_light(0)
    elif key == '2':
        iluminacao.enable_light(1)


    elif key == '\x1b':
        sys.exit(0)

    glutPostRedisplay()

def reshape(w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, w / h, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow(b"Sintese de Imagens")

init()

glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMouseFunc(camera.mouse)
glutMotionFunc(camera.motion)
glutMainLoop()


