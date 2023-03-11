import pygame as pg
import math

from settings import *


class Object:

    def __init__(self, screen, pos):
        self.screen = screen

        # in meter
        self.x = pos[0]
        self.y = pos[1]
        self.z = 0

        # in meter/second
        self.vx = 0
        self.vy = 0
        self.vz = 0

        # in meter/second square
        self.ax = 0
        self.ay = 0
        self.az = 0

        # in meter
        self.radius = RADIUS

        # in kilogram
        self.mass = MASS



    @property
    def pos(self):
        return self.x, self.y, self.z

    @property
    def energy_x(self):
        return 0.5 * self.mass * (self.vx**2)

    @property
    def energy_y(self):
        return 0.5 * self.mass * (self.vy**2)

    @property
    def energy_z(self):
        return 0.5 * self.mass * (self.vz**2)

    @property
    def energy(self):
        """Energy = (1/2) * mass * (velocity)**2 """
        return self.mass * (self.vx ** 2 + self.vy ** 2 + self.vz ** 2) * 0.5




    def move(self):
        self.x += self.vx * self.screen.delta_time
        self.y += self.vy * self.screen.delta_time
        self.z += self.vz * self.screen.delta_time
