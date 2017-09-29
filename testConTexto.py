import os
from random import uniform

from CC3501Utils import *
from texto import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


class Linea(Figura):
    def __init__(self, p1: Vector, p2: Vector, rgb=(1.0, 1.0, 1.0), pos=Vector(0, 0)):
        self.p1 = p1
        self.p2 = p2
        super().__init__(pos, rgb)

    def figura(self):
        glBegin(GL_LINES)
        glVertex2f(self.p1.x, self.p1.y)
        glVertex2f(self.p2.x, self.p2.y)
        glEnd()


class Triangulo(Figura):
    def __init__(self, p1: Vector, p2: Vector, p3: Vector, rgb=(1.0, 1.0, 1.0), pos=Vector(0, 0)):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        super().__init__(pos, rgb)

    def figura(self):
        glBegin(GL_TRIANGLES)
        glVertex2fv(self.p1.cartesianas())
        glVertex2fv(self.p2.cartesianas())
        glVertex2fv(self.p3.cartesianas())
        glEnd()


def main():
    ancho = 800
    alto = 600

    init(ancho, alto, "test")

    figuras = []
    linea = Linea(Vector(10, 10), Vector(300, 200), (1, 0, 0))
    trian = Triangulo(Vector(500, 400), Vector(270, 220), Vector(100, 500), (1, 0, 0))

    figuras.append(linea)
    figuras.append(trian)

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    p1 = Vector(uniform(0, 800), uniform(0, 600))
                    p2 = Vector(uniform(0, 800), uniform(0, 600))
                    rgb = (uniform(0, 1), uniform(0, 1), uniform(0, 1))
                    figuras.append(Linea(p1, p2, rgb))

                if event.key == K_RIGHT:
                    trian.pos += Vector(10, 0)
                if event.key == K_LEFT:
                    trian.pos -= Vector(10, 0)
                if event.key == K_UP:
                    trian.pos += Vector(0, 10)
                if event.key == K_DOWN:
                    trian.pos -= Vector(0, 10)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for fig in figuras:
            fig.dibujar()
        trian.dibujar()

        draw_text(100, 100, "holi")

        pygame.display.flip()
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

    pygame.quit()


main()
