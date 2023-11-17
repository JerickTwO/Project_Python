import turtle
import time 
import random

posponer = 0.1

#Marcador.
puntaje = 0
puntaje_mas_alto = 0

#Fondo.
wn = turtle.Screen()
wn.title('juego de snake')
wn.bgcolor('black')
wn.setup(600, 600)
wn.tracer()

#Texto.
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntaje      Mayor Puntaje",
             align = "center", font =("Courier", 20, "normal"))
