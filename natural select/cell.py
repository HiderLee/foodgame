from random import choice, randint
import pygame as pg
from setting import *
import time


    

class Cell:
    def __init__(self, game, gene:list) -> None:
        self.gene = self.mutant(gene)
        self.game = game
        self.origin_color = ( randint(50,255), randint(50,255), randint(50,255)   )
        self.first = False

        self.reset()

    def reset(self):
        self.x, self.y = START_POS
        self.movecount = 0
        self.food = 0
        self.path = set() #set
        self.color = (255,0,0) if self.first else self.origin_color 

    def move(self):
        if self.movecount > MAX_MOVEMENT-2:
            self.last()


        
        if  not( (self.x, self.y) in self.path ) and self.game.map.get_value(self.x, self.y) :  #맵을 찾아서 먹는함수와 연결
            self.path.add( (self.x, self.y) )
            self.food += self.game.map.get_value(self.x, self.y)

        if self.gene[self.movecount] == 'u' and self.y != 0:
            self.y -= 1
        elif self.gene[self.movecount] == 'd' and self.y != TILE_NUM_HEIGHT-1:
            self.y += 1
        elif self.gene[self.movecount] == 'l' and self.x != 0:
            self.x -= 1
        elif self.gene[self.movecount] == 'r' and self.x != TILE_NUM_WIDTH-1:
            self.x += 1

        self.movecount += 1

    def draw(self):
        pg.draw.rect(self.game.screen, self.color,
                              (self.x*TILE_SIZE, self.y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def mutant(self, gene):
        for _ in range( int(MUTANT_RATE*MAX_MOVEMENT) ):
            gene[randint(0, len(gene)-1)] = choice(dir)

        return gene

    def last(self):
        self.game.cells.sort(key=lambda cell: -cell.food)
        print(self.game.cells[0].food, len(self.game.cells))
        for i, cell in enumerate(self.game.cells):
            cell.reset()
            cell.first = False

        self.game.cells[0].first = True
        self.game.cells = self.game.cells[: CELL_NUM//SURVIVE_PER]
        self.game.cells.extend(   [Cell(self.game, i.gene[:]) for i in self.game.cells for _ in range(SURVIVE_PER-1)]  )



    def update(self):
        self.move()


dir = ['u', 'd', 'l', 'r']
cells = [ ]