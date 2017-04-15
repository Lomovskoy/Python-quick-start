# coding: utf-8
# Русская рулетка
import turtle, random,math

PHI = 360 / 7# Угол фи
RAD = 50#Радиус новых окружностей
turtle.speed(0)# Скрость черепашки
start = 0
#Начальная позицияотрисовки
start_x = 0
start_y = -50
#Количество оборнотов
MIN = 7
MAX = 100
answer = ''

def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def draw_circle(r,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    
def draw_pistol(base_x,base_y):
    #основной круг
    gotoxy(base_x,base_y)
    turtle.circle(80)
    #мушка
    gotoxy(base_x,base_y+160)
    draw_circle(5,'red')
    # Барабан
    for i in range(start,7):# Тригонометрические функцииповторяются внезависимости от числа итераций 
        # Формала перевода градусов в радианы для вычисления
        phi_rad = PHI * i * math.pi / 180.0
        # Позиция перемещения пира в окружности
        gotoxy(base_x+math.sin(phi_rad)* RAD,base_y+math.cos(phi_rad)* RAD + 60)
        turtle.circle(21)

def rotate_pistol(base_x,base_y,start):
    #Формулы поворота в системе коардинат
    # Угол для синуса и косинуса наращиваем в цикле
    for i in range(start,random.randrange(MIN,MAX)):# Тригонометрические функцииповторяются внезависимости от числа итераций 
        # Формала перевода градусов в радианы для вычисления
        phi_rad = PHI * i * math.pi / 180.0
        # Позиция перемещения пира в окружности
        gotoxy(base_x+math.sin(phi_rad)* RAD,base_y+math.cos(phi_rad)* RAD + 60)
        turtle.circle(21)
        draw_circle(21,'brown')
        draw_circle(21,'white')

        
    gotoxy(base_x+math.sin(phi_rad)* RAD,base_y+math.cos(phi_rad)* RAD + 60)
    draw_circle(21,'brown')
    
    return i % 7
#----------------------------------------------------------------------------------------------------------------------------
draw_pistol(start_x,start_y)

while answer != 'n':
    answer = turtle.textinput("Испытать удачу?","y/n")
    start = rotate_pistol(start_x,start_y,start)

    # Проверка места патрона
    if start == 0:
        gotoxy(-50,250)
        turtle.write("YOU DIED",font=("Arial", 18, 'normal'))
    else:
        gotoxy(-50,250)
        turtle.write("LUCKY GUY",font=("Arial", 18, 'normal'))

    
    
