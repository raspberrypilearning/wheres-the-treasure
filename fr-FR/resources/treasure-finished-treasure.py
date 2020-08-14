#!/bin/python3

from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

# On renvoie seulement les actions qui nous intéressent
def attendre_mouvement():
  while True:
    e = sense.stick.attendre_evenement()
    if e.action != ACTION_RELEASED:
      return e

R = [255, 0, 0]  # rouge
J = [255, 255, 0] # jaune
V = [0, 255, 0] # vert
B = [255, 255, 255] # blanc

score = 0

for tours in range(10):
  
  piecex = randint(0,7)
  piecey = randint(0,7)
  print(piecex, piecey)
    
  sense.set_pixel(piecex, piecey, J)
  sleep(2)
  sense.clear()
    
  x = randint(0,7)
  y = randint(0,7)
  sense.set_pixel(x, y, B)
    
  while True:
  
    e = attendre_mouvement()
    
    if e.direction == DIRECTION_MIDDLE:
      
      if x == piecex and y == piecey:
        sense.set_pixel(x, y, V)
        score += 1
      else:
        sense.set_pixel(x, y, R)
      
      sleep(1)
      sense.clear()
      break;
  
    sense.clear()
      
    if e.direction == DIRECTION_UP and y > 0:
      y = y - 1
      
    elif e.direction ==  DIRECTION_DOWN and y < 7:
      y = y + 1

    elif e.direction ==  DIRECTION_LEFT and x > 0:
      x = x - 1

    elif e.direction == DIRECTION_RIGHT and x <7:
      x = x + 1

    sense.set_pixel(x, y, B)
      
sense.show_message("Score : " + str(score))       
  
  
