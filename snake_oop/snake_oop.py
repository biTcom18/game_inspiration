#!/usr/bin/python

import pygame, random

pygame.init()

FPS = 30
clock = pygame.time.Clock()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

font = pygame.font.Font(None, 32)

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Game:
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

        bx = random.randint(1, 38)
        by = random.randint(1, 28)

        self.berry = Position(bx, by)
        self.blocks.append(Position(20,15))
        self.blocks.append(Position(19,15))
        self.direction = 0 # 0 = right, 1 = left, 2 = up, 3 = down
    

def load_map_file(filename):
    f = open(filename, 'r')
    content = f.readlines()   
    f.close()
    return content

snakemap = load_map_file('snake_oop/map.txt')


def lose_life(gamedata):
    pass

def position_berry(gamedata):
    pass



def head_hit_body(gamedata):
    return False


def head_hit_wall(map, gamedata):
    return False

def draw_data(display_surface, gamedata):
    text = "Lives = {0}, level = {1}"
    info = text.format(gamedata.lives, gamedata.level)
    text = font.render(info, 0,(255, 255, 255))
    textpos = text.get_rect(centerx = display_surface.get_width()/2, top = 32)
    display_surface.blit(text, textpos)

def draw_game_over(surface):
    text1 = font.render("Game Over", 1, (255, 255, 255))
    text2 = font.render("Space to play or close the window", 1, (255, 255, 255))
    # named parameters

    cx = display_surface.get_width() / 2
    cy = display_surface.get_height() / 2

    textpos1 = text1.get_rect(centerx=cx, top=cy - 48)
    textpos2 = text2.get_rect(centerx=cx, top=cy)
    surface.blit(text1, textpos1)
    surface.blit(text2, textpos2)

   
   
def draw_walls(surface, img, map):
    row = 0

    for line in map:
        col = 0
        for char in line:
            if ( char == '1'):
                imgRect = img.get_rect()
                imgRect.left = col * 16
                imgRect.top = row * 16
                surface.blit(img, imgRect)
            col += 1
        row += 1


def draw_snake(display_surface, img, gamedata):
    first = True
    for b in gamedata.blocks:
        dest = (b.x * 16, b.y * 16, 16, 16)
        if first:
            first = False
            src = (((gamedata.direction * 2) + gamedata.frame) * 16, 0, 16, 16)
        else:
            src = (8*16, 0, 16, 16)
    display_surface.blit(img, dest, src)

def update_game(gamedata, gametime):
    pass


def load_images():
    wall = pygame.image.load('snake_oop/wall.png')
    raspberry = pygame.image.load('snake_oop/berry.png')
    snake = pygame.image.load('snake_oop/snake.png')
    return {'wall': wall, 'berry': raspberry, 'snake': snake}

images = load_images()
images['berry'].set_colorkey((255, 0, 255))

data = Game()
quit_game = False

is_playing = False

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    if is_playing:
        x = random.randint(1,38)
        y = random.randint(1,28)

        rrect = images['berry'].get_rect()
        rrect.left = data.berry.x * 16
        rrect.top = data.berry.y * 16

        # Do update staff
        update_game(data, clock.get_time())
        crashed = head_hit_wall(snakemap, data) or head_hit_body(data)
        if crashed:
            lose_life(data)
            position_berry(data)
            
        is_playing = (data.lives > 0)
        if is_playing:
                display_surface.fill((0, 0, 0))
                # Do drawing stuff here
                draw_walls(display_surface, images['wall'], snakemap)
                display_surface.blit(images['berry'], rrect)
                draw_snake(display_surface, images['snake'], data)
                draw_data(display_surface, data)

    else:
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_SPACE]):
            is_playing = True
            data = None
            data = Game()
            
        draw_game_over(display_surface)
    
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()



