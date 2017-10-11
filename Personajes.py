from CC3501Utils import *
import os
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
            glVertex2f(cos(ang_i) * self.radio/2, sin(ang_i) * self.radio/2 + 0.8*self.radio)

        glEnd()



        # antenas
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(0.15 * self.radio, 1.15 * self.radio)
        glVertex2f(0.45 * self.radio, 1.40 * self.radio)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(-0.15 * self.radio, 1.15 * self.radio)
        glVertex2f(-0.45 * self.radio, 1.40 * self.radio)
        glEnd()

        # ojos
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 1, 1)  # rojo

        ang = 2 * pi / self.num_triangulos

        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * 5 + 0.2 * self.radio, sin(ang_i) * 5 + self.radio * 1.1)

        glEnd()

        # ojos
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 1, 1)

        ang = 2 * pi / self.num_triangulos

        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * 5 + -0.2*self.radio, sin(ang_i) * 5 + 1.1*self.radio)

        glEnd()


        #patas hacia la derecha
        glBegin(GL_LINES)
        glColor3f(0,0,0)
        glVertex2f(0.70*self.radio, 0.70*self.radio)
        glVertex2f(1.20*self.radio, 1.10*self.radio)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(0.70*self.radio, 0)
        glVertex2f(1.50*self.radio, 0)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(0.70*self.radio, -0.70*self.radio)
        glVertex2f(1.20*self.radio, -1.10*self.radio)
        glEnd()

        #patas hacia la izquierda
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(-0.70*self.radio, 0.70*self.radio)
        glVertex2f(-1.20*self.radio, 1.10*self.radio)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(-0.70*self.radio, 0)
        glVertex2f(-1.50*self.radio, 0)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(-0.70*self.radio, -0.70*self.radio)
        glVertex2f(-1.20*self.radio, -1.10*self.radio)
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
        glVertex2f(-0.45*self.radio/cos(0.25*self.radio),-0.90*self.radio)
        glVertex2f(0,-0.10*self.radio)
        glVertex2f(0.45*self.radio/cos(0.50*self.radio),-0.90*self.radio)
        glEnd()

        #linea de almedio
        glBegin(GL_LINES)
        glColor3f(0,0,0)
        glVertex2f(0,self.radio)
        glVertex2f(0,-0.5*self.radio)
        glEnd()



        #puntitos
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (0.15*self.radio)+0.30*self.radio, sin(ang_i) * (0.15*self.radio)+0.50*self.radio)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (0.15*self.radio)+0.70*self.radio, sin(ang_i) * (0.15*self.radio))
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (0.12*self.radio) + 0.4*self.radio, sin(ang_i) * (0.12*self.radio) - 0.3*self.radio)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (0.15*self.radio) -0.50*self.radio, sin(ang_i) * (0.15*self.radio) + 0.50*self.radio)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (0.15*self.radio) -0.30*self.radio, sin(ang_i) * (0.15*self.radio))
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # rojo

        ang = 2 * pi / self.num_triangulos
        for i in range(self.num_triangulos):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * (0.18*self.radio) -0.60*self.radio, sin(ang_i) * (0.18*self.radio) - 0.50*self.radio)
        glEnd()


