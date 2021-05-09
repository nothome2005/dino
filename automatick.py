import pyautogui as pg
from time import sleep
import keyboard

key = 'ctrl'
key1='shift'
input("Наведите курсор мыши на поле ввода и нажмите Enter")

x1,y1=pg.position()
print(x1,y1)
input("Наведите курсор мыши на кнопку отправки и нажмите Enter")
x2,y2=pg.position()
print(x2,y2)
player_select = input("\tТекст кометария(только на английском):")
print(player_select)
time=int(input("\tЗадержка между вводом коментариев в секундах:"))
print(time)
count=int(input("\tКол-во коментариев:"))
print("Для экстренной остановки нажмите ctrl")
for i in range(count):

    pg.moveTo(x1, y1,2)
    if keyboard.is_pressed(key):
        break       
    pg.click(x1, y1)
    pg.typewrite(str(player_select),interval=0.2)
    if keyboard.is_pressed(key):
        break
# Выполнения нажатия на клавишу       
    pg.moveTo(x2, y2)
    pg.click(x2, y2)
    if keyboard.is_pressed(key):
        break
print("Пргорамма завершена.")
input("")