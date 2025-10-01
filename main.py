import pygame
from simulation import *


pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 120
GREY = (29, 29, 29)
CELL_SIZE = 6
BRUSH_SIZE = 3

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand Sim")

clock = pygame.time.Clock()
sim = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE, BRUSH_SIZE)

# Simulation loop
while True:
    # 1. Check Event
    sim.handle_events()

    # 2. Update Grid
    sim.update()

    # 3. Draw Grid
    window.fill(GREY)
    sim.draw(window)

    pygame.display.flip()
    clock.tick(FPS)