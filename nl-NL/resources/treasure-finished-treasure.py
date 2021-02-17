#!/bin/python3

from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

# Geef gewoon de acties terug waarin we geïnteresseerd zijn
def wacht_op_zet():
  while True:
    e = sense.stick.wait_for_event()
    if e.action != ACTION_RELEASED:
      return e

R = [255, 0, 0]  # rood
Y = [255, 255, 0] # geel
G = [0, 255, 0] # groen
W = [255, 255, 255] # wit

score = 0

for beurten in range(10):
  
  muntx = randint(0,7)
  munty = randint(0,7)
  print(muntx, munty)
    
  sense.set_pixel(muntx, munty, Y)
  sleep(2)
  sense.clear()
    
  x = randint(0,7)
  y = randint(0,7)
  sense.set_pixel(x, y, W)
    
  while True:
  
    e = wacht_op_zet()
    
    if e.direction == DIRECTION_MIDDLE:
      
      if x == muntx and y == munty:
        sense.set_pixel(x, y, G)
        score += 1
      else:
        sense.set_pixel(x, y, R)
      
      sleep(1)
      sense.clear()
      break;
  
    sense.clear()
      
    if e.direction ==  DIRECTION_UP and y > 0:
      y = y - 1
      
    elif e.direction ==  DIRECTION_DOWN and y < 7:
      y = y + 1

    elif e.direction ==  DIRECTION_LEFT and x > 0:
      x = x - 1

    elif e.direction ==  DIRECTION_RIGHT and x < 7:
      x = x + 1

    sense.set_pixel(x, y, W)
      
sense.show_message("Score: " + str(score))       
  
  
