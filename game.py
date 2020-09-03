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

# Window size.
screen_width = 800
screen_height = 400

# Rectangle related variables.
position_x = 100
position_y = 300
r_width = random.choice(range(150, screen_width - 50))
r_height = 10
rect_gap = 50
velocity_r = 1

# Ball related variables.
radius = 10
xcoor = random.choice(range((radius + 2), screen_width-r_width))
ycoor = 20
gravity = 1
velocity_b = 1

# Color variables.
white = (255, 255, 255,)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (78, 231, 245)
dark_green = (37, 125, 0)

# Icon.
icon = pygame.image.load("ball.png")

# Window parametres.
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keep Falling")
screen.fill(light_blue)
pygame.display.set_icon(icon)


# Class for rectangle generation.
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


# Call for ball generation.
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


# Game Loop.
state = True
while state:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill(light_blue)

    key = pygame.key.get_pressed()

    # Movement to the right and related boundaries.
    if key[pygame.K_LEFT]:
        xcoor -= velocity_b
        if xcoor < 0:
            xcoor = screen_width
        if ycoor > position_y and ycoor < (position_y + r_height) and xcoor == (position_x + r_width + radius):
            xcoor += velocity_b

    # Movement to the right and related boundaries
    if key[pygame.K_RIGHT]:
        xcoor += velocity_b
        if xcoor > screen_width:
            xcoor = 0
        if ycoor > position_y and ycoor < (position_y + r_height) and xcoor == (position_x - radius):
            xcoor -= velocity_b

    # Teleportation to the top.
    if ycoor > screen_height:
        ycoor = 0
    # Collision with the rectangle.
    if ycoor == (position_y+r_height+radius) and xcoor >= position_x and xcoor <= (position_x + r_width):
        ycoor += velocity_b
    if ycoor == (position_y - radius) and xcoor >= position_x and xcoor <= (position_x + r_width):
        ycoor -= velocity_b
        position_y += velocity_b

    # Constant gravity.
    ycoor += gravity

    # Ball generation.
    Ball.draw(screen, white, xcoor, ycoor, radius)
    
    # Rectangle generation.
    for i in range(screen_height):
        Rectangle.draw(screen, dark_green, position_x,
                       position_y, r_width, r_height)
        position_y += rect_gap
        rect_width = rect_width = random.choice(range(screen_width - 50))

    pygame.display.update()
pygame.quit()
