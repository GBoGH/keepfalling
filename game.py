# Jakub Feik
# 21/05/2020

# Imports.
import time
import random
import math
import sys

import pygame

from pygame.locals import *

pygame.init()

# Window size setting
screen_width = 800
screen_height = 400

# Rectangle size and position.
xpos = 0
ypos = 50
rect_width = random.choice(range(screen_width - 50))
rect_height = 10
rect_gap = 50

# Ball position and size.
radius = 10
xcoor = random.choice(range(12, rect_width))
ycoor = ypos - radius

# Color values.
white = (255, 255, 255,)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (78, 231, 245)
dark_green = (37, 125, 0)


# Window icon.
icon = pygame.image.load("ball.png")

# Window parametres.
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keep Falling")
screen.fill(light_blue)
pygame.display.set_icon(icon)

# Rectangle generation.
for i in range(screen_height):
    pygame.draw.rect(screen, dark_green, (xpos, ypos, rect_width, rect_height))
    pygame.draw.rect(screen, dark_green, (rect_width + rect_gap, ypos,
                                          screen_width - (rect_width + rect_gap), rect_height))
    ypos += 50
    rect_width = random.choice(range(screen_width - 50))


# Ball drawing.
pygame.draw.circle(screen, white, (xcoor, ycoor), radius)

# Game Loop.
state = True
while state:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()
