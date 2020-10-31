import time
import random
import pygame
from pygame.locals import *
import math
import sys
import json

pygame.init()
clock = pygame.time.Clock()

# Window size.
screen_width = 800
screen_height = 400

# Rectangle size and position.
position_x = 0
position_y = 100
rect_gap = 100
r_width = random.randint(150, (screen_width-rect_gap-100))
r_height = 10
velocity_r = 1

# Ball properties.
radius = 10
xcoor = (position_x + r_width + int(rect_gap/2))
ycoor = 50
gravity = 1
velocity_b = 10

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


collisions = []

ball_surface = pygame.image.load("assets/ball.png")
ball_surface = pygame.transform.scale(ball_surface, (20, 20))
ball_rect = ball_surface.get_rect(center=(xcoor, ycoor))

ball_falling = 10
# Counter of the while loop passes
passes = 0

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(light_blue)
    clock.tick(120)

    # Constant movement of rectangles up.
    position_y -= velocity_r

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



    screen.blit(ball_surface, ball_rect)

    ball_rect.centery += gravity

    if ball_rect.centery > screen_height+20:
        ball_rect.centery = -20

    passes += 1

    pygame.display.update()

pygame.display.quit()
pygame.quit()
sys.exit()
