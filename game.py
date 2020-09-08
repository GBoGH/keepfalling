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

# Rectangle size and position.
position_x = random.randint(0, screen_width-150)
position_y = random.randint(0, screen_height-50)
r_width = random.randint(150, (screen_width - position_x))
r_height = 10
rect_gap = 50
velocity_r = 1

# Ball properties.
radius = 10
xcoor = random.choice(range((radius + 2), screen_width-r_width))
ycoor = 20
gravity = 1
velocity_b = 1


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
    def __init__(self, screen, color, xcoor, ycoor, radius, ):
        self.screen = screen
        self.color = color
        self.xcoor = xcoor
        self.ycoor = ycoor
        self.radius = radius

    def draw(self, color, xcoor, ycoor, radius):
        pygame.draw.circle(screen, color, (xcoor, ycoor), radius)
    
    """def left(self, velocity_b, radius, position_x, position_y, r_width, r_height):
        xcoor -= velocity_b
        if xcoor < 0:
            xcoor = screen_width
        if ycoor > position_y and ycoor < (position_y + r_height) and xcoor == (position_x + r_width + radius):
            xcoor += velocity_b
        
    def right(self, xcoor, velocity_b, radius, position_x, position_y, r_height, r_width):"""
    




class Rectangle:
    def __init__(self, screen, color, position_x, position_y, r_width, r_height):
        self.screen = screen
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.r_width = r_width
        self.r_height = r_height

    def draw(self, color, position_x, position_y, r_width, r_height):
        pygame.draw.rect(screen, dark_green, (position_x,
                                              position_y, r_width, r_height))


# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(light_blue)
    time.sleep(0.005)
    position_y -= velocity_r

    if position_y < -r_height:
        position_y = screen_height+radius

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        xcoor -= velocity_b
        if xcoor < 0:
            xcoor = screen_width
        if ycoor > position_y and ycoor < (position_y + r_height) and xcoor == (position_x + r_width + radius):
            xcoor += velocity_b
        

    if key[pygame.K_RIGHT]:
        xcoor += velocity_b
        if xcoor > screen_width:
            xcoor = 0
        if ycoor > position_y and ycoor < (position_y + r_height) and xcoor == (position_x - radius):
            xcoor -= velocity_b

    if key[pygame.K_DOWN]:
        if ycoor == (position_y - radius) and xcoor >= position_x and xcoor <= (position_x + r_width):
            ycoor -= velocity_r
        else:
            ycoor += velocity_b
        if ycoor > screen_height:
            ycoor = 0

    if ycoor > screen_height:
        ycoor = 0

    if ycoor == (position_y+r_height+radius) and xcoor >= position_x and xcoor <= (position_x + r_width):
        ycoor += velocity_b

    if ycoor == (position_y - radius) and xcoor >= position_x and xcoor <= (position_x + r_width):
        gravity = 0
        ycoor -= velocity_r
        if ycoor < 0:
            ycoor = screen_height

    elif ycoor == (position_y - radius) and xcoor <= position_x or xcoor >= (position_x + r_width):
        gravity = 1

    """while ycoor == (position_y - radius) and xcoor >= position_x and xcoor <= (position_x + r_width):
        gravity = 0
        ycoor -= velocity_r
        if ycoor < 0:
            ycoor = screen_height"""

    ycoor += gravity
    #print("position_x, position_y: (%d,%d) \nxcoor, ycoor: (%d,%d)" % (position_x,position_y, xcoor, ycoor))
    
    Rectangle.draw(screen, dark_green, position_x, position_y, r_width, r_height)
    Ball.draw(screen, white, xcoor, ycoor, radius)

    pygame.display.update()
pygame.quit()
