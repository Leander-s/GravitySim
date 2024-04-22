from world import World
from Window import Window, pg
from util import draw_circle, draw_text


class Camera:
    def __init__(self, world: World, window: Window, pos: tuple = (0, 0), zoomFactor: float = 1, defaultZoom: float = 1/200000000):
        self.pos = pos
        self.target = None
        self.zoomFactor: float = zoomFactor
        self.defaultZoom: float = defaultZoom
        self.zoom: float = self.zoomFactor * self.defaultZoom
        self.world = world
        self.window = window
        self.speed = 3

    def update(self):
        if self.window.mouse_wheel != 0:
            self.zoomFactor *= self.window.mouse_wheel/5 + 1
        self.zoom = self.zoomFactor * self.defaultZoom

        if pg.key.get_pressed()[pg.K_w]:
            self.pos = (self.pos[0], self.pos[1] - self.speed/self.zoom)
        if pg.key.get_pressed()[pg.K_s]:
            self.pos = (self.pos[0], self.pos[1] + self.speed/self.zoom)
        if pg.key.get_pressed()[pg.K_a]:
            self.pos = (self.pos[0] - self.speed/self.zoom, self.pos[1])
        if pg.key.get_pressed()[pg.K_d]:
            self.pos = (self.pos[0] + self.speed/self.zoom, self.pos[1])

    def setTarget(self, target):
        self.pos = (0, 0)
        self.target = target

    def getTarget(self):
        if self.target is None:
            return "No target"
        return self.target.name

    def draw(self, surface):
        if self.target is None:
            targetPos = (0, 0)
        else:
            targetPos = self.target.pos
        translation = ((-targetPos[0]-self.pos[0]) * self.zoom + self.window.width/2,
                       (-targetPos[1]-self.pos[1]) * self.zoom + self.window.height/2)
        for object in self.world.objects:
            pixel_pos = (object.pos[0] * self.zoom, object.pos[1] * self.zoom)
            translated_pos = (
                pixel_pos[0] + translation[0], pixel_pos[1] + translation[1])
            draw_circle(
                surface, translated_pos[0], translated_pos[1], object.r*self.zoom, object.color)
            draw_text(
                surface, translated_pos[0], translated_pos[1] - 40,
                object.name, 30, (130, 130, 130)
            )
