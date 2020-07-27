# Jakub Feik
# 21/05/2020

# imports
import time
import random
import pygame
from pygame.locals import *
import math
import sys

pygame.init()

# window size
screen_width = 800
screen_height = 400

# ball position and size
radius = 10
xcoor = 100
ycoor = 100
coorchange = 0

# colors
white = (255, 255, 255,)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (78, 231, 245)
dark_green = (37, 125, 0)

# Icon.
icon = pygame.image.load("ball.png")

# Window.
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keep Falling")
screen.fill(light_blue)
pygame.display.set_icon(icon)


class Ball:
    def __init__(self, screen, color, xcoor, ycoor, radius):
        self.screen = screen
        self.color = color
        self.xcoor = xcoor
        self.ycoor = ycoor
        self.radius = radius

    def draw(self, color, xcoor, ycoor, radius):
        pygame.draw.circle(screen, color, (xcoor, ycoor), radius)


#Ball.draw(screen, white, xcoor, ycoor, radius)


position_x = 150
position_y = 150
r_height = 60
r_width = 420

velocity_b = 1
t1_b = time.time()

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t2_b = time.time()
    dt_b = (t2_b - t1_b)
    t1_b = t2_b
    screen.fill(black)
    pygame.draw.rect(screen, dark_green, (position_x,
                                          position_y, r_width, r_height))
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        xcoor -= velocity_b
        if xcoor < 0:
            xcoor = screen_width
        if ycoor > position_y and ycoor < (position_y + r_height) and xcoor == (position_x + r_width + radius):
            xcoor += 1
    if key[pygame.K_RIGHT]:
        xcoor += velocity_b
        if xcoor > screen_width:
            xcoor = 0
        if ycoor > position_y and ycoor < (position_y + r_height) and xcoor == (position_x - radius):
            xcoor -= 1
        
    if key[pygame.K_UP]:
        ycoor -= velocity_b
        if ycoor < 0:
            ycoor = screen_height
        if ycoor == (position_y+r_height+radius) and xcoor >= position_x and xcoor <= (position_x + r_width):
            ycoor += 1
    if key[pygame.K_DOWN]:
        ycoor += velocity_b
        if ycoor > screen_height:
            ycoor = 0
        if ycoor == (position_y - radius) and xcoor >= position_x and xcoor <= (position_x + r_width):
            ycoor -= 1

    Ball.draw(screen, white, xcoor, ycoor, radius)

    pygame.display.update()

pygame.quit()
