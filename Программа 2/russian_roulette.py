# coding: utf-8
# Русская рулетка
import turtle, random,math
# Угол фи
PHI = 360 / 7
#Радиус новых окружностей
RAD = 50
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
turtle.speed(0)
start = 0
turtle.goto(0,0)
turtle.circle(80)
gotoxy(0,160)
draw_circle(5,'red')

# Угол фи
phi = 360 / 7
#Радиус новых окружностей
r = 50
for i in range(start,7):# Тригонометрические функцииповторяются внезависимости от числа итераций 
        # Формала перевода градусов в радианы для вычисления
        phi_rad = phi * i * math.pi / 180.0
        # Позиция перемещения пира в окружности
        gotoxy(math.sin(phi_rad)* r,math.cos(phi_rad)* r + 60)
        turtle.circle(21)

answer = turtle.textinput("Испытать удачу?","y/n")

while answer != 'n':
    #Формулы поворота в системе коардинат
    # Угол для синуса и косинуса наращиваем в цикле
    for i in range(start,random.randrange(7,100)):# Тригонометрические функцииповторяются внезависимости от числа итераций 
        # Формала перевода градусов в радианы для вычисления
        phi_rad = phi * i * math.pi / 180.0
        # Позиция перемещения пира в окружности
        gotoxy(math.sin(phi_rad)* r,math.cos(phi_rad)* r + 60)
        turtle.circle(21)
        draw_circle(21,'brown')
        draw_circle(21,'white')

        
    gotoxy(math.sin(phi_rad)* r,math.cos(phi_rad)* r + 60)
    draw_circle(21,'brown')

    start = i % 7
    # Проверка места патрона
    if start == 0:
        gotoxy(-50,250)
        turtle.write("YOU DIED",font=("Arial", 18, 'normal'))
    else:
        gotoxy(-50,250)
        turtle.write("LUCKY GUY",font=("Arial", 18, 'normal'))

    answer = turtle.textinput("Испытать удачу?","y/n")
    
    
