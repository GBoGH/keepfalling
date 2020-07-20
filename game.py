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

# Rectangle Class.
class Rectangle:
    def __init__(self, screen, color, xpos, ypos, width, height):
        self.screen = screen
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height

    # Draw method.
    def draw(screen, color, xpos, ypos, width, height):
        pygame.draw.rect(screen, color, (xpos, ypos, width, height))
        pygame.draw.rect(screen, color, (width + rect_gap, ypos,
                                         screen_width - (width + rect_gap), height))


# Ball Class.
class Ball:
    def __init__(self, screen, color, xcoor, ycoor, radius):
        self.screen = screen
        self.color = color
        self.xcoor = xcoor
        self.ycoor = ycoor
        self.radius = radius

    # Draw method.
    def draw(screen, color, xcoor, ycoor, radius):
        pygame.draw.circle(screen, color, (xcoor, ycoor), radius)

# Rectangle drawing.
for i in range(screen_height):
    Rectangle.draw(screen, dark_green, xpos, ypos, rect_width, rect_height)
    ypos += 50
    rect_width = rect_width = random.choice(range(screen_width - 50))

# Ball drawing.
Ball.draw(screen, white, xcoor, ycoor, radius)
 

# Game Loop.
state = True
while state:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()
