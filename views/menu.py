#!/usr/bin/python

from models import object
import keyboard

selected = 1
#menu = {
#    {'id':1, 'menu':["Créer un nouveau tournoi", "Gérer un tournoi", "Gérer les joueurs","Quitter"]},
#}

def show_menu(menuList=0):
    global selected
    print("\n" * 30)
    print("Choose an option:")
    for i in range(1, 5):
        print("{1} {0}. Do something {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))

def up():
    global selected
    if selected == 1:
        return
    selected -= 1
    show_menu()

def down():
    global selected
    if selected == 4:
        return
    selected += 1
    show_menu()

def enter():
    global selected
    print('winner is : ',selected)
    show_menu(selected)

show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter', enter)
keyboard.wait()