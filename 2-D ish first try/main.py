import pygame as pg
from sys import exit

from settings import *
from space import Space


class Window:

    def __init__(self):

        # initialize pygame
        pg.init()

        # initialize the window
        self.screen = pg.display.set_mode(RES, DOUBLEBUF)

        # handle the time related data
        self.clock = pg.time.Clock()
        self.delta_time = 1

        # running flag
        self.running = True


    def initialize(self):
        self.space = Space(self)


    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False


    def update(self):

        # delta timing and FPS max
        self.delta_time = self.clock.tick(FPS)

        # display the FPS as caption
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

        # Class updates
        self.space.update()


    def draw(self):
        pg.display.flip()
        self.screen.fill('black')

        # Class draw
        self.space.draw()



    def run(self):
        self.initialize()
        while self.running:
            self.check_event()
            self.update()
            self.draw()
        else:
            pg.quit()
            exit()


if __name__ == "__main__":
    Window().run()
