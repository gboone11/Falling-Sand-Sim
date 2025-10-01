import random
import colorsys
from grid import *

class SandParticle(object):
    def __init__(self) -> None:
        """initialize Sandparticle object
        """
        self.color = random_color((0.1,0.12), (0.5,0.7), (0.7,0.9))
    
    def update(self, grid: Grid, row: int, col: int) -> tuple:
        """defines movement of SandParticle
        moves down if none below and moves left or right if can't move down

        :param Grid grid: Grid object particle is moving in
        :param int row: row particle is in
        :param int col: column particle is in
        :return tuple: (row, col) particle will move to
        """
        if grid.is_cell_empty(row+1, col):
            # if cell below is empty, move down
            return row + 1, col
        else:
            # if cell below is occupied, iterate through offset list and move to open cell in offset list
            offsets = [-1,1]
            random.shuffle(offsets)
            for offset in offsets:
                if grid.is_cell_empty(row+1, col+offset):
                    return row+1, col+offset
                
        return row, col
    
class RockParticle(object):
    def __init__(self) -> None:
        """initialize RockParticle object
        """
        self.color = random_color((0.0,0.1), (0.1,0.3), (0.3,0.5))

    def update(self, grid: Grid, row: int, col: int) -> None:
        """defines movement of RockParticle
        RockParticle does not move

        :param Grid grid: kept for generic use of update method
        :param int row: row particle is in
        :param int col: column particle is in
        :return tuple: (row, col) particle will move to
        """
        return row, col

def random_color(hue_range: tuple, saturation_range: tuple, value_range: tuple) -> tuple:
    """returns random color in hsv range given

    :param tuple hue_range: (lower, uppper) range for hue
    :param tuple saturation_range: (lower, uppper) range for saturation
    :param tuple value_range: (lower, uppper) range for value
    :return tuple: random color in rgb
    """
    hue = random.uniform(*hue_range)
    saturation = random.uniform(*saturation_range)
    value = random.uniform(*value_range)

    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
    return int(r*255), int(g*255), int(b*255)