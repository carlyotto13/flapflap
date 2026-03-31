"""Responsible for pipe creation, movement and collision."""

import pygame
import random
from settings import PIPE_WIDTH, PIPE_HEIGHT, PIPE_OPENING_SPACE, PIPE_SPEED, GAME_WIDTH


class Pipe(pygame.Rect):
    """
    Represents a single pipe in the game.
    """

    def __init__(self, img, x, y, pipe_type):
        """Initializes a new Pipe object."""
        super().__init__(x, y, PIPE_WIDTH, PIPE_HEIGHT)
        self.img = img
        self.passed = False
        self.type = pipe_type

    def draw(self, window):
        """Draw a pipe."""
        window.blit(self.img, self)


class PipeManager:
    """Controls creation and collision of pipes."""

    def __init__(self, obstacle_image_path):
        """Load pipe assets."""
        self.obstacle_image = pygame.image.load(obstacle_image_path)
        self.obstacle_image = pygame.transform.scale(
            self.obstacle_image, (PIPE_WIDTH, PIPE_HEIGHT)
        )
        self.bottom_image = pygame.transform.rotate(self.obstacle_image, 180)
        self.pipes = []

    def create_pipes(self):
        """Creates new pipes."""
        random_pipe_y = -PIPE_HEIGHT / 4 - random.random() * (PIPE_HEIGHT / 2)
        top = Pipe(self.obstacle_image, GAME_WIDTH, random_pipe_y, "top")
        bottom = Pipe(
            self.bottom_image,
            GAME_WIDTH,
            random_pipe_y + PIPE_HEIGHT + PIPE_OPENING_SPACE,
            "bottom",
        )
        self.pipes.extend([top, bottom])

    def update(self):
        """Moves pipes and removes offscreen pipes."""
        for pipe in self.pipes:
            pipe.x += PIPE_SPEED

        while self.pipes and self.pipes[0].x < -PIPE_WIDTH:
            self.pipes.pop(0)

    def check_collision(self, player):
        """Check if player collides with pipes."""
        for pipe in self.pipes:
            if player.rect.colliderect(pipe):
                return True
        return False
