from CC3501Utils import *
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla




class Reloj(Figura):
    def __init__(self, radio,pos=Vector(0, 0), rgb=(1, 1, 1),vel=Vector(0,0)):
        numtriangulos = int(1.3 * radio)
        self.radio=radio
        self.vel=vel
        self.num_triangulos=numtriangulos
        super().__init__(pos, rgb)

    def figura(self):

        numtriangulos = int(1.3 * (self.radio+self.radio))
        self.num_triangulos=numtriangulos
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0,0,0)  # rojo

        ang = 2 * pi / self.num_triangulos

        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * self.radio / 2, sin(ang_i) * self.radio / 2 + 0.8 * self.radio)

        glEnd()



        numtriangulos = int(1.3 * self.radio)
        self.num_triangulos=numtriangulos
        glBegin(GL_TRIANGLE_FAN)
        glColor3fv(self.color)  # rojo

        ang = 2 * pi / self.num_triangulos

        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * self.radio / 2, sin(ang_i) * self.radio / 2 + 0.8 * self.radio)

        glEnd()


