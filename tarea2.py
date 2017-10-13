# la clase círculo contenida es esta tarea copiada de material docente.

import os
from CC3501Utils import *
from Personajes import *
from Plataformas import *
from Paredes import *
from random import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


def creacionPared():
    flores = []
    y = 20;
    deltay = 80;
    while y < 600:
        # florIzq
        f1 = florFigura((150, 150, 0), Vector(20, y))
        flores.append(f1)
        # florDer
        f1 = florFigura((150, 150, 0), Vector(750, y))
        flores.append(f1)
        y += deltay
        f2 = florFigura((255, 0, 255), Vector(750, y), (0, 255, 128))
        flores.append(f2)
        f2 = florFigura((255, 0, 255), Vector(20, y), (0, 255, 128))
        flores.append(f2)
        y += deltay
    return flores


def generadorPlataformas():
    medidas = []
    medidas.append(48)
    medidas.append(53)
    medidas.append(50)
    medidas.append(45)
    medidas.append(40)
    vel = Vector(uniform(-30, 30), 0.0)
    a = randint(1, 3)
    b = randint(1, 4)
    x = randint(100, 550)
    if a == 1:
        return plataforma_flor(medidas[b], (150, 150, 0), Vector(x, 500), (1, 51 / 255, 1), vel)
    elif b == 2:
        return plataforma_rama(medidas[b] * 4, Vector(x, 500), (115 / 255, 12 / 255, 12 / 255), vel)
    else:
        return plataforma_hoja(medidas[b], Vector(x, 500), (152 / 255, 1, 152 / 255), vel)


def accionPlataforma(plats, dt):
    # para cada plataforma
    for plat in plats:
        # se mueva hacia abajo

        plat.mover(dt / 60.0, g)
        if plat.pos.y < 0:
            del plats[0]

    # se setea el SR inicial
    glLoadIdentity()


def sobrePlataforma(fig, plats):
    for plat in plats:
        if (fig.pos.y - plat.pos.y) < 5 and (fig.pos.x-plat.pos.x)<10:
            return True
        else :
            return False


def main():
    global alto, ancho, g, rgb0
    # condiciones de la pantalla
    salto = 0
    ancho = 800
    alto = 600
    init(ancho, alto, "Chinita saltarina")
    ##########################Elementos iniciales##############
    radio_china = 50
    florss = creacionPared()
    rama = plataforma_rama(500, Vector(80, 10))
    ######################base################################

    #####gravedad inicial####
    g0 = Vector(0.0, -4.0)
    g = g0

    figuras = []
    fig1 = generadorPlataformas()  # plataforma nueva
    figuras.append(fig1)
    f = Personaje(radio_china, Vector(300, 80), (255, 0, 0))

    # se empieza a medir el tiempo
    t0 = pygame.time.get_ticks()
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == QUIT or f.pos.y < 15:  # cerrar ventana
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE and f.pos.y < 530:
                    salto = 1

                # va a la der pero no choca
                if event.key == K_RIGHT and f.pos.x < 700:
                    f.pos += Vector(10, 0)
                # va la izq y no choca
                if event.key == K_LEFT and f.pos.x > 100:
                    f.pos -= Vector(10, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers
        t1 = pygame.time.get_ticks()  # mide el tiempo final
        # ESCENAINICIAL!#######################################
        # dibujar la pared primero
        for flor in florss:
            flor.dibujar()

        vecRama = [rama]
        ###################################################

        for fig in figuras:
            fig.dibujar()

        if salto < 10 and salto > 0:
            f.saltar((t1 - t0) / 60.0, g)
            accionPlataforma(figuras, t1 - t0)
            accionPlataforma(florss, t1 - t0)
            salto += 1


        elif salto >= 10 and not (sobrePlataforma(f, figuras)):
            f.bajar((t1 - t0) / 60.0, g)

        accionPlataforma(vecRama, t1 - t0)
        f.dibujar()

        # el tiempo inicial de la siguiente iteracion es el tiempo final de esta iteracion

        t0 = t1
        print(salto)

        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

    pygame.quit()


main()
