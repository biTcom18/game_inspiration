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

def load_images():
    wall = pygame.image.load('wall.png')
    raspberry = pygame.image.load('berry.png')
    snake = pygame.image.load('snake.png')
    return {'wall': wall, 'berry': raspberry, 'snake': snake}

images = load_images()
images['berry'].set_colorkey((255, 0, 255))


def load_map_file(filename):
    f = open(filename, 'r')
    content = f.readlines()
    f.close()
    return content

snakemap = load_map_file('map.txt')


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
    
def lose_life(gamedata):
    pass

def position_berry(gamedata):
    pass



def head_hit_body(gamedata):
    return False


def head_hit_wall(map, gamedata):
    return False

def draw_data(display_surface, gamedata):
    pass

def draw_game_over(display_surface):
    pass

def draw_walls(display_surface, img, map):
    pass

def draw_snake(display_surface, img, gamedata):
    pass

def update_game(gamedata, gametime):
    pass


data = Game()
quit_game = False

is_playing = False

while not quit_game:
    for event in pygame.event.get():
        if event.typy == pygame.QUIT:
            quit_game = True

        if is_playing:
            x = random.randint(1,38)
            y = random.randint(1,28)

            rrect = images['berry'].get_rect()
            rrect.left = data.berry.x * 16
            rrect.top = data.berry.y * 16

            # Do update staff
            is_playing = (data.lives > 0)
            if is_playing:
                display_surface.fill((0, 0, 0))
                # Draw here

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



