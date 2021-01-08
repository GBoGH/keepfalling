# Decided to make separate module, to keep the main file clean.

import pygame

# Radius of the ball
radius = 10


# Load every ball, transform them and store them as a list, which is then returned
def pictures():
    ball0 = pygame.transform.scale(pygame.image.load("assets/ball0.png"),
                                   (radius*2, radius*2))
    ball30 = pygame.transform.scale(pygame.image.load("assets/ball30.png"),
                                    (radius*2, radius*2))
    ball60 = pygame.transform.scale(pygame.image.load("assets/ball60.png"),
                                    (radius*2, radius*2))
    ball90 = pygame.transform.scale(pygame.image.load("assets/ball90.png"),
                                    (radius*2, radius*2))
    ball120 = pygame.transform.scale(pygame.image.load("assets/ball120.png"),
                                     (radius*2, radius*2))
    ball150 = pygame.transform.scale(pygame.image.load("assets/ball150.png"),
                                     (radius*2, radius*2))
    ball180 = pygame.transform.scale(pygame.image.load("assets/ball180.png"),
                                     (radius*2, radius*2))
    ball210 = pygame.transform.scale(pygame.image.load("assets/ball210.png"),
                                     (radius*2, radius*2))
    ball240 = pygame.transform.scale(pygame.image.load("assets/ball240.png"),
                                     (radius*2, radius*2))
    ball270 = pygame.transform.scale(pygame.image.load("assets/ball270.png"),
                                     (radius*2, radius*2))
    ball300 = pygame.transform.scale(pygame.image.load("assets/ball300.png"),
                                     (radius*2, radius*2))
    ball330 = pygame.transform.scale(pygame.image.load("assets/ball330.png"),
                                     (radius*2, radius*2))
    balls = [ball0,
             ball30,
             ball60,
             ball90,
             ball120,
             ball150,
             ball180,
             ball210,
             ball240,
             ball270,
             ball300,
             ball330
             ]
    return balls
