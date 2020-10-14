import time
import random
import pygame
from pygame.locals import *
import math
import sys
import json




pygame.init()

# Window size.
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
xcoor = (position_x + r_width + int(rect_gap/2))
ycoor = 50
gravity = 1
velocity_b = 1


# Colors.
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

# List of predetermined rectangles.
with open("coordinates.json") as js:
    coordinates = json.load(js)




# Class for generating the ball.
class Ball:
    def __init__(self, screen, color, xcoor, ycoor, radius, ):
        self.screen = screen
        self.color = color
        self.xcoor = xcoor
        self.ycoor = ycoor
        self.radius = radius

    def draw(self, color, xcoor, ycoor, radius):
        pygame.draw.circle(screen, color, (xcoor, ycoor), radius)


# Class for rectangles.
class Rectangle:
    def __init__(self, screen, color, position_x, position_y, r_width,
    r_height):
        self.screen = screen
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.r_width = r_width
        self.r_height = r_height

    def draw(self, color, position_x, position_y, r_width, r_height):
        pygame.draw.rect(screen, dark_green, (position_x,
                                              position_y,
                                              r_width,
                                              r_height
                                              ))
        pygame.draw.rect(screen, dark_green, (rect_gap + r_width,
                                              position_y,
                                              screen_width -
                                              (rect_gap+r_width),
                                              r_height
                                              ))

# Counter of the while loop passes
passes = 0

item = coordinates[str(random.randint(1,1000))]

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(light_blue)
    time.sleep(0.005)

    # Constant movement of rectangles up.
    position_y -= velocity_r

    # Teleportation of the rectangles to the bottom
    if position_y < 0 - r_height:
        position_y = screen_height+radius

    # Inputs for movement
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        xcoor -= velocity_b
        if xcoor < 0 - radius: # Teleportation to the other side.
            xcoor = screen_width - radius
        if ycoor > position_y and ycoor < (position_y + r_height) and xcoor ==(position_x + r_width + radius): # Collisions from the left.
            xcoor += velocity_b

    if key[pygame.K_RIGHT]:
        xcoor += velocity_b
        if xcoor > screen_width + radius: # Teleportation to the other side.
            xcoor = 0
        if ycoor > position_y and ycoor < (position_y + r_height) and xcoor == (position_x - radius): # Collisions from the right.
            xcoor -= velocity_b

    # Collision objects.
    r_1 = pygame.Rect(position_x, position_y, r_width, r_height)
    r_2 = pygame.Rect(rect_gap+r_width, position_y,
                      screen_width-(rect_gap+r_width), r_height)
    b = pygame.Rect(xcoor, ycoor, radius, radius)

    # Collision detection.
    if r_1.colliderect(b) or r_2.colliderect(b):
        ycoor -= velocity_r
        if ycoor <= 0:
            break # Game over if ball goes of the screen.

    else:
        ycoor += gravity # Constant movement of the ball down.
        if ycoor >= screen_height + 20:
            ycoor = 0 - radius # Teleportation of the ball to the top

    # Generating the rectangle.
    
    Rectangle.draw(screen, dark_green, item["1_x"],
                    position_y, item["1_w"], item["1_h"])

    # Generating the baall.
    #Ball.draw(screen, white, xcoor, ycoor, radius)

    passes += 1
    """if passes%1000 == 0: # Acceleration, broken so far.
        velocity_r += 1
        velocity_b += 1
        gravity += 1"""

    pygame.display.update()

pygame.display.quit()
pygame.quit()
sys.exit()
