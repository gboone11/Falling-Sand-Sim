import pygame
LIGHT_GREY = (55, 55, 55)

class Grid(object):
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        for row in range(self.rows):
            for col in range(self.columns):
                color = LIGHT_GREY
                particle = self.cells[row][col]
                if particle is not None:
                    color = particle.color
                rect = (col*self.cell_size, row*self.cell_size, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(window, color, rect)