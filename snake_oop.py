import pygame, os, sys 
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
WHITE = (255, 255, 255)

font = pygame.font.Font("AttackGraffiti.ttf", 30)


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
    f = open(fileName, 'r')
    content = f.readlines()
    f.close()
    return content

def headHitBody(gamedata):
    return False

def headHitWall(map, gamedata):
    return False

def drawData(display_surface,gamedata):
    text = "Lives : {0}, Level : {1}"
    info = text.format(gamedata.lives, gamedata.level)
    text = font.render(info, 0, WHITE)
    textpos = text.get_rect(centerx = WINDOW_WIDTH / 2, top = 32)
    display_surface.blit(text, textpos)

def drawGameOver(display_surface):
    text_1 = font.render("G a m e    O v e r", True, WHITE)
    text_2 = font.render("S p a c e  to  play or close the window", True, WHITE) 
    cx = WINDOW_WIDTH / 2
    cy = WINDOW_HEIGHT / 2
    textpos_1 = text_1.get_rect(centerx = cx, top = cy - 48)
    textpos_2 = text_2.get_rect(centerx = cx, top = cy)
    display_surface.blit(text_1, textpos_1)
    display_surface.blit(text_2, textpos_2)

def drawWalls(display_surface, img, map):
    row = 0
    for line in map:
        col = 0
        for char in line:
            if (char == '1'):
                imgRect = img.get_rect()
                imgRect.left = col * 16
                imgRect.top = row * 16
                display_surface.blit(img, imgRect)
                
            col += 1
        row += 1

def drawSnake(display_surface, img, gamedata):
    pass

def updateGame(gamedata, gameTime):
    pass

def loadImages():
    wall = pygame.image.load('wall.png')
    raspberry = pygame.image.load('berry.png')
    snake = pygame.image.load('snake.png')
    return {'wall':wall, 'berry': raspberry, 'snake': snake}

images = loadImages()
images['berry'].set_colorkey(PURPLE)

snakemap = loadMapFile('map.txt')
data = GameData()
quitGame = False
isPlaying = False

# Main loop
while not quitGame:
    if isPlaying:
        x = random.randint(1, 38)
        y = random.randint(1, 28)
            
        rrect = images['berry'].get_rect()
        rrect.left  = data.berry.x * 16
        rrect.top = data.berry.y * 16
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        # Do update stuff here
        
        isPlaying = (data.lives > 0)
        
        if isPlaying:
            display_surface.fill(BLACK)
            
            # Do drawing stuff here
            drawWalls(display_surface, images['wall'], snakemap)
            display_surface.blit(images['berry'], rrect)
            drawSnake(display_surface, images['snake'], data)
            drawData(display_surface, data)
             
        
        
    else:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        if (keys[K_SPACE]):
            isPlaying = True
            data = None
            data = GameData()
        drawGameOver(display_surface)    
    
    pygame.display.update()
    clock.tick(FPS)
                
            



 

