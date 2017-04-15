# coding: utf-8
# Русская рулетка
import turtle, random,math

def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def draw_circle(r,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

# Скрость черепашки
#turtle.speed(0)

turtle.goto(0,0)
turtle.circle(80)
gotoxy(0,160)
draw_circle(5,'red')

# Угол фи
phi = 360 / 7
#Радиус новых окружностей
r = 50
#Формулы поворота в системе коардинат
# Угол для синуса и косинуса наращиваем в цикле
for i in range(0,7):
    # Формала перевода градусов в радианы для вычисления
    phi_rad = phi * i * math.pi / 180.0
    # Позиция перемещения пира в окружности
    gotoxy(math.sin(phi_rad)* r,math.cos(phi_rad)* r + 60)
    turtle.circle(21)

gotoxy(math.sin(phi_rad)* r,math.cos(phi_rad)* r + 60)
draw_circle(21,'brown')
