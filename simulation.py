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

    def update(self):
        for row in range(self.grid.rows):
            for col in range(self.grid.columns):
                particle = self.grid.get_cell(row, col):
                if particle is not None:
                    new_pos = particle.update(self.grid, row, col)
                    if new_pos != (row, col):
                        self.grid.set_cell(new_pos[0], new_pos[1], particle)
                        self.grid.remove_particle(row, col)