from CC3501Utils import *
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


class plataforma_hoja(Figura):
    def __init__(self, largo, pos=Vector(300, 300), rgb=(152 / 255, 1, 152 / 255),vel=Vector(0,0)):
        self.largo = largo
        self.vel=vel
        self.numtriangulos = int(1.3 * largo)
        super().__init__(pos, rgb)

    def figura(self):
        # base de la hoja
        glBegin(GL_TRIANGLE_FAN)

        ang = 2 * pi / self.numtriangulos
        numero = round(self.numtriangulos / 4)
        ies = []
        for i in range(self.numtriangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (self.largo + 25), sin(ang_i) * (self.largo))

            if i == numero:
                ies.append(i)
            if i == numero * 2:
                ies.append(i)

            if i == numero * 3:
                ies.append(i)

            if i == numero * 4:
                ies.append(i)
        glEnd()

        ies = [self.numtriangulos / 10, 2 * self.numtriangulos / 10, 3 * self.numtriangulos / 10,
               7 * self.numtriangulos / 10, 8 * self.numtriangulos / 10, 9 * self.numtriangulos / 10]
        for i in range(len(ies)):
            ang_i = ang * ies[i]
            glBegin(GL_LINES)
            glColor3f(0, 0, 0)
            if i == 0 or i == 5:
                glVertex2f(self.largo / 3, 0)
                glVertex2f(cos(ang_i) * (self.largo + 25), sin(ang_i) * (self.largo))

            elif i == 4 or i == 1:
                glVertex2f(-self.largo / 3, 0)
                glVertex2f(cos(ang_i) * (self.largo + 25), sin(ang_i) * (self.largo))

            elif i == 2 or i == 3:
                glVertex2f(-(self.largo - self.largo / 7), 0)
                glVertex2f(cos(ang_i) * (self.largo + 25), sin(ang_i) * (self.largo))

            glEnd()
        # raices linea horizontal
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(-(self.largo + 24), 0)
        glVertex2f(self.largo + 24, 0)
        glEnd()

        distRaices = (self.largo + 24) / 2 - self.largo / 3

    def mover(self,dt,g):
        # modificamos la velocidad con la aceleracion
        self.vel = sumar(self.vel, ponderar(dt, g))

        # modificamos la posicion con la velocidad
        self.pos = sumar(self.pos, Vector(0,-15))

# plataforma que recibe el radio del circulo central y el color de sus hojas ademas del color del centro
class plataforma_flor(Figura):
    def __init__(self, radio, colorHojas, pos=Vector(100, 100), rgb=(1, 51 / 255, 1),vel=Vector(0,0)):
        self.radio = radio
        self.vel=vel
        self.num_triangulos = int(1.3 * radio)
        self.colorHojas = colorHojas
        super().__init__(pos, rgb)

    def figura(self):
        # circulo izq
        glBegin(GL_TRIANGLE_FAN)
        glColor3fv(self.colorHojas)
        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * self.radio - self.radio / 8, sin(ang_i) * self.radio + self.radio)

        glEnd()

        # circulo der
        glBegin(GL_TRIANGLE_FAN)
        glColor3fv(self.colorHojas)
        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * self.radio + self.radio * 2, sin(ang_i) * self.radio + self.radio)

        glEnd()

        # circulo arriba
        glBegin(GL_TRIANGLE_FAN)
        glColor3fv(self.colorHojas)
        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * self.radio + self.radio, sin(ang_i) * self.radio + self.radio * 2)

        glEnd()

        # circulo abajo
        glBegin(GL_TRIANGLE_FAN)
        glColor3fv(self.colorHojas)
        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * self.radio + self.radio, sin(ang_i) * self.radio - self.radio / 8)

        glEnd()

        # circulo central
        glBegin(GL_TRIANGLE_FAN)
        glColor3fv(self.color)
        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * 7 * self.radio / 8 + self.radio, sin(ang_i) * 7 * self.radio / 8 + self.radio)

        glEnd()

        #linea para la plataforma
        glBegin(GL_QUADS)
        glColor3f(218, 201, 201)
        glVertex2f(-self.radio,self.radio)
        glVertex2f(3*self.radio,self.radio)
        glVertex2f(3*self.radio,self.radio*2/3)

        glVertex2f(-self.radio,self.radio*2/3)
        glEnd()

    def mover(self, dt,g):
        # modificamos la velocidad con la aceleracion
        self.vel = sumar(self.vel, ponderar(dt, g))

        # modificamos la posicion con la velocidad
        self.pos = sumar(self.pos, Vector(0,-15))


class plataforma_rama(Figura):
    def __init__(self, largo, pos=Vector(100, 100), rgb=(115 / 255, 112 / 255, 12 / 255),vel=Vector(0,0)):
        self.largo = largo
        self.vel=vel
        super().__init__(pos, rgb)

    def figura(self):
        # rama ppal
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(self.largo, 0)
        glVertex2f(self.largo, 20)
        glVertex2f(0, 20)
        glEnd()

        # rama para arriba
        glBegin(GL_QUADS)
        glVertex2f(2 * self.largo / 3,0)
        glColor3fv(self.color)
        glVertex2f(2 * self.largo / 3 + 10, -2)
        glVertex2f(self.largo + 10, tan(45) * self.largo / 3)

        glVertex2f(self.largo, tan(45) * self.largo / 3)

        glEnd()

        # rama para arriba
        glBegin(GL_QUADS)
        glColor3fv(self.color)
        glVertex2f(2 * self.largo / 3, 0)
        glVertex2f(2 * self.largo / 3 + 10, 0)
        glVertex2f(self.largo + 10,- tan(45) * self.largo /8)
        glVertex2f(self.largo, -tan(45) * self.largo /8)
        glEnd()


    def mover(self,dt,g):
        # modificamos la velocidad con la aceleracion
        self.vel = sumar(self.vel, ponderar(dt, g))

        # modificamos la posicion con la velocidad
        self.pos = sumar(self.pos, Vector(0,-15))
