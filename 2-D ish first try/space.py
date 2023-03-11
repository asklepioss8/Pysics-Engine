from itertools import combinations
import pygame as pg
from math import sqrt

from settings import *
from spatial_functions import *
from object import Object

#-Xmx2015m

class Space:

    def __init__(self, screen):
        self.screen = screen

        self.object_count = 500
        self.obj_list = [0 for x in range(self.object_count)]
        self.obj_list_combined = None
        self.obj_list_coordinates = []

        self.initialize()

    def initialize(self):
        if INTERVAL > RADIUS * 2:
            self.obj_list_coordinates = isoform_coordinate_creator(HALF_WIDTH,
                                                                   HALF_HEIGHT,
                                                                   INTERVAL,
                                                                   self.object_count)
        else:
            raise Exception("The initial distance between object must be grater than their radius")

        reg1 = 0
        for coordinates in self.obj_list_coordinates:
            self.obj_list[reg1] = Object(self.screen, coordinates)
            reg1 += 1
        self.obj_list_combined = list(combinations(self.obj_list, 2))


    def gravity(self, obj1, obj2):
        """Force (in Newton) = G * (M1 * M2) * (distance_(x, y or z)/ (distance ** 3)
        G = 6.674×10−11 m3⋅kg−1⋅s−2 """
        dist = distance(obj1, obj2)
        fx = (GRAVITY_CONST * obj1.mass * obj2.mass * partial_distance_x(obj1, obj2)) / (dist ** 3)
        fy = (GRAVITY_CONST * obj1.mass * obj2.mass * partial_distance_y(obj1, obj2)) / (dist ** 3)
        fz = (GRAVITY_CONST * obj1.mass * obj2.mass * partial_distance_z(obj1, obj2)) / (dist ** 3)

        return fx, fy, fz

    def gravitaional_potential(self):
        """Energy = G * (M1) * (M2) / distance"""
        gravitational_energy = 0
        for obj in self.obj_list_combined:
            gravitational_energy += (GRAVITY_CONST * obj[0].mass * obj[1].mass) / distance(obj[0], obj[1])
        return -gravitational_energy

    def kinetic_energy(self):
        kinetic_energy = 0
        for obj in self.obj_list:
            kinetic_energy += obj.energy
        return kinetic_energy

    def energy(self):
        """returns, gravitational, kinetic and total energgy at the same time"""
        reg1 = self.gravitaional_potential()
        reg2 = self.kinetic_energy()
        reg3 = reg1 + reg2

        return reg1, reg2, reg3

    def movement(self):
        """Force caused by gravity causes acceleration in directions
        a = F / M """

        # acceleration reset
        for obj in self.obj_list:
            obj.ax = 0
            obj.ay = 0
            obj.az = 0

        # for each object created, the gravitational force must be calculated in binary between objects
        for obj in self.obj_list_combined:
            # collision detection
            if (obj[0].radius + obj[1].radius) >= distance(obj[0], obj[1]):
                collision(obj[0], obj[1])

            else:
                # Force for 3 axes
                fx, fy, fz = self.gravity(obj[0], obj[1])

                # acceleration for x-axis
                if partial_distance_x(obj[0], obj[1]) != 0:
                    obj[0].ax += -fx / obj[0].mass
                    obj[1].ax += fx / obj[1].mass

                # acceleration for y-axis
                if partial_distance_y(obj[0], obj[1]) != 0:
                    obj[0].ay += -fy / obj[0].mass
                    obj[1].ay += fy / obj[1].mass

                # acceleration for z-axis
                if partial_distance_z(obj[0], obj[1]) != 0:
                    obj[0].az += -fz / obj[0].mass
                    obj[1].az += fz / obj[1].mass

        # Convert acceleration to velocity
        for obj in self.obj_list:
            obj.vx += obj.ax * self.screen.delta_time
            obj.vy += obj.ay * self.screen.delta_time
            obj.vz += obj.az * self.screen.delta_time

            # move objects
            obj.move()

    def zoom(self):
        pass

    def draw(self):
        for obj in self.obj_list:
            pg.draw.circle(self.screen.screen, "white", (obj.pos[0] / SCOPE, obj.pos[1] / SCOPE), obj.radius)



    def update(self):
        self.movement()
        #print(self.energy())
