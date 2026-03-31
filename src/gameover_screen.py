"""Creates the game over screen."""

import pygame
from sys import exit
from screen import Screen
from settings import GAME_WIDTH, GAME_HEIGHT
from highscore import load_highscore
from pathlib import Path

ASSETS_PATH = Path(__file__).parents[1] / "assets"


def run_game_over(score: float, last_animal:str) -> tuple[str,str | None]:
    """
    Displays game over screen and handles player interactions.
    Restart game or return to menu
    Shows players score and highscore
    """
    pygame.init()
    window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    #clock = pygame.time.Clock()
    clock: pygame.time.Clock = pygame.time.Clock()

    # Screen Setup
    screen = Screen(
        window,
        background_path=ASSETS_PATH / "starting_screen" / "start_background.png",
        block_image_path=ASSETS_PATH / "starting_screen" / "start_block.png",
        show_settings=False,
    )

    # labels for blocks and font size
    highscore = load_highscore()
    labels = [
        "GAME OVER",
        f"Highscore: {highscore}\nYour Score: {score}",
        "TRY AGAIN",
        "BACK TO MENU",
    ]
    font_scales = [1.0, 0.5, 0.7, 0.7]

    screen.add_blocks(
        labels, start_y=GAME_HEIGHT * 2 / 5, spacing=90, font_scales=font_scales
    )

    # Cloud-Event
    CLOUD_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOUD_EVENT, 3000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    return "TRY_AGAIN", last_animal

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for rect, lines, _ in screen.blocks:
                    if rect.collidepoint(pos):
                        first_line = lines[0]
                        if first_line == "TRY AGAIN":
                            return "TRY_AGAIN", last_animal
                        if first_line == "BACK TO MENU":
                            return "BACK_TO_MENU", None

            if event.type == CLOUD_EVENT:
                screen.create_cloud()

        screen.draw()  # draws background, blocks, buttons, clouds
        screen.move_clouds(speed=-2)
        pygame.display.update()
        clock.tick(60)
