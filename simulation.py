from grid import *
from particle import *

class Simulation(object):
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)

    def draw(self, window):
        self.grid.draw(window)

    def add_particle(self, row, col):
        self.grid.add_particle(row, col, SandParticle)

    def remove_particle(self, row, col):
        self.grid.remove_particle(row, col)