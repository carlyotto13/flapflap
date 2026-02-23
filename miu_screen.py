import pygame
import random
from miu_settings import GAME_WIDTH, GAME_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT, TEXT_FONT_SIZE

class Screen:
    def __init__(self, window, background_path, blocks=None, block_image_path=None):
        self.window = window
        self.background = pygame.image.load(background_path)
        self.font = pygame.font.SysFont("Comic Sans MS", TEXT_FONT_SIZE)

        # Block-Bild laden, falls vorhanden
        self.block_image = None
        if block_image_path:
            img = pygame.image.load(block_image_path)
            self.block_image = pygame.transform.scale(img, (BLOCK_WIDTH, BLOCK_HEIGHT))

        # Blöcke: Liste von (Label, pygame.Rect)
        self.blocks = blocks if blocks else []

        # Wolken (optional)
        self.clouds = []
        self.cloud_image = pygame.image.load('assets/starting_screen/start_obstacle.png')
        self.cloud_image = pygame.transform.scale(self.cloud_image, (209, 120))

    def add_blocks(self, labels, start_y, spacing):
        self.blocks = []
        for i, label in enumerate(labels):
            x = (GAME_WIDTH - BLOCK_WIDTH)/2
            y = start_y + i * spacing
            rect = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
            self.blocks.append((rect, label))

    def create_cloud(self):
        cloud_y = random.uniform(GAME_HEIGHT / 4, GAME_HEIGHT * 3 / 4)
        cloud_rect = pygame.Rect(GAME_WIDTH, cloud_y, 209, 120)
        self.clouds.append((cloud_rect, self.cloud_image))

    def move_clouds(self, speed):
        for cloud, img in self.clouds:
            cloud.x += speed
        self.clouds = [(c, img) for c, img in self.clouds if c.x + c.width > 0]

    def draw(self):
        self.window.blit(self.background, (0, 0))
        for cloud, img in self.clouds:
            self.window.blit(img, cloud)
        for rect, label in self.blocks:
            if self.block_image:
                self.window.blit(self.block_image, rect)
            text = self.font.render(label, True, (255, 255, 255))
            text_rect = text.get_rect(center=rect.center)
            self.window.blit(text, text_rect)