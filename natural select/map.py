import pygame as pg
from random import randrange
from setting import *

minimap = [ [  randrange(1, 11) if (randrange(0,100) < 100*FOOD_RATE) else 0 for _ in range(TILE_NUM_WIDTH)   ] 
           for i in range(TILE_NUM_HEIGHT)]



class Map:
    def __init__(self, game) -> None:
        self.game = game

    def draw(self):
        for y, row in enumerate(minimap):
            for x, value in enumerate(row):
                pg.draw.rect(self.game.screen,
                             (255 - (255//MAX_FOOD)*value, 255,  255- (255//MAX_FOOD)*value) if value else (100, 100, 100),
                              (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE), 0 if value else 1)
                
    def get_value(self, x, y):
        return minimap[y][x]