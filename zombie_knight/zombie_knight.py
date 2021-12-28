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
    
    
class Tile(pygame.sprite.Sprite):
    """ A class to represent 32x32 pixel area in our display """
    
    def __init__(self):
        """ Initialize the tile """    
        pass
    
    
class Player(pygame.sprite.Sprite):
    """ A class the user can control """
    
    def __ini__(self):
        """ Initialize the player """
        pass
    
    def update(self):
        """ Update the player """
        pass
    
    def move(self):
        """ Move the player """
        pass
    
    
    def check_collisions(self):
        """ Check for collisions with platforms and portals """
        pass 

    def check_animations(self):
        """ Check to see if jump/fire animation shpuld run """
        pass
        
    def jump(self):
        """ Jump upwards if on a platform """
        pass        
    
    def fire(self):
        """ Fire a 'bullet' from a sword """
        pass

    def reset(self):
        """ Reset the player's position """
        pass

    def animate(self):
        """ Anemate the players actions """
        pass

class Bullet(pygame.sprite.Sprite):
    """ A projectile launched by the player """
    
    def __init__(self):
        """ Initialize the bullet """
        pass

    def update(self):
        """ Update the bullet """
        pass

class Zombie(pygame.sprite.Sprite):
    """ An enemy class that moves across the screen """
    
       def __ini__(self):
            """ Initialize the zombie """
        pass
    
    def update(self):
        """ Update the zombie """
        pass
    
    def move(self):
        """ Move the zombie """
        pass
    
    
    def check_collisions(self):
        """ Check for collisions with platforms and portals """
        pass 

    def check_animations(self):
        """ Check to see if death/rise animation shpuld run """
        pass
    

    def animate(self):
        """ Animate the zombie's actions """
        pass
    
    
class RubyMaker(pygame.sprite.Sprite):
    """ A title that is animated.A ruby will be generated here """
    
    def __init__(self):
        """ Initialize the ruby maker """
        pass
    
    def update(self):
        """ Update the ruby maker """
        pass

    def animate(self):
        """ Animate the ruby maker """
        pass
    
    
class Ruby(pygame.sprite.Sprite):
    """ A class the player must collect to earn points and health """
    
    def __init__(self):
        """ Initialize the ruby """
        pass
    
    def update(self):
        """ Update the ruby """
        pass
    
    def move(self):
        """ Move the ruby """
        pass
    
    def check_collisions(self):
        """ Check for collisions with platforms and portals """
        pass
    
    def animate(self):
        """ Animate the ruby """
        pass
    
    
class Portal(pygame.sprite.Sprite):
    """ A class that if collided with will transport you """
    
    def __init__(self):
        """ Initialize the portal """
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