from util import G
from math import sqrt


class Celest:
    def __init__(self, pos: tuple, radius: int, vel: tuple, mass: int, color: tuple, name: str = "No name"):
        self.pos = pos
        self.name = name
        self.vel = vel
        self.mass = mass
        self.r = radius
        self.color = color


class World:
    def __init__(self, celest_objects: list = []):
        '''
        The argument celest_objects must be a list of Celests.
        '''
        self.objects: list = celest_objects

    def getObject(self, name: str):
        for object in self.objects:
            if object.name == name:
                return object

    def update(self, fps, warp=1):
        forces: dict = {}

        for i in range(len(self.objects)):
            # Updating the force
            force: tuple = (0, 0)
            for j in range(len(self.objects)):
                if i == j:
                    continue
                if (i, j) not in forces:
                    dist = (self.objects[i].pos[0] - self.objects[j].pos[0],
                            self.objects[i].pos[1] - self.objects[j].pos[1])
                    term = G * self.objects[i].mass * self.objects[j].mass
                    totalDist = sqrt(dist[0]**2 + dist[1]**2)
                    partX = -dist[0]/totalDist
                    partY = -dist[1]/totalDist
                    forces[(i, j)] = (partX * term /
                                      totalDist**2, partY * term/totalDist**2)
                    forces[(j, i)] = (-forces[(i, j)][0], -forces[(i, j)][1])

                force = (force[0] + forces[(i, j)][0],
                         force[1] + forces[(i, j)][1])

            # Updating the velocity
            self.objects[i].vel = (self.objects[i].vel[0] + warp * force[0]/(self.objects[i].mass * fps),
                                   self.objects[i].vel[1] + warp * force[1]/(self.objects[i].mass * fps))

            # Updating the Position
            self.objects[i].pos = (self.objects[i].pos[0] + warp * self.objects[i].vel[0]/fps,
                                   self.objects[i].pos[1] + warp * self.objects[i].vel[1]/fps)
