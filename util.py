import pygame as pg
import time

G = 6.67430 * pow(10, -11)
Solar_Radius = 696300000
Solar_Mass = 1.9885*pow(10, 30)
Earth_Radius = 6378100
Earth_Mass = 5.9722 * pow(10, 24)
AU = 1.495978707 * pow(10, 11)
LY = 9.4607 * pow(10, 15)

def draw_circle(surface, x: int, y: int, r: int, color: tuple):
    pg.draw.circle(surface, color, (x, y), r)


def draw_text(surface, x: int, y: int, text: str, size: int, color: tuple = (255, 255, 255), font="Arial"):
    pg.font.init()
    pgfont = pg.font.SysFont(font, size)
    textSurface = pgfont.render(text, 0, color, None)
    surface.blit(textSurface, (x, y))


class TickCounter:
    def __init__(self):
        self.start = time.time()

    def tick(self, tickrate: int):
        ticked = False
        while not ticked:
            self.end = time.time()
            diff = self.end - self.start
            if diff >= 1/tickrate:
                ticked = True
        self.start = time.time()
