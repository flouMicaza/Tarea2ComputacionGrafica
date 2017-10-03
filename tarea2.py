#la clase círculo contenida es esta tarea copiada de material docente.

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


class Personaje(Figura):
    def __init__(self, radio,pos=Vector(0, 0), rgb=(1.0, 0, 0)):
        numtriangulos = int(1.3 * radio)
        self.radio=radio
        self.num_triangulos=numtriangulos
        super().__init__(pos, rgb)

    def figura(self):
        #cabeza
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos

        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * 50, sin(ang_i) * 50 + 80)

        glEnd()

        #ojos
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 1, 1)  # rojo

        ang = 2 * pi / self.num_triangulos

        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * 5 + 20, sin(ang_i) * 5 + 110)

        glEnd()

        # ojos
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 1, 1)

        ang = 2 * pi / self.num_triangulos

        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * 5 + -20, sin(ang_i) * 5 + 110)

        glEnd()

        #antenas
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(15, 115)
        glVertex2f(45, 140)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(-15, 115)
        glVertex2f(-45, 140)
        glEnd()

        #patas hacia la derecha
        glBegin(GL_LINES)
        glColor3f(0,0,0)
        glVertex2f(70, 70)
        glVertex2f(120, 110)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(70, 0)
        glVertex2f(150, 0)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(70, -70)
        glVertex2f(120, -110)
        glEnd()

        #patas hacia la izquierda
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(-70, 70)
        glVertex2f(-120, 110)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(-70, 0)
        glVertex2f(-150, 0)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(-70, -70)
        glVertex2f(-120, -110)
        glEnd()


        #circulo base rojo
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(255,0,0)  #rojo
        glVertex2f(0.0, 0.0)

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glColor3f(230, 0, 0)  # rojo
            glVertex2f(cos(ang_i) * (self.radio), sin(ang_i) * (self.radio))

        glVertex2f(1.0 * self.radio, 0.0)
        glEnd()

        # triangulo de las alas
        glBegin(GL_TRIANGLES)
        glColor3f(0,0,0)  # NEGRO
        glVertex2f(-45/cos(25),-90)
        glVertex2f(0,-10)
        glVertex2f(45/cos(50),-90)
        glEnd()

        #linea de almedio
        glBegin(GL_LINES)
        glColor3f(0,0,0)
        glVertex2f(0,100)
        glVertex2f(0,-25)
        glEnd()



        #puntitos
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (15)+30, sin(ang_i) * (15)+50)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (15)+70, sin(ang_i) * (15))
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (12) + 40, sin(ang_i) * (12) - 30)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (15) -50, sin(ang_i) * (15) + 50)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (15) -30, sin(ang_i) * (15))
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (18) -60, sin(ang_i) * (18) - 50)
        glEnd()




def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "titulo")
    radio=100

    figuras = []
    #t = Triangulo(Vector(200, 200), Vector(600, 200), Vector(400, 500), (1, 0, 0))
    #figuras.append(t)

    f=Personaje(radio,Vector(250, 200),(255, 0, 0))
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


        #glBegin(GL_LINES)
        #glVertex2f(500, 500)
        #glVertex2f(500, 600)
        #glEnd()

        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

    pygame.quit()


main()
