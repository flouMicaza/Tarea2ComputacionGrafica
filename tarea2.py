#la clase círculo contenida es esta tarea copiada de material docente.

import os
from CC3501Utils import *
from Personajes import *
from Plataformas import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla

def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "titulo")
    radio=100

    figuras = []
    #t = Triangulo(Vector(200, 200), Vector(600, 200), Vector(400, 500), (1, 0, 0))
    #figuras.append(t)

    f=Personaje(radio,Vector(250, 200),(255, 0, 0))
    hoja=plataforma_hoja(16)
    figuras.append(f)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pass

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers

        # dibujar figuras
        #for fig in figuras:
        f.dibujar()
        hoja.dibujar()


        #glBegin(GL_LINES)
        #glVertex2f(500, 500)
        #glVertex2f(500, 600)
        #glEnd()

        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

    pygame.quit()


main()
