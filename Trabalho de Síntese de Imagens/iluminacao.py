from OpenGL.GL import *
from OpenGL.GLUT import *

LIGHT0_POS = [3.0, 5.0, 3.0]
LIGHT1_POS = [-4.0, 3.0, -2.0]

# Variáveis globais para controlar o estado das luzes
light0_active = True
light1_active = True

def init_lights():
    glEnable(GL_LIGHTING)

    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    glEnable(GL_NORMALIZE)
    glShadeModel(GL_SMOOTH)

    glLightModelfv(
        GL_LIGHT_MODEL_AMBIENT,
        [0.15, 0.15, 0.15, 1.0]
    )

    #Luz branca
    glLightfv(GL_LIGHT0, GL_AMBIENT,
              [0.3, 0.3, 0.3, 1.0])

    glLightfv(GL_LIGHT0, GL_DIFFUSE,
              [1.0, 1.0, 1.0, 1.0])

    glLightfv(GL_LIGHT0, GL_SPECULAR,
              [1.0, 1.0, 1.0, 1.0])

    #Luz Azul 
    glLightfv(GL_LIGHT1, GL_AMBIENT, 
              [0.05, 0.05, 0.15, 1.0])

    glLightfv(GL_LIGHT1, GL_DIFFUSE,
              [0.2, 0.2, 1.0, 1.0])

    glLightfv(GL_LIGHT1, GL_SPECULAR,
              [0.4, 0.4, 1.0, 1.0])

    # Material
    glMaterialfv(
        GL_FRONT_AND_BACK,
        GL_SPECULAR,
        [1.0, 1.0, 1.0, 1.0]
    )

    glMaterialf(
        GL_FRONT_AND_BACK,
        GL_SHININESS,
        64.0
    )

def draw_light_markers():

    # As esferas não devem receber iluminação
    glDisable(GL_LIGHTING)

    # =====================
    # Luz 0 (branca)
    # =====================
    glColor3f(1.0, 1.0, 1.0)

    glPushMatrix()
    glTranslatef(*LIGHT0_POS)
    glutSolidSphere(0.15, 16, 16)
    glPopMatrix()

    # =====================
    # Luz 1 (azul)
    # =====================
    glColor3f(0.3, 0.3, 1.0)

    glPushMatrix()
    glTranslatef(*LIGHT1_POS)
    glutSolidSphere(0.15, 16, 16)
    glPopMatrix()

    glEnable(GL_LIGHTING)


def update_light_positions():
    global light0_active, light1_active
    
    # Luz principal (Luz 0)
    if light0_active:
        glEnable(GL_LIGHT0)
        glLightfv(
            GL_LIGHT0,
            GL_POSITION,
            [*LIGHT0_POS, 1.0]
        )
    else:
        glDisable(GL_LIGHT0)

    # Luz secundária (Luz 1)
    if light1_active:
        glEnable(GL_LIGHT1)
        glLightfv(
            GL_LIGHT1,
            GL_POSITION,
            [*LIGHT1_POS, 1.0]
        ) 
    else:
        glDisable(GL_LIGHT1)

def enable_light(light_id):
    global light0_active, light1_active

    if light_id == 0:
        light0_active = not light0_active
    elif light_id == 1:
        light1_active = not light1_active
