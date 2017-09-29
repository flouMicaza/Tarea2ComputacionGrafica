import os

from CC3501Utils import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


class Triangulo(Figura):
    def __init__(self, p1: Vector, p2: Vector, p3: Vector, rgb=(1.0, 1.0, 1.0), pos=Vector(0, 0)):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        super().__init__(pos, rgb)

    def figura(self):
        glBegin(GL_TRIANGLES)
        glVertex2f(self.p1.x, self.p1.y)
        glVertex2f(self.p2.x, self.p2.y)
        glVertex2f(self.p3.x, self.p3.y)
        glEnd()


class Persona(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super().__init__(pos, rgb)

    def figura(self):
        # "dibujamos" en la lista
        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 0.0)
        # cuello
        glVertex2f(2, 0)
        glVertex2f(-2, 0)
        glVertex2f(-2, -15)
        glVertex2f(2, -15)
        # cuerpo
        glColor3f(100.0, 100.0, 4.0)
        glVertex2f(12, -15)  # hombro
        glVertex2f(-12, -15)  # hombro

        glVertex2f(-12, -50)  # cadera
        # chantar un color entremedio hace un dregrade!
        glColor3f(1.0, 1.0, 0.0)
        glVertex2f(12, -50)  # cadera
        glColor3f(1.0, 1.0, 0.0)
        glEnd()

        # cabeza
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(66 / 255.0, 226 / 255.0, 244 / 255.0)  # celeste
        glVertex2f(0.0, 0.0)

        radio = 10
        ang = 2 * pi / 20
        for i in range(20):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio, sin(ang_i) * radio)

        glVertex2f(1.0 * radio, 0.0)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(0.0, 0.0, 0.6)  # azul
        # pierna1
        glVertex2f(-12, -50)  # cadera
        glVertex2f(-6, -50)
        glVertex2f(-9, -70)

        # pierna2
        glVertex2f(12, -50)  # cadera
        glVertex2f(6, -50)
        glVertex2f(9, -70)

        glColor3f(0.0, 1.0, 0.0)  # verde
        # brazo1
        glVertex2f(12, -15)  # hombro
        glVertex2f(12, -20)
        glVertex2f(30, -15)

        # brazo2
        glVertex2f(-12, -15)  # hombro
        glVertex2f(-12, -20)
        glVertex2f(-20, -15)
        glEnd()


def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "titulo")

    figuras = []
    t = Triangulo(Vector(0, 0), Vector(600, 200), Vector(400, 500), (1, 0, 0))
    figuras.append(t)

    p = Persona(Vector(400, 300))  # posicion inicial del personaje

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pass


                if event.key == K_a:
                    p.pos += Vector(10, 0)
                if event.key == K_d:
                    p.pos -= Vector(10, 0)
                if event.key == K_w:
                    p.pos += Vector(0, 10)
                if event.key == K_s:
                    p.pos -= Vector(0, 10)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers

        # dibujar figuras
        for fig in figuras:
            fig.dibujar()
        p.dibujar()

        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

    pygame.quit()


main()
