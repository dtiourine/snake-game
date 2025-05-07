import pygame
import math
import random
from pygame import Rect

class Food:
    def __init__(self, screen, food_width: int = 20, food_height: int = 20):
        random_x = math.floor(random.uniform(50, (screen.get_width() - 49)))
        random_y = math.floor(random.uniform(50, (screen.get_height() - 49)))
        self.screen = screen
        self.food_width = food_width
        self.food_height = food_height
        self.item = Rect(random_x, random_y, self.food_width, self.food_height)

    def move(self):
        random_x = math.floor(random.uniform(50, (self.screen.get_width() - 49)))
        random_y = math.floor(random.uniform(50, (self.screen.get_height() - 49)))
        pygame.Rect.update(self.item, random_x, random_y, self.food_width, self.food_height)








