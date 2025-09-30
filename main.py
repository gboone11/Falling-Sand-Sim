import pygame
import sys
from grid import *
from particle import *

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 120
GREY = (29, 29, 29)
CELL_SIZE = 20

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand Sim")

clock = pygame.time.Clock()
grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
grid.cells[0][0] = SandParticle()
grid.cells[3][2] = SandParticle()

# Simulation loop
while True:

    # 1. Check Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Update Grid

    # 3. Draw Grid
    window.fill(GREY)
    grid.draw(window)

    pygame.display.flip()
    clock.tick(FPS)