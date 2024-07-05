from util import G
from math import sqrt


class Celest:
    def __init__(self, pos: tuple, radius: int, vel: tuple, mass: int, color: tuple, name: str = "No name", orbitBody = None):
        self.pos = pos
        self.name = name
        self.vel = vel
        self.orbit = orbitBody
        self.mass = mass
        self.r = radius
        self.color = color
        self.orbitBody = orbitBody


class World:
    def __init__(self, celest_objects: list = []):
        '''
        The argument celest_objects must be a list of Celests.
        '''
        self.objects: list = celest_objects

        for celest in self.objects:
            if celest.orbitBody == None: continue
            other = self.getObject(celest.orbitBody)
            dist = (celest.pos[0] - other.pos[0],
                    celest.pos[1] - other.pos[1])
            term = G * celest.mass * other.mass
            totalDist = sqrt(dist[0]**2 + dist[1]**2)
            partX = dist[0]/(abs(dist[0]) + abs(dist[1]))
            partY = dist[1]/(abs(dist[0]) + abs(dist[1]))
            if partX >= 0 and partY >= 0:
                partY *= -1
            if partX >= 0 and partY < 0:
                pass
            if partX < 0 and partY < 0:
                partY *= -1
            if partX < 0 and partY >= 0:
                partY *= -1
            gForce = term / totalDist**2
            vel = sqrt((gForce * totalDist)/celest.mass)
            celest.vel = (partY * vel, partX*vel)


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
