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
position_x = 0
position_y = 50
rect_gap = 100
r_width = random.randint(150, (screen_width-rect_gap-100))
r_height = 10
velocity_r = 1

# Ball properties.
radius = 10
xcoor = random.randint((radius + 2), screen_width-r_width)
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
        pygame.draw.rect(screen, dark_green, (rect_gap+r_width,
                                              position_y, screen_width-(rect_gap+r_width), r_height))


# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(light_blue)
    time.sleep(0.005)
    position_y -= velocity_r

    if position_y < 0 - r_height:
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

    r_1 = pygame.Rect(position_x, position_y, r_width, r_height)
    r_2 = pygame.Rect(rect_gap+r_width, position_y,
                      screen_width-(rect_gap+r_width), r_height)
    b = pygame.Rect(xcoor, ycoor, radius, radius)
    if r_1.colliderect(b) or r_2.colliderect(b):
        ycoor -= velocity_r
        if ycoor <= 0:
            ycoor = screen_height + radius
            while ycoor != screen_height-radius:
                ycoor -= velocity_r
    else:
        ycoor += gravity
        if ycoor >= screen_height + 20:
            ycoor = 0 - radius

    Rectangle.draw(screen, dark_green, position_x,
                   position_y, r_width, r_height)
    Ball.draw(screen, white, xcoor, ycoor, radius)

    pygame.display.update()
pygame.quit()
