import mouse
import keyboard
import time

start_key = input('Клавиша старта: ')
stop_key = input('Клавиша остановки: ')

while True:
  if keyboard.is_pressed(start_key):
    mouse.is_pressed(button = 'left')
    while True:
      time.sleep(0.01)
      mouse.double_click(button = 'left')
      if keyboard.is_pressed(stop_key):
        break