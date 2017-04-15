# coding: utf-8

# Python. Быстрый старт.
# Занятие 3.

# Домашнее задание: 
#   функциями dir и help исследовать модули os, sys, psutil
#   вывести максимум информации о системе (ветка №2):
#   имя текущей директории, платформа (ОС), кодировка файловой системы,
#   логин пользователя, количество CPU


# Подключение модуля производится командой import.
# Модули os,sys идут в комплекте с Python'ом.
import os
import sys
import shutil
# psutil - сторонний модуль, нужно установить через pip install psutil
import psutil       


print("\t\tРобот помошник Python")
print("\t\tПривет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

while True:
    answer = input("Давайте поработаем? (Y/N) ")
         
    if answer == 'Y' or answer == 'y':
        print("Отлично, друг!")
        print("Я умею:")
        print("\t[1] - выведу список файлов текущей директория")
        print("\t[2] - выведу информацию об операционной системе")
        print("\t[3] - выведу список id процессов")
        print("\t[4] - дублирую файлы в текущей директории")
        print("\t[5] - дублирую указанный файл")
        print("\t[6] - удаляю дибликаты")
        do = int(input("Укажите номер действия: "))
        
        if do == 1:
            print(os.listdir())
        elif do == 2:
            print("Вот, что я знаю о системе: ")
            print("\tКоличество процессоров: ", psutil.cpu_count())
            print("\tПлатформа: ", sys.platform)
            print("\tКодировка файловой системы: ", sys.getfilesystemencoding())
            print("\tТекущая директория: ", os.getcwd())
            print("\tТекущий пользователь: ", os.getlogin())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            file_list = os.listdir()
            for f in file_list:
                #Проверка является ли элемент файлом
                if os.path.isfile(f):
                    newfile = f + '.dupl'
                    #копируем
                    shutil.copy(f, newfile)
        elif do == 5:
            file_name = input("Введите имя файла и относительный путь до него (. - текущая): ")
            #Проверка является ли элемент файлом
            if os.path.isfile(file_name):
                newfile = file_name + '.dupl'
                #копируем
                shutil.copy(file_name, newfile)
                
        elif do == 6:
            dirname = input("Укажите относительную директорию (. - текущая): ")# . текущая
            file_list = os.listdir(dirname)
            for f in file_list:
                # join формирует имя файла в зависимости от операционной системы / \
                file_name = os.path.join(dirname,f)
                # проверка на окончение файла
                if file_name.endswith('.dupl'):
                    os.remove(file_name)#Удалить
                
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
