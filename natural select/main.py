import pygame as pg
import sys
from setting import *
from map import *
from cell import *

dir = ['u', 'd', 'l', 'r']
class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        self.FPS = FPS

        self.onlyseeFirst = False

    def new_game(self):
        self.map = Map(self)
        self.cells = [   Cell(self,  [ choice(dir) for _ in range(MAX_MOVEMENT) ] ) for i in range(CELL_NUM)]

    def update(self):
        pg.display.flip()   #화면 업데이트
        self.delta_time = self.clock.tick(self.FPS) #fps 고정
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')  #fps를 제목으로
        for cell in self.cells:
            cell.update()
            if cell.movecount > MAX_MOVEMENT-2:
                break
        
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:  # A 키를 누르면 FPS 감소
            self.FPS -= 5 if self.FPS - 5 > 0 else 0
        if keys[pg.K_d]:  # D 키를 누르면 FPS 증가
            self.FPS += 5 if self.FPS < 600 else 0  

    def draw(self):
        self.screen.fill('black')
        self.map.draw()

        if self.onlyseeFirst:
            self.cells[0].draw()
        else:
            for cell in self.cells[::-1]:
                cell.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # 왼쪽 마우스 버튼 클릭
                    self.onlyseeFirst = not self.onlyseeFirst 
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()