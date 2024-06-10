from pygame.locals import *
from random import randint
import pygame
import time
from operator import *


class Player:
    x = [0]  # x-position
    y = [0]  # y-position
    size = 44  # step size must be same for Player,Computer,Food
    direction = 0  # to track which direction snake is moving
    length = 3  # initial length of snake

    MaxMoveAllow = 2
    updateMove = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, 1800):
            self.x.append(-100)
            self.y.append(-100)

        # at first rendering no collision
        self.x[0] = 1 * 44
        self.y[0] = 1 * 44

    def update(self):
        self.updateMove = self.updateMove + 1
        if gt(self.updateMove,self.MaxMoveAllow):
            # update previous to new position
            for i in range(self.length - 1, 0, 1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
            # updating the position of snake by size of block(44)
            if self.direction == 0:
                self.x[0] = self.x[0] + self.size
            if self.direction == 1:
                self.x[0] = self.x[0] + self.size
            if self.direction == 2:
                self.x[0] = self.x[0] + self.size
            if self.direction == 3:
                self.x[0] = self.x[0] + self.size

            self.updateMove = 0




