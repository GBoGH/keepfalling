import time
import random
import pygame
from pygame.locals import *
import math
import sys
import db

pygame.init()

clock = pygame.time.Clock()

def main_menu():
    ""

# Rectangles functions.
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
    for rectangle in rectangles:
        screen.blit(rectangle_surface, rectangle)

def rectangle_deletion(rectangles):
    for rectangle in rectangles:
        if rectangle.centery < -50:
            rectangles.remove(rectangle)

# Collisions functions.
def collisions(rectangles):
    for rectangle in rectangles:
        while ball_rect.colliderect(rectangle):
            gravity = 0
            ball_rect.centery -= velocity_r

# Score functions.
def score_counter(rectangles, score_add, score):
    
    for i in rectangles:
        if ball_rect.centery >= i.centery-10 and \
ball_rect.centery <= i.centery+10:
            print("True")
            score += score_add
            score_add = 0



def score_display():
    ""

# Countdown functions.
def countdown():
    if passes >= 50 and passes < 100:
        three = font.render("THREE", True, black)
        three_rect = three.get_rect(center=text_pos)
        screen.blit(three, three_rect)
    if passes >= 100 and passes < 150:
        two = font.render("TWO", True, black)
        two_rect = two.get_rect(center=text_pos)
        screen.blit(two, two_rect)
    if passes >= 150 and passes < 200:
        one = font.render("ONE", True, black)
        one_rect = one.get_rect(center=text_pos)
        screen.blit(one, one_rect)
    if passes >= 200 and passes < 250:
        start = font.render("START", True, black)
        start_rect = start.get_rect(center=text_pos)
        screen.blit(start, start_rect)
    if passes > 250:
        ball_rect.centery += gravity
    if passes < 250:
        move = font.render("MOVE  USING   ARROWS", True, black)
        move_rect = move.get_rect(midtop=(screen_width//2, 120))
        screen.blit(move, move_rect)

def game_over():
    game_over = font.render("GAME  OVER", True, black)
    game_over_rect = game_over.get_rect(center = text_pos)
    cont = font.render("PRESS  SPACE  TO  PlAY AGAIN", True, black)
    cont_rect = cont.get_rect(midtop=(screen_width//2, 150))
    screen.blit(game_over, game_over_rect)
    screen.blit(cont, cont_rect)


# Window size.
screen_width = 800
screen_height = 400

# Rectangle size and position.
rect_gap = 100
r_height = 10
velocity_r = 1


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

# Font.
font = pygame.font.Font("assets/ARCADECLASSIC.ttf", 50)
font_score = pygame.font.Font("assets/ARCADECLASSIC.ttf", 40)
font_game_over = pygame.font.Font("assets/ARCADECLASSIC.ttf", 60)
text_pos = (screen_width/2, 100)

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

center_surface = pygame.image.load("assets/empty.png")
center_surface = pygame.transform.scale(center_surface, (screen_width, 1))

rectangles = []
rectangles.extend(rectangle_generation())

# ! Score is still not working !
score = 0
score_add = 1

passes = 0


# game loop
game_running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

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

    if key[pygame.K_SPACE] and game_running == False:
        rectangles.clear()
        rectangles.extend(rectangle_generation())
        ball_rect.center = (screen_width/2, 50)
        passes = 0
        game_running = True

    screen.fill(light_blue)
    clock.tick(120)

    if game_running:
        countdown()

        if rectangles[-1].centery <= 350:
            rectangles.extend(rectangle_generation())

        rectangles = rectangle_movement(rectangles)

        rectangle_drawing(rectangles)
        
        rectangle_deletion(rectangles)

        screen.blit(ball_surface, ball_rect)

        collisions(rectangles)

        score_counter(rectangles, score_add, score)

        if ball_rect.centery > screen_height+20:
            ball_rect.centery = -20
        if ball_rect.centery < -20:
            game_running = False

    elif not game_running:
        game_over()
        break

    pygame.display.update()
    passes += 1
print(score)