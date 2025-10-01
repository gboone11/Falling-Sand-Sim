import pygame

class Grid(object):
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        for row in range(self.rows):
            for col in range(self.columns):
                particle = self.cells[row][col]
                if particle is not None:
                    color = particle.color
                    rect = (col*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(window, color, rect)

    def is_in_grid(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.columns

    def add_particle(self, row, col, particle_type):
        if self.is_in_grid(row, col):
            self.cells[row][col] = particle_type()

    def remove_particle(self, row, col):
        if self.is_in_grid(row, col):
            self.cells[row][col] = None

    def is_cell_empty(self, row, col):
        if self.is_in_grid(row, col):
            return self.cells[row][col] is None
        return False

    def set_cell(self, row, col, particle):
        if self.is_in_grid(row, col):
            self.cells[row][col] = particle

    def get_cell(self, row, col):
        if self.is_in_grid(row, col):
            return self.cells[row][col]
        raise ValueError("cell is not in grid")
    
    def clear(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.remove_particle(row, col)
    
