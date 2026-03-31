"""Creates background and buttons on screen."""

import pygame
import random
from settings import (
    GAME_WIDTH,
    GAME_HEIGHT,
    BLOCK_WIDTH,
    BLOCK_HEIGHT,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    CIRCLE_WIDTH,
    CIRCLE_HEIGHT,
    TEXT_FONT_SIZE,
    SETTINGS_BUTTON_WIDTH,
    SETTINGS_BUTTON_HEIGHT,
)
from pathlib import Path

ASSETS_PATH = Path(__file__).parents[1] / "assets"


class Screen:
    """
    Screen renderer
    draws background, clouds, buttons, ...
    """

    def __init__(
        self,
        window,
        background_path,
        blocks=None,
        block_image_path=None,
        show_settings=True,
    ):
        """Initializes screen layout."""
        self.window = window
        self.background = pygame.image.load(background_path)

        self.block_image = None
        if block_image_path:
            img = pygame.image.load(block_image_path)
            self.block_image = pygame.transform.scale(img, (BLOCK_WIDTH, BLOCK_HEIGHT))

        self.blocks = blocks if blocks else []

        self.clouds = []
        self.cloud_image = pygame.image.load(
            ASSETS_PATH / "starting_screen" / "start_obstacle.png"
        )
        self.cloud_image = pygame.transform.scale(self.cloud_image, (209, 120))

        self.settings_image = pygame.image.load(
            ASSETS_PATH / "settings_screen" / "seetings_button.png"
        )
        self.settings_image = pygame.transform.scale(
            self.settings_image, (SETTINGS_BUTTON_WIDTH, SETTINGS_BUTTON_HEIGHT)
        )

        self.show_settings = show_settings
        if self.show_settings:
            self.settings_image = pygame.image.load(
                ASSETS_PATH / "settings_screen" / "seetings_button.png"
            )
            self.settings_image = pygame.transform.scale(
                self.settings_image, (SETTINGS_BUTTON_WIDTH, SETTINGS_BUTTON_HEIGHT)
            )
            self.settings_rect = self.settings_image.get_rect()
            self.settings_rect.topright = (GAME_WIDTH - 20, 20)

    def add_blocks(self, labels, start_y, spacing, x_positions=None, font_scales=None):
        """Create interactive blocks with text (buttons)"""
        self.blocks = []
        for i, label in enumerate(labels):
            if x_positions:
                x = x_positions[i]
            else:
                x = (GAME_WIDTH - BLOCK_WIDTH) / 2

            y = start_y + i * spacing
            rect = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)

            scale = font_scales[i] if font_scales else 1

            if isinstance(label, str):  # split string in case of line breaks
                lines = label.split("\n")
            else:
                lines = label
            self.blocks.append((rect, lines, scale))

    def create_cloud(self):
        """Creates decorative cloud."""
        cloud_y = random.uniform(GAME_HEIGHT / 4, GAME_HEIGHT * 3 / 4)
        cloud_rect = pygame.Rect(GAME_WIDTH, cloud_y, 209, 120)
        self.clouds.append((cloud_rect, self.cloud_image))

    def move_clouds(self, speed):
        """Moves cloud horizontally."""
        for cloud, img in self.clouds:
            cloud.x += speed
        self.clouds = [(c, img) for c, img in self.clouds if c.x + c.width > 0]

    def draw(self):
        """Render screen: background, buttons, clouds"""
        self.window.blit(self.background, (0, 0))
        if self.show_settings:
            self.window.blit(self.settings_image, self.settings_rect)
        for cloud, img in self.clouds:
            self.window.blit(img, cloud)
        for rect, label, scale in self.blocks:
            if self.block_image:
                self.window.blit(self.block_image, rect)

            scaled_size = int(TEXT_FONT_SIZE * scale)
            font = pygame.font.SysFont("Comic Sans MS", scaled_size)

            scaled_size = int(TEXT_FONT_SIZE * scale)
            font = pygame.font.SysFont("Comic Sans MS", scaled_size)
            line_height = font.get_height()
            total_height = line_height * len(label)

            for i, line in enumerate(label):
                if not isinstance(line, str):
                    line = str(line)

                text_surface = font.render(line, True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.centerx = rect.centerx
                text_rect.y = rect.centery - total_height / 2 + i * line_height
                self.window.blit(text_surface, text_rect)
