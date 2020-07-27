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





# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        xcoor -= 1
        if xcoor < 0:
            xcoor = screen_width
    if key[pygame.K_RIGHT]:
        xcoor += 1
        if xcoor > screen_width:
            xcoor = 0
    if key[pygame.K_UP]:
        ycoor -= 1
        if ycoor < 0:
            ycoor = screen_height
    if key[pygame.K_DOWN]:
        ycoor += 1
        if ycoor > screen_height:
            ycoor = 0

    screen.fill(black)
    Ball.draw(screen, white, xcoor, ycoor, radius)
    pygame.display.update()

pygame.quit()
