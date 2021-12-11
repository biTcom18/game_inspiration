import pygame, random

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wrangler")

# Set FPS and clock
FPS  = 60
clock = pygame.time.Clock()

# Define classes
class Game():
    """ A class to control gameplay """
    def __init__(self):
        """ Initialize the game object """
        pass
    
    def update(self):
        """ Update our game object """
        pass
    
    def draw(self):
        """ Draw the HUD and other to display """
        pass
    
    def check_collisions():
        """ Check for collisions between player and monsters """
        
    def start_new_round(self):
        """ Populate display board with new monsters """
        pass
    
    def choose_new_target(self):
        """ Choose a new target monster for the player """
        pass
    
    def pause_game(self):
        """ Pause the game """
        pass
    
    def reset_game(self):
        """ Reset the game """
        pass
    
    
    
class Player(pygame.sprite.Sprite):
    """ A player class that the user can control """
    def __init__(self):
        """ Initialize the player """
        super().__init__()
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT
        
        self.lives = 5
        self.warps = 2
        self.velocity = 8
        
        self.catch_sound = pygame.mixer.Sound("catch.wav")
        self.die_sound = pygame.mixer.Sound("die.wav")
        self.warp_sound = pygame.mixer.Sound("warp.wav") 
    
    def update(self):
        """ Update the player """
        keys = pygame.key.get_pressed()
        
        # Move the player within the bounds if tge screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.velocity
    
      
    def warp(self):
        """ Warp the player to the bottom 'safe zone' """
        pass
    
    def reset(self):
        """ Resets the players position """
        pass
    
    
class Monster(pygame.sprite.Sprite):
    """ A class to create enemy monster objects """
    def __init__(self):
        """ Initialize the monster """
        
    def update(self):
        """ Update the monster """
        pass
    

# Create a player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)


# Create a monster group
my_monster_group = pygame.sprite.Group()

# Create a game object
my_game = Game()

# The main game loop
running = True
while running:
    # Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    # Fill the display
    display_surface.fill((0, 0, 0))
    
    # Update and draw sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)
    
    my_monster_group.update()
    my_monster_group.draw(display_surface)
    
    # Update and draw the Game
    my_game.update()
    my_game.draw()
     
            
    # Update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)
            
            
            
# End the game
pygame.quit()