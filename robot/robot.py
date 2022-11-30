import pygame

from robotview import RobotView
from robotcontroller import RobotController
from robotgenerator import RobotGenerator
from radarview import RadarVeiw

pygame.init() 

FPS = 30
clock = pygame.time.Clock()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

lastMillis = 0

generator = RobotGenerator()
view = RobotView('robot/robot.png')
radar = RadarVeiw('robot/blip.png', 'robot/radarview.png')
controller = RobotController(generator.getRobots())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    deltaTime = lastMillis / 1000

    generator.update(deltaTime)
    controller.update(deltaTime)

    display_surface.fill((0, 0, 0))

    view.draw(display_surface, generator.getRobots())
    radar.draw(display_surface, generator.getRobots())

    pygame.display.update()
    lastMillis = clock.tick(FPS)

pygame.quit()
