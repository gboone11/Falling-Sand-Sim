import pygame, sys
from grid import *
from particle import *

class Simulation(object):
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.cell_size = cell_size

    def draw(self, window):
        self.grid.draw(window)

    def add_particle(self, row, col):
        self.grid.add_particle(row, col, SandParticle)

    def remove_particle(self, row, col):
        self.grid.remove_particle(row, col)

    def update(self):
        for row in range(self.grid.rows-2, -1, -1):
            for col in range(self.grid.columns):
                particle = self.grid.get_cell(row, col)
                if particle is not None:
                    new_pos = particle.update(self.grid, row, col)
                    if new_pos != (row, col):
                        self.grid.set_cell(new_pos[0], new_pos[1], particle)
                        self.grid.remove_particle(row, col)
    
    def restart(self):
        self.grid.clear()

    def handle_key(self, event):
        if event.key == pygame.K_SPACE:
            self.restart()
        elif event.key == pygame.K_0:
            print("Eraser Selected")
        elif event.key == pygame.K_1:
            print("Sand Particle Selected")
        elif event.key == pygame.K_2:
            print("Rock Particle Selected")

    def handle_mouse(self):
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            pos = pygame.mouse.get_pos()
            row = pos[1] // self.cell_size
            col = pos[0] // self.cell_size
            self.add_particle(row, col)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key(event)

        self.handle_mouse()