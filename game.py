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

ball = pygame.draw.circle(screen, white, (xcoor, ycoor), radius)



def ballmovement():
    if event.type == pygame.KEYDOWN:
        if event.type == pygame.K_LEFT:
            coorchange = 50
        if event.type == pygame.K_RIGHT:
            coorchange = -50
    if event.type == pygame.KEYUP:
        if event.type == K_LEFT or event.type == pygame.K_RIGHT:
            coorchange = 0
    print(coorchange)
    print(xcoor)

    


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            xcoor -= 5
        if key[pygame.K_RIGHT]:
            xcoor += 5
        """if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                coorchange = -50
            if event.type == pygame.K_RIGHT:
                coorchange = 50
        if event.type == pygame.KEYUP:
            if event.type == K_LEFT or event.type == pygame.K_RIGHT:
                coorchange = 0
            """
    xcoor += coorchange
    if xcoor <= 0:
        xcoor = 0
    elif xcoor >= 800:
        xcoor = 800
    pygame.display.update()
