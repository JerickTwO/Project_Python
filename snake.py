import turtle
import time 
import random

posponer = 0.1

#Marcador 
puntaje = 0
puntaje_mas_alto = 0

#Fondo
wn = turtle.Screen()
wn.title('juego de snake')
wn.bgcolor('black')
wn.setup(600, 600)
wn.tracer()

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntaje      Mayor Puntaje",
             align = "center", font =("Courier", 20, "normal"))

#Cabeza
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'stop'
cabeza.color('green')

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.penup()
comida.goto(0,100)
comida.color('red')

#Cuerpo
segmentos = []


#Funciones
def arriba():
    cabeza.direction = 'up'
def abajo():
    cabeza.direction = 'down'
def izquierda():
    cabeza.direction = 'left'
def derecha():
    cabeza.direction = 'right'
def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)
#Teclado
wn.listen()
wn.onkeypress(arriba, 'Up')
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')

while True:
    wn.update()

    #Colisiones con bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Eiminar los segmentos.
        for segmento in segmentos:
            segmento.hideturtle()

        #Limpiar segmaentos
        segmentos.clear()

        #Resetear marcador
        puntaje = 0
        texto.clear()
        texto.write("Puntaje: {}      Mayor Puntaje: {}".format(puntaje,puntaje_mas_alto), 
                align = "center", font =("Courier", 20, "normal"))

    #Colision de comida
    if cabeza.distance(comida) <20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.penup()
        nuevo_segmento.color('light green')
        segmentos.append(nuevo_segmento)

        #Aumentar marcador
        puntaje += 10

        if puntaje > puntaje_mas_alto:
            puntaje_mas_alto = puntaje
            
        texto.clear()
        texto.write("Puntaje: {}      Mayor Puntaje: {}".format(puntaje,puntaje_mas_alto), 
                align = "center", font =("Courier", 20, "normal"))

