#la clase círculo contenida es esta tarea copiada de material docente.

import os
from CC3501Utils import *
from Personajes import *
from Plataformas import *
from Paredes import *
os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


def creacionPared():
    flores = []
    y= 20;
    deltay=80;
    while y<600:
        #florIzq
        f1 = florFigura((150, 150, 0), Vector(20, y))
        flores.append(f1)
        #florDer
        f1 = florFigura((150, 150, 0), Vector(800-80, y))
        flores.append(f1)
        y += deltay
        f2 = florFigura((255, 0, 255), Vector(800-80, y), (0, 255, 128))
        flores.append(f2)
        f2 = florFigura((255, 0, 255), Vector(20, y), (0, 255, 128))
        flores.append(f2)
        y += deltay
    return flores

def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "titulo")
    radio=50 #tamaño minimo de 50!

    florss=creacionPared()

    figuras = []
    flor=plataforma_flor(radio,(150,150,0))
    rama=plataforma_rama(500,Vector(80,10))
    hoja=plataforma_hoja(50,Vector(350,350))
    f = Personaje(radio, Vector(300, 80), (255, 0, 0))


    figuras.append(rama)
    figuras.append(f)

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


        #dibujar la pared primero
        for flor in florss:
            flor.dibujar()


        # dibujar figuras
        for fig in figuras:
            fig.dibujar()

        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

    pygame.quit()


main()
