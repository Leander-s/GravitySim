from Window import Window, pg
from world import World, Celest
from camera import Camera
from util import draw_text, TickCounter


def main():
    mainWindow = Window("Gravity Simulation", 1600, 800)
    celests: list[Celest] = [
        Celest((0, 0), 700000000, (0, 0), 2 *
               pow(10, 30), (255, 255, 255), "Sun"),
        Celest((46000000000, 0), 2500000, (0, 45000),
               3.3*pow(10, 23), (200, 200, 200), "Mercury"),
        Celest((108000000000, 0), 6000000, (0, 35000),
               4.9*pow(10, 25), (200, 140, 120), "Venus"),
        Celest((149000000000, 0), 6370000, (0, 29000),
               6*pow(10, 24), (100, 150, 180), "Earth"),
        Celest((149380000000, 0), 1737000, (0, 30000),
               7.3*pow(10, 22), (190, 190, 190), "Luna"),
        Celest((778000000000, 0), 71000000, (0, 13000),
               1.9*pow(10, 27), (190, 130, 140), "Jupiter")
    ]
    mainWorld = World(celests)
    mainCamera = Camera(mainWorld, mainWindow, (0, 0))
    ticker = TickCounter()
    warp = 1
    targetNumber = len(mainWorld.objects) + 1
    currentTarget = 0

    while (not mainWindow.closed):
        if mainWindow.last_key_pressed == pg.K_PERIOD:
            warp *= 2
        if mainWindow.last_key_pressed == pg.K_COMMA:
            warp /= 2
        if mainWindow.last_key_pressed == pg.K_e:
            currentTarget = (currentTarget + 1) % targetNumber
            if currentTarget == 0:
                mainCamera.setTarget(None)
            else:
                mainCamera.setTarget(mainWorld.objects[currentTarget-1])
        if mainWindow.last_key_pressed == pg.K_q:
            currentTarget = (currentTarget - 1) % targetNumber
            if currentTarget == 0:
                mainCamera.setTarget(None)
            else:
                mainCamera.setTarget(mainWorld.objects[currentTarget-1])
        mainWindow.update()
        mainWorld.update(mainWindow.fps, warp)
        mainCamera.update()
        draw_text(mainWindow.surface, 700, 10, "Warp: " + str(warp), 10)
        draw_text(mainWindow.surface, 10, 10,
                  "Meters per pixel: " + str(int(round(1/mainCamera.zoom, 0))), 10)
        draw_text(mainWindow.surface, 1300, 10, "FPS: " +
                  str(int(round(mainWindow.actual_fps))), 10)
        draw_text(mainWindow.surface, 10, 780, "Current target: " + mainCamera.getTarget(), 10)
        mainCamera.draw(mainWindow.surface)
        mainWindow.clear()
        ticker.tick(mainWindow.fps)


if __name__ == '__main__':
    main()