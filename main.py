import pygame
import sys
from simulation import *


pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 120
GREY = (29, 29, 29)
CELL_SIZE = 20

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand Sim")

clock = pygame.time.Clock()
sim = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation loop
while True:

    # 1. Check Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        pos = pygame.mouse.get_pos()
        row = pos[1] // CELL_SIZE
        col = pos[0] // CELL_SIZE
        sim.add_particle(row, col)
    # 2. Update Grid

    # 3. Draw Grid
    window.fill(GREY)
    sim.draw(window)

    pygame.display.flip()
    clock.tick(FPS)