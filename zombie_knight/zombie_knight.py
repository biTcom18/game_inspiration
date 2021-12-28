import pygame, random
# Use 2D vectors

vector = pygame.math.Vector2

# Initialize pygame
pygame.init()

# Set display surface (tile size is 32x32 so 1280/32 = 40 tiles wide, 736/32 = 23 tiles height)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Knight")

# Set FPS  and clock
FPS = 30
clock = pygame.time.Clock()

# Define classes
class Game():
    """ A class to help manage gameplay """
    
    def __init__(self):
        """ Initialize the game """
        pass
    
    def update(self):
        """ Update the game """ 
        pass
    
    def draw(self):
        """ Draw the game HUD """    
        pass
    
    def add_zombie(self):
        """ Add a zombie to the game """
        pass
    
    def check_collisions(self):
        """ Check collisions that affect gameplay """
        pass
    
    def check_round_completion(self):
        """ Check if the player survived a single night """
        pass
    
    def check_game_over(self):
        """ Check to see if the player lost the game """
        pass
    
    def start_new_round(self):
        """ Start a new night """
        pass
    
    def pause_game(self):
        """ Pause the game """
        pass
    
    def reset_game(self):
        """ Reset the game """
        pass







# Load a background image (we must resize)
background_image = pygame.transform.scale(pygame.image.load("zombie_knight/images/background.png"), (1280, 736))
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Blit the background
    display_surface.blit(background_image, background_rect)
    
    # Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)
    
# End the game
pygame.quit()