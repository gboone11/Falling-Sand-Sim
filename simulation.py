import pygame, sys
from grid import *
from particle import *
import random

class Simulation(object):
    def __init__(self, width, height, cell_size, brush_size):
        self.grid = Grid(width, height, cell_size)
        self.cell_size = cell_size
        self.mode = "sand"
        self.brush_size = brush_size

    def draw(self, window):
        self.grid.draw(window)
        self.draw_brush(window)

    def add_particle(self, row, col):
        if self.mode == "sand":
            if random.random() < 0.15:
                self.grid.add_particle(row, col, SandParticle)
        elif self.mode == "rock":
            self.grid.add_particle(row, col, RockParticle)


    def remove_particle(self, row, col):
        self.grid.remove_particle(row, col)

    def update(self):
        for row in range(self.grid.rows-2, -1, -1):
            if row % 2 == 0:
                column_range = range(self.grid.columns)
            else:
                column_range = reversed(range(self.grid.columns))
                
            for col in column_range:
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
            self.mode = "erase"
        elif event.key == pygame.K_1:
            self.mode = "sand"
        elif event.key == pygame.K_2:
            self.mode = "rock"

    def handle_mouse(self):
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            pos = pygame.mouse.get_pos()
            row = pos[1] // self.cell_size
            col = pos[0] // self.cell_size

            self.apply_brush(row, col)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key(event)

        self.handle_mouse()

    def apply_brush(self, row, col):
        for r in range(self.brush_size):
            for c in range(self.brush_size):
                if self.mode == "erase":
                    self.remove_particle(row+r, col+c)
                else:
                    self.add_particle(row+r, col+c)

    def draw_brush(self, window):
        mouse_pos = pygame.mouse.get_pos()
        col = mouse_pos[0] // self.cell_size
        row = mouse_pos[1] // self.cell_size

        brush_size_visual = self.brush_size * self.cell_size
        color = (255, 255, 255)

        if self.mode == "rock":
            color = (100, 100, 100)
        elif self.mode == "sand":
            color = (185, 142, 100)
        elif self.mode == "erase":
            color = (255, 105, 180)

        pygame.draw.rect(window, color, (col*self.cell_size, row*self.cell_size, brush_size_visual, brush_size_visual))