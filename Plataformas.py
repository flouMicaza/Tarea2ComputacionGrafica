from CC3501Utils import *
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla

class plataforma_hoja(Figura):
    def __init__(self,largo,color1=152,color2=255, color3=152 ,pos=Vector(100,100), rgb=(152/255, 1,152/255)):
        self.largo=largo
        self.numtriangulos = int(1.3 * largo)
        super().__init__(pos, rgb)

    def figura(self):
        #base de la hoja
        glBegin(GL_TRIANGLE_FAN)


        ang = 2 * pi / self.numtriangulos

        for i in range(self.numtriangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i)*(self.largo+25), sin(ang_i)*(self.largo))
        glEnd()

        #raices
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(-(self.largo+24),0)
        glVertex2f(self.largo+24,0)
        glEnd()
        # raices
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(10, 0)
        glVertex2f(30, 11)
        glEnd()
