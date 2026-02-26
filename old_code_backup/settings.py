# settings
from os import walk
import pygame

W, H = 600, 650 # width and height

obstacle_pair_sizes = [
    (1, 7),
    (2, 6),
    (3, 5),
    (4, 4),
    (5, 3),
    (6, 2),
    (7, 1)
]
obstacle_size = H // 10
obstacle_gap = (obstacle_size * 2) + (obstacle_size // 2)
ground_space = 50

def import_sprite(path):
    surface_list = []
    for _, __, img_file in walk(path):
        for image in img_file:
            full_path = f"{path}/{image}"
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)
    return surface_list