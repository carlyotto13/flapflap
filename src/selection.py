"""Responsible for selection of character."""

import pygame
from sys import exit
from screen import Screen
from settings import GAME_WIDTH, GAME_HEIGHT
from run import run_flappy
from setting_screen import run_settings
from pathlib import Path

ASSETS_PATH = Path(__file__).parents[1] / "assets"


def run_selection():
    """Initializes the selection screen."""
    # pygame.init()
    window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    clock = pygame.time.Clock()

    labels = ["FROG", "HAMSTER", "PENGUIN", "DOG"]
    screen = Screen(
        window,
        background_path=ASSETS_PATH / "starting_screen" / "start_background.png",
        block_image_path=ASSETS_PATH / "starting_screen" / "start_block.png",
        show_settings=True,
    )
    screen.add_blocks(labels, start_y=GAME_HEIGHT * 2 / 5, spacing=90)

    CLOUD_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOUD_EVENT, 3000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for rect, label, scale in screen.blocks:
                    if rect.collidepoint(pos):
                        run_flappy(label[0])
                if screen.settings_rect.collidepoint(pos):
                    run_settings()
            if event.type == CLOUD_EVENT:
                screen.create_cloud()

        screen.move_clouds(speed=-2)
        screen.draw()
        pygame.display.update()
        clock.tick(60)
