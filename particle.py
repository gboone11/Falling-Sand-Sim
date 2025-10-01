import random
import colorsys

class SandParticle(object):
    def __init__(self):
        self.color = random_color((0.1,0.12), (0.5,0.7), (0.7,0.9))
    
    def update(self, grid, row, col):
        if grid.is_cell_empty(row+1, col):
            return row + 1, col
        else:
            offsets = [-1,1]
            random.shuffle(offsets)
            for offset in offsets:
                if grid.is_cell_empty(row+1, col+offset):
                    return row+1, col+offset
                
        return row, col
    
class RockParticle(object):
    def __init__(self):
        self.color = random_color((0.0,0.1), (0.1,0.3), (0.3,0.5))

    def update(self, grid, row, col):
        return row, col

def random_color(hue_range, saturation_range, value_range):
    hue = random.uniform(*hue_range)
    saturation = random.uniform(*saturation_range)
    value = random.uniform(*value_range)

    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
    return int(r*255), int(g*255), int(b*255)