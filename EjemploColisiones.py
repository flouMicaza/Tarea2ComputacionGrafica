#####################################################################
# Daniel Calderon S.
# CC3501-1
# Primavera 2010
#####################################################################
from random import uniform

from CC3501Utils import *


#####################################################################
# Funciones de graficos
#####################################################################

def init(ancho, alto, titulo):
    # inicializar pygame
    pygame.init()
    pygame.display.set_mode((ancho, alto), OPENGL | DOUBLEBUF)
    pygame.display.set_caption(titulo)

    # inicializar opengl
    glViewport(0, 0, ancho, alto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, ancho, 0.0, alto) # tipo de vista
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # definir variables de opengl
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDisable(GL_DEPTH_TEST)
    return


#####################################################################
# Clase circulo y manejo
#####################################################################


class Circulo:
    def __init__(self, r, pos, vel, rgb, num_triangulos):
        self.radio = r# radio del circulo
        self.pos = pos  # posicion del circulo
        self.vel = vel  # velocidad del circulo
        self.nun_triangulos = num_triangulos  # numero de triangulos a utilizar

        self.rgb = []  # color del circulo
        self.rgb.append(rgb[0])  # se agregan elementos a self.rgb
        self.rgb.append(rgb[1])
        self.rgb.append(rgb[2])

        self.vida = 100 # cantidad de choques que resiste

        # guardamos el dibujo en una lista
        self.lista = 0  # crea la variable de instancia "lista"
        self.crear()

    def mover(self,dt):
        # modificamos la velocidad con la aceleracion
        self.vel = sumar(self.vel, ponderar(dt, g))

        # modificamos la posicion con la velocidad
        self.pos = sumar(self.pos, ponderar(dt, self.vel))

    def crear(self):
        # creamos la matriz (lista)
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)

        # "dibujamos" en la lista
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0.0, 0.0)

        angulo = 2 * pi / self.nun_triangulos
        for i in range(self.nun_triangulos):
            angulo_i = angulo * i
            glVertex2f(cos(angulo_i), sin(angulo_i))

        glVertex2f(1.0, 0.0)
        glEnd()  # cierra el glBegin

        # cerramos la lista
        glEndList()

    def dibujar(self):
        # poner SR base
        glPushMatrix()

        # nos vamos a la posicion
        glTranslatef(self.pos.x, self.pos.y, 0.0)

        # escalamos en el tamano, asi la unidad es el r
        glScalef(self.radio * 2, self.radio, 0.0)

        # asignamos color
        glColor3f(self.rgb[0], self.rgb[1], self.rgb[2])

        # dibujamos lo almacenado en la lista
        glCallList(self.lista)

        # sacar SR base
        glPopMatrix()

    # cambia el color del circulo, distintas alternativas
    def colorear(self):
        # se ponen amarillos con los golpes
        self.rgb = [1, 1, self.vida / 10.0]

        # aleatorio entre amarillo y blanco
        # self.rgb=[1,1,uniform(0,1)]

        # color aleatorio
        self.rgb=[uniform(0,1),uniform(0,1),uniform(0,1)]


def chocar(c1, c2):
    normal = normalizar(restar(c2.pos, c1.pos))
    tangente = rotar(normal, pi / 2)

    # condicion para que no se produzcan rebotes dobles
    if not punto(c2.vel, normal) > 0 > punto(c1.vel, normal):
        # ver archivo anexo
        v1normal = ponderar(punto(c1.vel, normal), normal)
        v1tang = ponderar(punto(c1.vel, tangente), tangente)

        v2norm = ponderar(punto(c2.vel, normal), normal)
        v2tang = ponderar(punto(c2.vel, tangente), tangente)

        c1.vel = sumar(v2norm, v1tang)
        c2.vel = sumar(v1normal, v2tang)

        # cambiar colores de los circulos
        c1.colorear()
        c2.colorear()


def estan_chocando(c1, c2):
    return distancia(c1.pos, c2.pos) < (c1.radio + c2.radio)


def chocar_borde(c):
    if c.pos.x + c.radio > ancho:
        c.vel.x = -abs(c.vel.x)  # rebotar
        c.pos.x = ancho - c.radio  # quedarse dentro de la pantalla

    if c.pos.x < c.radio:
        c.vel.x = abs(c.vel.x)
        c.pos.x = c.radio

    if c.pos.y > alto - c.radio:
        c.vel.y = -abs(c.vel.y)
        c.pos.y = alto - c.radio

    if c.pos.y < c.radio:
        c.vel.y = abs(c.vel.y)
        c.pos.y = c.radio


def accion(circulos, dt):
    # limpia la pantalla para volver a dibujar
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # para cada circulo
    for i in range(len(circulos)):
        # se mueve
        circulos[i].mover(dt / 60.0)

        # se verifica colision con el borde
        chocar_borde(circulos[i])

        # se dibuja
        circulos[i].dibujar()

        # se revisa colision con otro circulo
        for j in range(i + 1, len(circulos)):
            if estan_chocando(circulos[i], circulos[j]):
                # si estan chocando, cambian su velocidad
                chocar(circulos[i], circulos[j])
                # y pierden una vida
                circulos[i].vida = circulos[i].vida - 1
                circulos[j].vida = circulos[j].vida - 1

    # si hay ciculos con 0 vidas se eliminan
    n = len(circulos)
    aux = []
    for i in range(n):
        # pop() saca el ultimo elemento de una lista
        c = circulos.pop()

        # si el elemento sacado tiene vidas se agrega a aux
        if c.vida > 0:
            aux.append(c)
            # sino tenia vidas, no se hace nada

    # se devuelven los elementos de aux a cs
    for a in aux:
        circulos.append(a)

    # se setea el SR inicial
    glLoadIdentity()


#####################################################################
# Programa principal
#####################################################################


def main():
    global alto, ancho, g, rgb0

    rgb0 = [1.0, 1.0, 1.0]  # color inicial circulos

    num_circulos = 5  # numero de circulos
    radio = 30  # radio de circulos
    ancho = 800  # ancho de pantalla
    alto = 600  # alto de pantalla

    num_triangulos = int(1.3 * radio)  # numero de triangulos para cada circulo
    vel_ang = pi / 12  # angulo en el que rotara la gravedad

    # inicializando...
    init(ancho, alto, "Ejemplo Colisiones")

    # contenedor de elementos a dibujar
    circulos = []

    # gravedad inicial
    g0 = Vector(0.0, -4.0)
    g = g0

    for i in range(num_circulos):
        # posicion inicial aleatoria dentro de la pantalla
        pos = Vector(uniform(radio, ancho - radio), uniform(radio, alto - radio))

        # velocidad inicial aleatorea en x
        vel = Vector(uniform(-30, 30), 0.0)

        # crea un circulo y lo agrega a circulos
        circulos.append(Circulo(radio, pos, vel, rgb0, num_triangulos))

    # se empieza a medir el tiempo
    t0 = pygame.time.get_ticks()

    run = True  # control de iteracion

    while run:

        # Control de eventos...
        # se itera para cada evento detectado
        for event in pygame.event.get():

            # evento cerrar ventana
            if event.type == QUIT:
                run = False

            # evento presionar tecla
            if event.type == KEYDOWN:

                # cerrar
                if event.key == K_ESCAPE:
                    run = False

                # rotar gravedad con las flechas
                if event.key == K_LEFT:
                    g = rotar(g, vel_ang)
                if event.key == K_RIGHT:
                    g = rotar(g, -vel_ang)
                if event.key == K_UP:
                    g = rotar(g, pi / 2)
                if event.key == K_DOWN:
                    g = rotar(g, -pi / 2)

                # crear nuevo ciculo
                if event.key == K_n:
                    pos = Vector(uniform(radio, ancho - radio), uniform(radio, alto - radio))
                    vel = Vector(uniform(-30, 30), uniform(0, 0))
                    circulos.append(Circulo(radio, pos, vel, rgb0, num_triangulos))

                # eliminar ultimo circulo
                if event.key == K_m:
                    if len(circulos) > 0:
                        del circulos[len(circulos) - 1]

                # deja de un mismo color aleatorio todos los circulos
                if event.key == K_c:
                    rgb0 = [uniform(0, 1), uniform(0, 1), uniform(0, 1)]
                    for c in circulos:
                        c.rgb = rgb0

                # deja todos los circulos blancos
                if event.key == K_w:
                    glColor4f(1.0, 1.0, 1.0, 0.0)

                # alterna entre activar y desactivar la gravedad
                if event.key == K_0:
                    if g.modulo() != 0:
                        g = Vector(0, 0)
                    else:
                        g = g0

        # que cada objeto actue durante el intervalo de tiempo tardado
        t1 = pygame.time.get_ticks()  # mide el tiempo final
        accion(circulos, t1 - t0)

        pygame.display.flip()
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

        # el tiempo inicial de la siguiente iteracion es el tiempo final de esta iteracion
        t0 = t1

    pygame.quit()  # cierra la ventana pygame


# necesario para que el programa se pueda llamar mediante argumentos,
# sino se usan argumentos no hay problema, se llama al main
if __name__ == "__main__":
    main()