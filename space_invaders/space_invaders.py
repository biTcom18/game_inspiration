
import pygame, random

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Define classes
class Game():
""" A class to help control and update gameplay """
    def __init__(self):
        pass
    
    def update(self):
        """ Update the game """
        pass
    
    def draw(self):
        """ Draw the hud and other information to display """
        pass 

    def shift_aliens(self):
        """ Shift a wave of aliens down the screen and revers direction """
        
    def check_collisions(self):
        """ Check for collisions between player bullet group and alien group """
        pass
    
    def check_round_completion(self):
        """ Check to see if a player has completed a single round """
        pass
    
    def start_new_round(self):
        """ Start a new round """
        pass
        
    def check_game_status(self):        
        """ Check to see the status of the game and how the player died """
        pass
    
    def pause_game(self):
        """ Pauses the game """
        pass
    
    def reset_game(self):
        """ Reset the game """
        pass
    
class Player(pygame.sprite.Sprite):
    """ A class to model a spaceship the user can control """
    def __init__(self):
        """ Initialize the player """
        pass
    
    def update(self):
        """ Update the player """
        pass
    
    def fire(self):
        """ Fire a bullet """
        
    def reset(self):
        """ Reset the players position """
        pass 
    
    
class Alien(pygame.sprite.Sprite):
    """ A class to model an enemy alien """
    def __init__(self):
        """ Initialize the alien """
        pass
    
    def update(self):
        """ Update the alien """
        pass
    
    def fire(self):
        """ Fire a bullet """
        
    def reset(self):
        """ Reset the alien position """
        pass 
        
        
        
        
# The main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Update the display and tick
    pygame.display.update()
    clock.tick(FPS)
    
# End the game
pygame.quit()
