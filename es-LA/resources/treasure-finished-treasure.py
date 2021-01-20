#!/bin/python3

from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

# Solo devuelve las acciones que nos interesan
def wait_for_move():
  while True:
    e = sense.stick.wait_for_event()
    if e.action != ACTION_RELEASED:
      return e

R = [255, 0, 0]  # rojo
A = [255, 255, 0] # amarillo
V = [0, 255, 0] # verde
B = [255, 255, 255] # blanco

puntuacion = 0

for turns in range(10):
  
  monedax = randint(0,7)
  moneday = randint(0,7)
  print(monedax, moneday)
    
  sense.set_pixel(monedax, moneday, A)
  sleep(2)
  sense.clear()
    
  x = randint(0, 7)
  y = randint(0, 7)
  sense.set_pixel(x, y, B)
    
  while True:
  
    e = wait_for_move()
    
    if e.direction == DIRECTION_MIDDLE:
      
      if x == monedax e y == moneday:
        sense.set_pixel(x, y, V)
        puntuacion += 1
      else:
        sense.set_pixel(x, y, R)
      
      sleep(1)
      sense.clear()
      break;
  
    sense.clear()
      
    if e.direction ==  DIRECTION_UP and y > 0:
      y = y - 1
      
    elif e.direction == DIRECTION_DOWN and y < 7:
      y = y + 1

    elif e.direction ==  DIRECTION_LEFT and x > 0:
      x = x - 1

    elif e.direction ==  DIRECTION_RIGHT and x < 7:
      x = x + 1

    sense.set_pixel(x, y, B)
      
sense.show_message("Puntuacion: " + str(puntuacion))       
  
  
