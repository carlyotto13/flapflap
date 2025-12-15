# world.py
import pygame
from obstacle import Obstacle
from animal import Animal
from game import GameIndicator
from settings import W, H, obstacle_size, obstacle_gap, obstacle_pair_sizes
import random

class World:
    def __init__(self, screen):
        self.screen = screen
        self.world_shift = 0
        self.current_x = 0
        self.gravity = 0.5
        self.current_obstacle = None
        self.obstacles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self._generate_world()
        self.playing = False
        self.game_over = False
        self.passed = True
        self.game = GameIndicator(screen)

    # adds obstacle once the last obstacle added reached the desired obstacle horizontal spaces
    def _add_obstacle(self):
        obstacle_pair_size = random.choice(obstacle_pair_sizes)
        top_obstacle_height, bottom_obstacle_height = obstacle_pair_size[0] * obstacle_size, obstacle_pair_size[1] * obstacle_size
        obstacle_top = Obstacle((W, 0 - (bottom_obstacle_height + obstacle_gap)), obstacle_size, H, True)
        obstacle_bottom = Obstacle((W, top_obstacle_height + obstacle_gap), obstacle_size, H, False)
        self.obstacles.add(obstacle_top)
        self.obstacles.add(obstacle_bottom)
        self.current_obstacle = obstacle_top

    # creates the player and the obstacle
    def _generate_world(self):
        self._add_obstacle()
        animal = Animal((W//2 - obstacle_size, H//2 - obstacle_size), 30)
        self.player.add(animal)