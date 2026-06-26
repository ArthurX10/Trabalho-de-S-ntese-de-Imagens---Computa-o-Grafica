Tema 3: Simulação
i. Simule efeitos de iluminação com no mínimo duas fontes de luz em relação à
diferentes objetos em um plano (considere uma visualização em três dimensões)

Escolhido (ou validado) o projeto a ser implementado, faça:
a) Monte uma apresentação para contextualizar sua solução e explicar aos colegas de
classe o funcionamento da implementação (tente ser o mais didático possível);
b) Mostre a codificação (ao vivo) do tema escolhido (não seja detalhista durante a
apresentação, planeje bem o tempo);
c) Escreva um breve relatório contendo: Tema escolhido; Bibliotecas usadas (GLUT,
FreeGLUT, etc.); Principais desafios técnicos; Screenshots; Link do projeto no GitHub.




"""
Varios objetos, 2 Fontes de Luz. 

"""


#ILUMINAÇÃO PHONG


#Luz ambiente 
glEnable(GL_LIGHTING)
glEnable(GL_DEPTH_TEST)

glLightModelfv(GL_LIGHT_MODEL_AMBIENTE)

#Material

glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
glMaterialfv(GL_FRONT, GL_SPECULAR, color)
glMaterialfv(GL_FRONT, GL_AMBIENT, color)
glMaterialfv(GL_FRONT, GL_SHININESS, 0.5)

#Função que gera Luz    
def gerar_luz(light_id, posição - [x,y,z], intensidade):
    projeção da luz - glLight(light_id, GL_POSITION, position + [1])
    luz difusa      - glLight(light_id, GL_DIFFUSE, [COLOR[0] * intensity, color[1] * intensity, color[2] * intensity, 1])

    glLightfv(light_id, GL_CONTANT_ATTENUATION, 0)
    glLightfv(light_id, GL_LINEAR_ATTENUATION, 0.1)
    glLightfv(light_id, GL_QUADRATIC_ATTENUATION, 0.01 )

    glEnable(light_id)



#LUZ DIRECIONAL & SPOT
    DIRECIONAL = SOL
    (LIGHT_ID, DIRECTION, COLOR, INTENSITY)

    glLightfv(light_id,GL_POSITION, DIRECTION + [0])

    #configurar a intencidade
    glLightfv(light_id, GL_DIFFUSE, [COLOR[0] * INTENSITY, COLOR[1] * INTENSITY, COLOR[2] * INTENSITY_, 1])
    glLight(light_id, GL_SPECULAR, COLOR + [1])

    glLight(light_id, GL_CONSTANT_ATTENUATION, 1)
    glLight(light_id, GL_LINEAR_ATTENUATION, 0)
    glLight(light_id, GL_QUADRATIC_ATTENUATION, 0)

    glEnable(light_id)


#Luz spot - Luz da lanterna
    (light_id, position, color, intensity, cutoff, exponent):
        glLight(light_id, GL_POSIOTION, position + [1])

        glLight(light_id,GL_SPOT_DIRECTION, direction)

        glLight(light_id, GL_DIFFUSE, color[0] * intensity, color[1] * intensity, color[2] * intensity, 1 )

        glLight(light_id, GL_SPECULAR, COLOR* [1])

        glLightf(light_id, GL_SPOT_CUTOFF, cutoff)

        glLightf(light_id, GL_SPOT_EXPONENT, expanent)

        glLight(light_id, GL_CONSTANT_ATTENUATION, 1)
        glLight(light_id, GL_LINEAR_ATTENUATION, 0.1)
        glLight(light_id, GL_QUADRATIC_ATTENUATION, 0.01)

        glEnable(light_id)
