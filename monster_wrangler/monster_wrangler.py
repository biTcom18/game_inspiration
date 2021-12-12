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
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom  = WINDOW_HEIGHT
    
    def reset(self):
        """ Resets the players position """
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT
    
    
class Monster(pygame.sprite.Sprite):
    """ A class to create enemy monster objects """
    def __init__(self, x, y, image, monster_type):
        """ Initialize the monster """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        # Monster type is an int 0 -> blue, 1 -> green, 2 -> purple, 3 -> yellow
        self.type = monster_type
        
        # Set random motion
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)
        
        
    def update(self):
        """ Update the monster """
        self.rect.x += self.dx*self.velocity
        self.rect.y += self.dy*self.velocity
        
        # Bounce the monster off the edges of the sisplay
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -1*self.dx
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.dy = -1*self.dy
            
    

# Create a player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

# Create a monster group
my_monster_group = pygame.sprite.Group()

# Test monster
monster = Monster(500, 500, pygame.image.load("green_monster.png"), 1)
my_monster_group.add(monster)
monster = Monster(100, 500, pygame.image.load("blue_monster.png"), 0)
my_monster_group.add(monster)

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