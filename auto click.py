import mouse
import keyboard
import time
import pyautogui

keys = ["q","w","e","r","t","y","u","i","o","p",
       "a","s","d","f","g","h","j","k",
       "l","z","x","c","b","v","n","m", "esc","space", "SHIFT","caps lock", 'tab','enter',
       "delete", "home", "end", "page up", "page down", "insert", "ctrl", "alt", 
       "1", "2", "3", "4", "5", "6", "7" , "8", "9", "0", 
       "/", "*", "-", "+", ".", "|", "'", ",", ".", "/", ";", "-", "=" , "[" , "]", "`"]

start_key = input('Клавиша старта: ')
stop_key = input('Клавиша остановки: ')
method = input("Введите метод ('key' или 'mouse' без кавычки) ")
if method == "mouse":
  mouse_type = input('Введите клавишу на мышке (("left" - левая кнопка мыши) ("right" - правая кнопка мыши)')
if method == 'key':
  key_type = input('Введите клавишу: ')
# мышь
if method == 'mouse' and mouse_type == "left":
  while True:
    if keyboard.is_pressed(start_key):
      mouse.is_pressed(button = mouse_type)
      while True:
        time.sleep(0.01)
        mouse.double_click(button = mouse_type)
        if keyboard.is_pressed(stop_key):
          break


if method == 'mouse' and mouse_type == "right":
  while True:
    if keyboard.is_pressed(start_key):
      mouse.is_pressed(button = mouse_type)
      while True:
        time.sleep(0.01)
        mouse.double_click(button = mouse_type)
        if keyboard.is_pressed(stop_key):
          break

# клава

if method == 'key':
  while True:
    if keyboard.is_pressed(start_key):
      
      while True:
        time.sleep(0.01)
        pyautogui.press(key_type)
        if keyboard.is_pressed(stop_key):
          break
