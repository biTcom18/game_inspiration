import pygame
from pygame import font

# Initialize pygame
pygame.init()

# Set display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface  = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set FPS  and clock
FPS = 30
clock = pygame.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELERATION = .25

score = 0
burger_points = 0
burger_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY

boost_level = STARTING_BOOST_LEVEL

burger_velocity = STARTING_BURGER_VELOCITY

# Set colors
ORANGE = (246, 170, 54)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set fonts
font = pygame.font.Font("WashYourHand.ttf", 32)

# Set text
points_text = font.render("Burger Points: " + str(burger_points), True, ORANGE)
points_rect = points_text.get_rect()
points_rect.topleft = (10, 10)

score_text = font.render("Score: " + str(score), True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 50)

title_text = font.render("Burger Dog", True, ORANGE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

eaten_text = font.render("Burgers Eaten: " + str(burger_eaten), True, ORANGE)
eaten_rect = eaten_text.get_rect()
eaten_rect.centerx = WINDOW_WIDTH//2
eaten_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

boost_text = font.render("Boost: " + str(boost_level), True, ORANGE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH - 10, 50) 

game_over_text = font.render("FINAL SCORE: " + str(score), True, ORANGE)


# Set sound and music 

# Set images


# The main game loop
running = True
while running:
    for event in pygame.event.get():
        # Check if the user wants to quit
        if event.type == pygame.QUIT:
            running = False
            
# End the game
pygame.quit()