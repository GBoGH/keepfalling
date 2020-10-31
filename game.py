import time
import random
import pygame
from pygame.locals import *
import math
import sys
import json
import os

os.system("cls")

pygame.init()
clock = pygame.time.Clock()


def rectangle_generation():
    left_length = random.choice(widths)
    left_rectangle = rectangle_surface.get_rect(topright=(left_length, 450))
    right_rectangle = rectangle_surface.get_rect(
        topleft=(left_length+rect_gap, 450))
    return left_rectangle, right_rectangle


def rectangle_movement(rectangles):
    for rectangle in rectangles:
        rectangle.centery -= velocity_r
    return rectangles


def rectangle_drawing(rectangles):
    for i in rectangles:
            screen.blit(rectangle_surface, i)


def rectangle_deletion(rectangles):
    for rectangle in rectangles:
        if rectangle.centery < -50:
            rectangles.remove(rectangle)


def collisions(rectangles):
    for rectangle in rectangles:
        while ball_rect.colliderect(rectangle):
            gravity = 0
            ball_rect.centery -= velocity_r


# Window size.
screen_width = 800
screen_height = 400

# Rectangle size and position.
rect_gap = 100
r_height = 10
velocity_r = 4

# Ball properties.
radius = 10
gravity = 1
velocity_b = 5

# Colors.
white = (255, 255, 255,)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (78, 231, 245)
dark_green = (37, 125, 0)

# Icon.
icon = pygame.image.load("assets/icon.png")

# Window.
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keep Falling")
screen.fill(light_blue)
pygame.display.set_icon(icon)

# Ball.
ball_surface = pygame.image.load("assets/ball.png")
ball_surface = pygame.transform.scale(ball_surface, (20, 20))
ball_rect = ball_surface.get_rect(center=(screen_width/2, 50))

# Rectangles.
widths = []
for i in range(1001):
    x = random.randint(150, (screen_width-rect_gap-100))
    widths.append(x)

rectangle_surface = pygame.image.load("assets/rectangle.png")
rectangle_surface = pygame.transform.scale(rectangle_surface, (1000, r_height))
rectangles = []
rectangles.extend(rectangle_generation())


passes = 0

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if rectangles[-1].centery < 350:
        rectangles.extend(rectangle_generation())

    screen.fill(light_blue)
    clock.tick(120)

    # Inputs for movement
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        ball_rect.centerx -= velocity_b
        if ball_rect.centerx < -20:
            ball_rect.centerx = screen_width + 20

    if key[pygame.K_RIGHT]:
        ball_rect.centerx += velocity_b
        if ball_rect.centerx > screen_width + 20:
            ball_rect.centerx = -20

    rectangles = rectangle_movement(rectangles)
    rectangle_drawing(rectangles)

    screen.blit(ball_surface, ball_rect)
    collisions(rectangles)
    rectangle_deletion(rectangles)
    print(rectangles)


    if passes < 150:
        pass
    else:
        ball_rect.centery += gravity

    #if ball_rect.centery > screen_height+20:
        #ball_rect.centery = -20
    #if ball_rect.centery < -20:
        #break

    pygame.display.update()

    passes += 1
    #print(passes)

pygame.display.quit()
pygame.quit()
sys.exit()
