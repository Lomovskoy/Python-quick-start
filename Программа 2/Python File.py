# coding: utf-8

import turtle, random

# Скрость черепашки
turtle.speed(0)
answer = ''

while answer != 'N' or answer != 'n':
    
    answer = turtle.textinput("Нарисовать окружность","Y/N")
    
    if answer == 'Y' or answer == 'y':
        # Отрыв пера
        turtle.penup()
        # Определяем коардинату центра окружности
        turtle.goto(random.randrange(-400,400),random.randrange(-400,400))
        # Опустить перо
        turtle.pendown()
        # Цвета
        turtle.fillcolor(random.random(),random.random(),random.random())
        turtle.begin_fill()
        # Радиус окружности
        turtle.circle(random.randrange(1,100))
        turtle.end_fill()

    else:
        pass
