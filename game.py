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
    about_surface = pygame.image.load("assets/about.png")
    about_surface = pygame.transform.scale(about_surface, (30,30))
    about = about_surface.get_rect(bottomleft=(10,screen_height-10))
    screen.blit(about_surface, about)

# Rectangles functions.
def rectangle_generation():
    left_length = random.randint(150, (screen_width-rect_gap-100))
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
        while ball.colliderect(rectangle):
            gravity = 0
            ball.centery -= velocity_r

# Score functions.
def score_counter(rectangles):
    global score, score_add
    for rectangle in rectangles:
        if rectangle.centery-10 <= ball.centery <= rectangle.centery+10 and score_add:
            score += 1
            score_add = False
        if rectangle.centery + 20 < ball.centery < rectangle.centery + 40:
            score_add = True
        
def score_display(score):
    score_surface = font_score.render(str(int(score)), True, white)
    score = score_surface.get_rect(topright=(screen_width-5, 5))
    screen.blit(score_surface, score)

def score_record():
    global user_name, score
    user_name = "'" + user_name + "'"
    db.insert("score", user_name, score,)

def five_best():
    names = db.bestx("score", 5)
    y = screen_height-5
    for i in reversed(names):
        name_surface = font_bestof.render((i),True, black)
        name = name_surface.get_rect(bottomright=(screen_width-5,y))
        screen.blit(name_surface, name)
        y -= 20

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
        ball.centery += gravity
    if passes < 250:
        move = font.render("MOVE  USING   ARROWS", True, black)
        move_rect = move.get_rect(midtop=(screen_width//2, 120))
        screen.blit(move, move_rect)

def game_over():
    global user_name, score

    player_input()

    game_over = font.render("GAME  OVER", True, black)
    game_over_rect = game_over.get_rect(midtop=(screen_width//2, 10))
    screen.blit(game_over, game_over_rect)

    score_surface = font.render(f"YOUR  SCORE  WAS {score}",True,black)
    your_score = score_surface.get_rect(midtop=(screen_width//2,40))
    screen.blit(score_surface,your_score)
    
    typing_surface = font.render("START  TYPING  TO  FILL IN", True, black)
    typing = typing_surface.get_rect(midtop=(screen_width//2, 110))
    screen.blit(typing_surface, typing)

    enter_name = font.render("YOUR  NAME  AND PRESS", True, black)
    enter = enter_name.get_rect(midtop=(screen_width//2,140))
    screen.blit(enter_name, enter)

    submit_name = font.render("ENTER  TO  SUBMIT  YOUR  SCORE", True, black)
    submit =  submit_name.get_rect(midtop=(screen_width//2,170))
    screen.blit(submit_name,submit)

    name_surface = font.render(user_name, True, black)
    name = name_surface.get_rect(midtop=(screen_width//2,240))
    screen.blit(name_surface,name)

    cont = font.render("PRESS  SPACE  TO  PLAY AGAIN", True, black)
    cont_rect = cont.get_rect(midtop=(screen_width//2, 335))
    screen.blit(cont, cont_rect)

def reset():
    global game_running
    screen.fill(light_blue)
    rectangles.clear()
    rectangles.extend(rectangle_generation())
    ball.center = (screen_width/2, 50)
    passes = 0
    score = 0
    game_running = True

def player_input():
    global user_name, name_entered
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and not name_entered:
            if event.key == K_BACKSPACE:
                    user_name = user_name[:-1]
            elif event.key == K_RETURN:
                score_record()
                user_name = "SCORE SUBMITTED"
                name_entered = True
            elif event.key == K_SPACE and name_entered:
                reset()
            else:
                user_name += event.unicode
        

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
font_bestof = pygame.font.Font("assets/ARCADECLASSIC.ttf", 20)
text_pos = (screen_width/2, 100)

# Window.
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keep Falling")
screen.fill(light_blue)
pygame.display.set_icon(icon)

# Ball.
ball_surface = pygame.image.load("assets/ball.png")
ball_surface = pygame.transform.scale(ball_surface, (20, 20))
ball = ball_surface.get_rect(center=(screen_width/2, 50))


rectangle_surface = pygame.image.load("assets/rectangle.png")
rectangle_surface = pygame.transform.scale(rectangle_surface, (screen_width, r_height))


rectangles = []
rectangles.extend(rectangle_generation())

score = 0
score_add = True

passes = 0

user_name = ""

# game loop
menu = True
game_running = False
name_entered = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    screen.fill(light_blue)
    clock.tick(120)
    key = pygame.key.get_pressed()
    
    if menu:
        main_menu()
        five_best()
        if key[K_SPACE]:
            game_running = True
            menu = False
            passes = 0

    if key[K_LEFT]:
        ball.centerx -= velocity_b
        if ball.centerx < -20:
            ball.centerx = screen_width + 20

    if key[K_RIGHT]:
        ball.centerx += velocity_b
        if ball.centerx > screen_width + 20:
            ball.centerx = -20

    if game_running:
        countdown()

        if rectangles[-1].centery <= screen_height-50:
            rectangles.extend(rectangle_generation())

        rectangles = rectangle_movement(rectangles)

        rectangle_drawing(rectangles)
        
        rectangle_deletion(rectangles)

        screen.blit(ball_surface, ball)

        collisions(rectangles)

        score_counter(rectangles)

        score_display(score)


        if ball.centery > screen_height+20:
            ball.centery = -20
        if ball.centery < -20:
            game_running = False

    
    elif not game_running and not menu:
        game_over()

    pygame.display.update()
    passes += 1