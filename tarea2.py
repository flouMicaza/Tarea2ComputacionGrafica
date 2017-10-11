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
    radio=50 #tamaño minimo de 50!



    figuras = []
    #t = Triangulo(Vector(200, 200), Vector(600, 200), Vector(400, 500), (1, 0, 0))
    #figuras.append(t)

    flor=plataforma_flor(radio,(150,150,0))
    rama=plataforma_rama(200,Vector(200,200))
    hoja=plataforma_hoja(50,Vector(350,350))
    f = Personaje(radio, Vector(150, 150), (255, 0, 0))
    figuras.append(f)
    figuras.append(hoja)
    figuras.append(flor)
    figuras.append(rama)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pass

                if event.key == K_d:
                    f.pos += Vector(10, 0)
                if event.key == K_a:
                    f.pos -= Vector(10, 0)
                if event.key == K_w:
                    f.pos += Vector(0, 10)
                if event.key == K_s:
                    f.pos -= Vector(0, 10)


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers

        # dibujar figuras
        for fig in figuras:
            fig.dibujar()

        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

    pygame.quit()


main()
