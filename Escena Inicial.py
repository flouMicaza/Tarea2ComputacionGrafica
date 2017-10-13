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
        f1 = florFigura((150, 150, 0), Vector(750, y))
        flores.append(f1)
        y += deltay
        f2 = florFigura((255, 0, 255), Vector(750, y), (0, 255, 128))
        flores.append(f2)
        f2 = florFigura((255, 0, 255), Vector(20, y), (0, 255, 128))
        flores.append(f2)
        y += deltay
    return flores

def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "titulo")
    radio=30 #tamaño minimo de 50!
    radio_china=50
    florss=creacionPared()

    figuras = []
    flor=plataforma_flor(radio,(150,150,0),Vector(100,500))
    flor2 = plataforma_flor(radio, (196/255, 97/255, 140/255),Vector(350,200))
    rama=plataforma_rama(500,Vector(80,10))
    rama2 = plataforma_rama(radio*4, Vector(400, 100))
    hoja=plataforma_hoja(50,Vector(550,350))
    hoja1 = plataforma_hoja(50, Vector(200, 450))
    f = Personaje(radio_china, Vector(300, 80), (255, 0, 0))



    figuras.append(hoja)
    figuras.append(rama)
    figuras.append(hoja1)
    figuras.append(flor2)
    figuras.append(rama2)
    figuras.append(f)
    figuras.append(flor)


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
