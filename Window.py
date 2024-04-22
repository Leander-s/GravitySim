import pygame as pg
import time


class Window:
    def __init__(
            self, title: str, width: int, height: int, fps: int = 144, fullscreen: bool = False, backgroundcolor: tuple = (0, 0, 0)
    ):
        pg.init()
        self.width: int = width
        self.height: int = height
        self.background_color: tuple = backgroundcolor
        self.title: str = title
        self.fullscreen: bool = fullscreen
        self.fps: int = fps
        self.actual_fps: int = 0
        self.timer: float = time.time()
        self.clock = pg.time.Clock()
        pg.display.set_caption(title)
        self.surface = pg.display.set_mode((width, height), display=fullscreen)
        self.click: bool = False
        self.mouse1: bool = False
        self.mouse_wheel: int = 0
        self.key_is_held: dict = {}
        self.key_was_pressed: dict = {}
        self.last_key_pressed = None
        self.closed: bool = False

    def update(self):
        self.last_key_pressed = None
        self.mouse_wheel = 0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.closed = True
            if event.type == pg.MOUSEWHEEL:
                self.mouse_wheel = event.y
            if event.type == pg.KEYDOWN:
                self.last_key_pressed = event.key

        if pg.mouse.get_pressed(3)[0]:
            if self.click and self.mouse1:
                self.click = False
            elif not self.click and not self.mouse1:
                self.click = True
                self.mouse1 = True
        else:
            self.click = True
            self.mouse1 = False

    def clear(self):
        pg.display.flip()
        self.surface.fill(self.background_color)
        self.clock.tick(self.fps)
        stop = time.time()
        diff = stop - self.timer
        if diff == 0:
            self.actual_fps = 200
        else:
            self.actual_fps = int(1/diff)
        self.timer = time.time()

    def was_key_pressed(self, key):
        if pg.key.get_pressed()[key]:
            if key not in self.key_was_pressed:
                self.key_was_pressed[key] = False
            if key not in self.key_is_held:
                self.key_is_held[key] = False
            if self.key_was_pressed[key] and self.key_is_held[key]:
                self.key_was_pressed[key] = False
            elif not self.key_was_pressed[key] and not self.key_is_held[key]:
                self.key_was_pressed[key] = True
                self.key_is_held[key] = True
        else:
            self.key_is_held[key] = False
            self.key_was_pressed[key] = False

        return self.key_was_pressed[key]
