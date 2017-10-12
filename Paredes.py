from CC3501Utils import *
import os
from Plataformas import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla

#esta clase solo crea un objeto flor que sera utilizado en la case tarea2 para generar las paredes
class florFigura(Figura):
    def __init__(self, colorHojas,pos=Vector(100, 100), rgb=(1, 51 / 255, 1)):
        self.radio=600/15/2
        self.colorHojas1=colorHojas
        self.num_triangulos = int(1.3 * self.radio)
        super().__init__(pos, rgb)

    def figura(self):

        # circulo izq
        glBegin(GL_TRIANGLE_FAN)
        glColor3fv(self.colorHojas1)
        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * self.radio - self.radio / 8, sin(ang_i) * self.radio + self.radio)

        glEnd()

        # circulo der
        glBegin(GL_TRIANGLE_FAN)
        glColor3fv(self.colorHojas1)
        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * self.radio + self.radio * 2, sin(ang_i) * self.radio + self.radio)

        glEnd()

        # circulo arriba
        glBegin(GL_TRIANGLE_FAN)
        glColor3fv(self.colorHojas1)
        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * self.radio + self.radio, sin(ang_i) * self.radio + self.radio * 2)

        glEnd()

        # circulo abajo
        glBegin(GL_TRIANGLE_FAN)
        glColor3fv(self.colorHojas1)
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


