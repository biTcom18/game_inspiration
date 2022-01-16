import pygame
import random

from pygame.locals import *

# Inialization if pygame
pygame.init()

# Setting the game values
FPS = 30
clock = pygame.time.Clock()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)

font = pygame.font.Font("AttackGraffiti.ttf", 32)


# Define classes

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class GameData:
    def __init__(self):
        self.lives = 3
        self.isDead = False
        self.blocks = []
        self.tick = 250
        self.speed = 250
        self.level = 1
        self.berrycount = 0
        self.segments = 1
        self.frame = 0
        
        bx = random.randint(1,38)
        by = random.randint(1,28)
        
        self.berry = Position(bx, by)
        self.blocks.append(Position(20,15))
        self.blocks.append(Position(19,15))
        self.direction = 0
        
def looseLife(gamedata):
    pass

def positionBerry(gamedata):
    pass

def loadMapFile(fileName):
    return None

def headHitBody(gamedata):
    return False

def headHitWall(map, gamedata):
    return False

def drawData(surface,gamedata):
    pass

def drawGameOver(surface):
    pass 

def drawWalls(surface, img, map):
    pass

def drawSnake(surface, img, gamedata):
    pass

def updateGame(gamedata, gameTime):
    pass

def loadImages():
    return {}

images = loadImages()
images['berry'].set_colorkey(PURPLE)

snakemap = loadMapFile('map.txt')
data = GameData()
running = True
isPlaying = False

# Main loop
while running:
    if isPlaying:
        x = random.randint(1, 38)
        y = random.randint(1, 28)
            
        rrect = images['berry'].get_rect()
        rrect.left  = data.berry.x * 16
        rrect.top = data.berry.y * 16
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
        # Do update stuff here
        
        isPlaying = (data.lives > 0)
        
        if isPlaying:
            display_surface.fill(BLACK)
            
        # Do drawing stuff here
    else:
        keys = pygame.key.get_pressed()
        
        if (keys[K_SPACE]):
            isPlaying = True
            data = None
            data = GameData()
            drawGameOver(display_surface)    
    
    pygame.display.update()
    clock.tick(FPS)
                
            
# End the game
pygame.quit()



 

