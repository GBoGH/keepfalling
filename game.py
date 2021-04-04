import random
import sys

import pygame
from pygame.locals import *

import scores
import pictures

# Initializing Pygame.
pygame.init()

# Function to render main menu screen and everything on it.
def main_menu():
    learn_more = font_15.render("LEARN  MORE  AT:", True, black)
    learn_more_rect = learn_more.get_rect(bottomleft=(10, screen_height-25))
    screen.blit(learn_more, learn_more_rect)

    address = font_15.render("GITHUB.COM/GBOGH/KEEPFALLING", True, black)
    adress_rect = address.get_rect(bottomleft=(10, screen_height-10))
    screen.blit(address, adress_rect)

    keepfalling = font_85.render("KEEP  FALLING", True, black)
    keepfalling_rect = keepfalling.get_rect(midtop=(screen_width//2, 50))
    screen.blit(keepfalling, keepfalling_rect)

    space = font_25.render("PRESS  SPACE  TO  PLAY.", True, black)
    space_rect = space.get_rect(midtop=(screen_width//2, 200))
    screen.blit(space, space_rect)


# Set of fuctions responsible for rectangle mechanics.

# Function to create two triangles with random legth.
def rectangle_generation():
    left_length = random.randint(150, (screen_width-rect_gap-100))
    # Rectangle on the left side with random length.
    left_rectangle = rectangle_surface.get_rect(topright=(left_length, 450))
    # Supplmenting rectangle on the right.
    right_rectangle = rectangle_surface.get_rect(
        topleft=(left_length+rect_gap, 450))
    return left_rectangle, right_rectangle

# Function to change y coordinate of every rectangle in the list of rectangles.
def rectangle_movement(rectangles):
    for rectangle in rectangles:
        # All rectangle's y coordinate is lowered therefore rectangles move up.
        rectangle.centery -= velocity_r
    return rectangles

# Function which draws every rectangle in the list on the screen.
def rectangle_drawing(rectangles):
    for rectangle in rectangles:
        screen.blit(rectangle_surface, rectangle)

# Function which deletes the rectangles if they are of the screen.
def rectangle_deletion(rectangles):
    for rectangle in rectangles:
        if rectangle.centery < -50:
            # If the rectangle is to far up, it gets delted.
            rectangles.remove(rectangle)


# Function which checks for collisions between the ball and rectangles.
def collisions(rectangles):
    for rectangle in rectangles:
        while ball_rect.colliderect(rectangle):
            # If the ball touches the rectangle, it moves up with it.
            ball_rect.centery -= velocity_r


# Set of functions responsible for score counting.
# Function which counts the score.
def score_counter(rectangles):
    global score, score_add, ticks
    for rectangle in rectangles:
        # Coordinate check determines whether ball passed trough floor.
        if rectangle.centery-10 <= ball_rect.centery <= rectangle.centery+10 and score_add:
            score += 1
            # With each score point, one tick is added to speed up the game.
            ticks += 1
            # Condition to add only one point to score.
            score_add = False
        # If ball is  below the rectangle, score counting is recovered.
        if rectangle.centery + 20 < ball_rect.centery < rectangle.centery + 40:
            score_add = True

# Function which renders the score on the screen.
def score_display(score):
    score = font_35.render(str(int(score)), True, white)
    score_rect = score.get_rect(topright=(screen_width-5, 5))
    screen.blit(score, score_rect)


# Function to display five best scores.
def five_best():
    score_dict = scores.dictionary()
    # Getting the values from db module.
    names = scores.bestx(score_dict, 5)
    y = screen_height-5
    # Displaying those scores onto the screen.
    for i in reversed(names):
        name = font_15.render((i), True, black)
        name_rect = name.get_rect(bottomright=(screen_width-5, y))
        screen.blit(name, name_rect)
        # Moving text up with each line.
        y -= 20


# Function for the initial coundown.
def countdown():
    # With every pass vo the while loop variable passes increase by one.
    # Ussing variable passes as a kind of timer.
    if passes >= 50 and passes < 100:
        three = font_45.render("THREE", True, black)
        three_rect = three.get_rect(center=text_pos)
        screen.blit(three, three_rect)

    if passes >= 100 and passes < 150:
        two = font_45.render("TWO", True, black)
        two_rect = two.get_rect(center=text_pos)
        screen.blit(two, two_rect)

    if passes >= 150 and passes < 200:
        one = font_45.render("ONE", True, black)
        one_rect = one.get_rect(center=text_pos)
        screen.blit(one, one_rect)

    if passes >= 200 and passes < 250:
        start = font_45.render("START", True, black)
        start_rect = start.get_rect(center=text_pos)
        screen.blit(start, start_rect)

    # When passes reaches 250, the game starts and the ball starts falling.
    if passes > 250:
        ball_rect.centery += gravity

    # Displaying how to move during the whole countdown-
    if passes < 250:
        move = font_45.render("MOVE  USING   ARROWS", True, black)
        move_rect = move.get_rect(midtop=(screen_width//2, 120))
        screen.blit(move, move_rect)


# Function to display game over screen.
def game_over():
    global score

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    # Next six code blocks, jut display text on the game over screen.
    # Pygame cannot display multiline text, therefore it is split.
    game_over = font_45.render("GAME  OVER.", True, black)
    game_over_rect = game_over.get_rect(midtop=(screen_width//2, 10))
    screen.blit(game_over, game_over_rect)

    your_score = font_45.render(f"YOUR  SCORE  WAS {score}", True, black)
    your_score_rect = your_score.get_rect(midtop=(screen_width//2, 45))
    screen.blit(your_score, your_score_rect)

    to_submit = font_45.render("TO  SUBMIT  YOUR  SCORE", True, black)
    to_submit_rect = to_submit.get_rect(midtop=(screen_width//2, 130))
    screen.blit(to_submit, to_submit_rect)

    enter = font_45.render("REFER  TO  SUBMITTING", True, black)
    enter_rect = enter.get_rect(midtop=(screen_width//2, 165))
    screen.blit(enter, enter_rect)

    submit = font_45.render("GUIDE  ON  MY GITHUB", True, black)
    submit_rect = submit.get_rect(midtop=(screen_width//2, 200))
    screen.blit(submit, submit_rect)

    cont = font_45.render("PRESS  SPACE  TO  PLAY AGAIN.", True, black)
    cont_rect = cont.get_rect(midtop=(screen_width//2, 330))
    screen.blit(cont, cont_rect)

    key = pygame.key.get_pressed()
    if key[K_SPACE]:
        reset()


# Function to reset the game.
def reset():
    global game_running, passes, score, ticks
    rectangles.clear()  # Rectangle list is emptied.
    rectangles.extend(rectangle_generation())  # Initial triangle is added.
    ball_rect.center = (xcoor, ycoor)  # Ball position is reset.
    passes = 0  # Passes of the while loop if set to zero.
    score = 0  # Score resets.
    ticks = 120  # Game speed resets to default.
    game_running = True  # Game starts running again.



# Color values.
white = (255, 255, 255,)
black = (0, 0, 0)
light_blue = (78, 231, 245)

# Window parametres.
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keep Falling")  # Window caption
icon = pygame.image.load("assets/icon.png")  # Window icon
pygame.display.set_icon(icon)

# Ball properties.
radius = 10
gravity = 1  # Falling speed of the ball
xcoor = screen_width/2  # Initial coordinates of the ball.
ycoor = 50  # Initial coordinates of the ball.
velocity_b = 5  # Sideways velocity of the ball

# Pictures of ball rotations.
# Decided to do it like this, since it is easier then actual rotation.
# Also, rotation worsens the quality
balls = pictures.pictures()  # Import picture list form pictures module.
ball_index = 0  # Select the initial picture.
ball = balls[ball_index]  # Select the picture to display.
ball_rect = ball.get_rect(center=(xcoor, ycoor))


# Rectangle properties.
rect_gap = 100  # Default gap between rectangles.
rect_height = 10  # Height of the rectangle.
velocity_r = 1  # Velocity for upwards movement of the triangles.

# Picture to fill rectagle, once again easier than solid color.
rectangle_surface = pygame.image.load("assets/rectangle.png")
# Scale the picture to proper size.
rectangle_surface = pygame.transform.scale(
    rectangle_surface, (screen_width, rect_height))
# List of rectangles
rectangles = []
# Generate the initial rectangle.
rectangles.extend(rectangle_generation())


# Font import and sizes.

# Font for title.
font_85 = pygame.font.Font("assets/Bungee.ttf", 85)
# Font for general use.
font_45 = pygame.font.Font("assets/Bungee.ttf", 45)
# Font to display the score during game.
font_35 = pygame.font.Font("assets/Bungee.ttf", 35)
# Font to display "Press space to play"
font_25 = pygame.font.Font("assets/Bungee.ttf", 25)
# Font to display "Learn more" and "Highscores"
font_15 = pygame.font.Font("assets/Bungee.ttf", 15)
# Position of the text on the screen
text_pos = (screen_width/2, 100)

# Setting the score value and whether to allow adding score.
score = 0
score_add = True

# Number of time the while loop was repeated.
passes = 0

# Setting of game ticks. Higher the number, faster the game.
clock = pygame.time.Clock()
ticks = 120

# Booleans for menu screen, game running and name entered.
menu = True
game_running = False

# Main game loop.
while True:

    # Condition for exiting and closing the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    # Filling the screen, esentially resetting it.
    screen.fill(light_blue)

    # Setting the game speed.
    clock.tick(ticks)

    # Listening for key presses.
    key = pygame.key.get_pressed()

    # When main menu is active.
    if menu:
        main_menu()
        five_best()
        # When space is pressed, game starts and menu ends.
        if key[K_SPACE]:
            game_running = True
            menu = False
            passes = 0

    # When game is running.
    elif game_running:
        countdown()

        # If last rectangle is at certain postion, generating a new one.
        if rectangles[-1].centery <= screen_height-50:
            rectangles.extend(rectangle_generation())

        # Applying movement to all rectangles
        rectangles = rectangle_movement(rectangles)

        # Drawing all the rectangles.
        rectangle_drawing(rectangles)

        # Deleting rectangles if they are out of screen.
        rectangle_deletion(rectangles)

        # Detecting collisions.
        collisions(rectangles)

        # Counting the score.
        score_counter(rectangles)

        # Displaying the score
        score_display(score)

        # If left arrow is pressed, the ball moves to the left.
        if key[K_LEFT]:
            ball_rect.centerx -= velocity_b
            # Ball teleportation if it goes offscreen.
            if ball_rect.centerx < -20:
                ball_rect.centerx = screen_width + 20
            # Rotation of the ball, cycling trough the list of balls.
            if ball_index > -12:
                ball_index -= 1
            else:
                ball_index = 11

        # If right arrow is pressed, the ball moves to the right.
        if key[K_RIGHT]:
            ball_rect.centerx += velocity_b
            # Ball teleportation if it goes offscreen.
            if ball_rect.centerx > screen_width + 20:
                ball_rect.centerx = -20
            # Rotation of the ball, cycling trough the list of balls.
            if ball_index < 11:
                ball_index += 1
            else:
                ball_index = 0

        # Determining which ball to display, depending on the index.
        rotated_ball = balls[ball_index]
        # Displaying that ball.
        rotated_ball_rect = rotated_ball.get_rect(
            center=(ball_rect.centerx, ball_rect.centery))
        screen.blit(rotated_ball, rotated_ball_rect)

        # Teleporation of the ball to the top, if it goes below the screen.
        if ball_rect.centery > screen_height+20:
            ball_rect.centery = -20
        # Ending the game if the ball goes above the screen.
        if ball_rect.centery < -20:
            game_running = False

    # When menu is not displayed nor is the game running -> Game Over.
    elif not game_running and not menu:
        game_over()

    # Update the scren at the end of loop.
    pygame.display.update()

    # Count the passes up to 250, then stop to save system resources.
    if passes < 300:
        passes += 1
