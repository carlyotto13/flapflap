"""Creates character and regulates it's movements."""

import pygame
from settings import (
    FROG_START_X,
    FROG_START_Y,
    FROG_WIDTH,
    FROG_HEIGHT,
    GRAVITY,
    JUMP_STRENGTH,
    GAME_HEIGHT,
)


class Player:
    """
    Represents the selected player-controlled character.
    """

    def __init__(self, image_path, config):
        """Load player and initialize variables."""
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (FROG_WIDTH, FROG_HEIGHT))
        self.rect = pygame.Rect(FROG_START_X, FROG_START_Y, FROG_WIDTH, FROG_HEIGHT)
        self.velocity_y = 0
        self.alive = True

    def jump(self):
        """Upward force to simulate jump"""
        self.velocity_y = JUMP_STRENGTH

    def update(self):
        """Apply Gravity and update vertical position of player."""
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        self.rect.y = max(self.rect.y, 0)

        if self.rect.y > GAME_HEIGHT:
            self.alive = False

    def draw(self, window):
        """Draw player."""
        window.blit(self.image, self.rect)
