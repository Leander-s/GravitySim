from Window import Window, pg
from world import World, Celest
from camera import Camera
from util import draw_text, TickCounter, Solar_Mass, Solar_Radius, Earth_Mass, Earth_Radius, AU, LY


def main():
    mainWindow = Window("Gravity Simulation", 1920, 1080)
    Sol: list[Celest] = [
        Celest((0, 0), Solar_Radius, (0, 0),
               Solar_Mass, (255, 240, 233), "Sun"),
        Celest((46000000000, 0), 2500000, (0, 45000),
               3.3*pow(10, 23), (200, 200, 200), "Mercury"),
        Celest((108000000000, 0), 6000000, (0, 35000),
               4.9*pow(10, 25), (200, 140, 120), "Venus"),
        Celest((AU, 0), Earth_Radius, (0, 29000),
               Earth_Mass, (100, 150, 180), "Earth"),
        Celest((149380000000, 0), 1737000, (0, 30000),
               7.3*pow(10, 22), (190, 190, 190), "Luna"),
        Celest((778000000000, 0), 71000000, (0, 13000),
               1.9*pow(10, 27), (190, 130, 140), "Jupiter")
    ]
    Trappist_1: list[Celest] = [
        Celest((0, 0), 0.1192 * Solar_Radius, (0, 0), 0.0898 *
               Solar_Mass, (255, 163, 74), "Trappist_1"),
        Celest((1726000000, 0), 1.116 * Earth_Radius, (0, 83679),
               1.374 * Earth_Mass, (190, 140, 140), "Trappist_1b"),
        Celest((0.0158 * AU, 0), 1.097 * Earth_Radius, (0, 70972),
               1.308 * Earth_Mass, (140, 140, 180), "Trappist_1c"),
        Celest((0.02227 * AU, 0), 0.788 * Earth_Radius, (0, 59833),
               0.388 * Earth_Mass, (130, 130, 180), "Trappist-1d")
    ]
    Galaxy:list[Celest] = [
        Celest((0, 0), 25000000000, (0, 0), 8.54 * pow(10, 36), (100, 40, 40), "Sagittarius A*"),
        Celest((LY, 0), Solar_Radius * 2, (0, 0), 8 * Solar_Mass, (255, 230, 250), "StarA", "Sagittarius A*"),
        Celest((2 * LY, 0), Solar_Radius * 1.4, (0, 0), 4 * Solar_Mass, (255, 230, 250), "StarB", "Sagittarius A*"),
        Celest((2 * LY - 0.5 * AU, 0), 3 * Earth_Radius, (0, 0), 8 * Earth_Mass, (120, 140, 150), "StarB-b", "Sagittarius A*"),
        Celest((-LY, AU), Solar_Radius * 9, (0, 0), 13 * Solar_Mass, (255, 230, 250), "StarC", "Sagittarius A*"),
        Celest((0.5 * LY, LY), Solar_Radius * 3, (0, 0), 8 * Solar_Mass, (255, 230, 250), "StarD", "Sagittarius A*"),
        Celest((LY, -LY), Solar_Radius * 0.5, (0, 0), 0.3 * Solar_Mass, (255, 230, 250), "StarE", "Sagittarius A*"),
        Celest((4 * LY, 2 * -LY), Solar_Radius * 2, (0, 0), 8 * Solar_Mass, (255, 230, 250), "StarF", "Sagittarius A*"),
        Celest((LY, LY), Solar_Radius * 1, (0, 0), 1 * Solar_Mass, (255, 230, 250), "StarG", "Sagittarius A*"),
        Celest((LY + AU, LY), Earth_Radius, (0, 0), Earth_Mass, (255, 230, 250), "StarG-a", "Sagittarius A*"),
    ]
    Test_System:list[Celest] = [
        Celest((0, 0), Solar_Radius, (0, 0), Solar_Mass, (255, 255, 255), "Sun"),   
        Celest((0, 0.5 * AU), Earth_Radius, (0, 0), Earth_Mass, (140, 170, 200), "Earth", "Sun")
    ]
    mainWorld = World(Galaxy)
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
        draw_text(mainWindow.surface, 10, 780,
                  "Current target: " + mainCamera.getTarget(), 10)
        mainCamera.draw(mainWindow.surface)
        mainWindow.clear()
        ticker.tick(mainWindow.fps)


if __name__ == '__main__':
    main()
