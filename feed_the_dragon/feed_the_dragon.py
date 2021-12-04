import pygame

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Dragon")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100


# Set colors

# Set fonts


# Main loop
running = True
while running:
    # Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# End the game
pygame.quit()
