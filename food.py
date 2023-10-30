import pygame
import random

snake_speed = 4
cell_size = 40
grid_width = 32
grid_height = 28
screen_width = cell_size * grid_width
screen_height = cell_size * grid_height

class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*cell_size, random.randint(0, grid_height-1)*cell_size)

    def draw_food(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (cell_size, cell_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)