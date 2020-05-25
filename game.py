#Jakub Feik
#21/05/2020

#imports
import time
import random
import pygame
from pygame.locals import *
import math
import sys


pygame.init()

#window size
screen_width = 800
screen_height = 400

#rectangle size and position
xpos = random.choice(range(screen_width))
ypos = 50
rect_width = random.choice(range(screen_width-50))
rect_height = 10
rect_gap = 50

#ball position and size
radius = 10
"""xcoor = random.choice(range(12,rect_width))
ycoor = ypos - radius"""
xcoor = 100
ycoor = 100


#colors
white = (255,255,255,)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue= (0,0,255)
light_blue = (78, 231, 245)
dark_green = (37, 125, 0)


pressed = pygame.key.get_pressed()
right = pressed[pygame.K_RIGHT]
left = pressed[pygame.K_LEFT]
up = pressed[pygame.K_UP]
down = pressed[pygame.K_DOWN]

#miscellaneous
state = True
icon = pygame.image.load("ball.png")

#windowaa
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Keep Falling")
screen.fill(light_blue)
pygame.display.set_icon(icon)


 


def ball_movement():
    global ycoor
    global pressed
    pygame.draw.circle(screen, white, (xcoor, ycoor), radius)
    if pressed[pygame.K_RIGHT]:
            ycoor += 50



#game loop
while state:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    ball_movement()
    pygame.display.update()

