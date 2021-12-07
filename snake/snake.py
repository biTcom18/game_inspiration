import pygame

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Snake~~")

# Set FPS and clock
FPS = 20
clock = pygame.display.Clock()

# Set game values
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100

snake_dx = 0
snake_dy = 0

score = 0

# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0 , 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

# Set fonts
font = pygame.font.SysFont("gabriola",  48)


# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED)


# Set sound and music

# Set images

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
# End the game
pygame.quit()

