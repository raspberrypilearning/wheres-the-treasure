#!/bin/python3

from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

# आम्हाला स्वारस्य असलेल्या कृती परत करा
def wait_for_move():
  while True:
    e = sense.stick.wait_for_event()
    if e.action != ACTION_RELEASED:
      return e

R = [255, 0, 0]  # लाल
Y = [255, 255, 0] # पिवळा
G = [0, 255, 0] # हिरवा
W = [255, 255, 255] # पांढरा

score = 0

for turns in range(10):
  
  coinx = randint(0,7)
  coiny = randint(0,7)
  print(coinx, coiny)
    
  sense.set_pixel(coinx, coiny, Y)
  sleep(2)
  sense.clear()
    
  x = randint(0,7)
  y = randint(0,7)
  sense.set_pixel(x, y, W)
    
  while True:
  
    e = wait_for_move()
    
    if e.direction == DIRECTION_MIDDLE:
      
      if x == coinx and y == coiny:
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
  
  
