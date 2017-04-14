# coding: utf-8

# Python. Быстрый старт.
# Занятие 3.

# Домашнее задание: 
#   функциями dir и help исследовать модули os, sys, psutil
#   вывести максимум информации о системе (ветка №2):
#   имя текущей директории, платформа (ОС), кодировка файловой системы,
#   логин пользователя, количество CPU


# Подключение модуля производится командой import.
# Модуль os идет в комплекте с Python'ом.
import os
import sys
# psutil - сторонний модуль, нужно установить через pip install psutil
import psutil       


print("Great Python Program!")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

while True:
    answer = input("Давайте поработаем? (Y/N)")
         
    if answer == 'Y' or answer == 'y':
        print("Отлично, друг!")
        print("Я умею:")
        print(" [1] - выведу список файлов текущей директория")
        print(" [2] - выведу текущую директорию")
        print(" [3] - выведу список id процессов")
        print(" [4] - выведу информацию об операционной системе")
        do = int(input("Укажите номер действия: "))
        
        if do == 1:
            print(os.listdir())
        elif do == 2:
            print(os.getcwd())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print(sys.platform)
            print(os.name)
            
        else:
            print("Введите цифру из списка!")
       
    # Функция type выводит информацию о типе переменной (объекта)
    # Функция dir показывает внутреннее содержимое переменной (объекта) - атрибуты, методы
    # Функция help выводит встронную справку об объекте
        
    elif answer == 'N' or answer == 'n':    
        print("До свидания!")
        break
    else:
        print("Неизвестный ответ")    
