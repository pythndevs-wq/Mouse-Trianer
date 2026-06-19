import pygame
import random


pygame.init()

# screen setup
HEIGHT, WIDTH = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Trainer")

# clicks
CPS = 0
clicks = 0

# others behind the game loop
running = True
clock = pygame.time.Clock()

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        


    clock.tick(60)  # limit to 60 frames per second
    # refrest screen after every loop
    pygame.display.flip()