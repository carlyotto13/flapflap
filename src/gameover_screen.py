# gameover screen

import pygame
from sys import exit
from screen import Screen
from settings import GAME_WIDTH, GAME_HEIGHT
import highscore


def run_game_over(score, last_animal):
    pygame.init()
    window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    clock = pygame.time.Clock()

    # Screen Setup mit Settings-Button
    screen = Screen(
        window,
        background_path='../assets/starting_screen/start_background.png',
        block_image_path='../assets/starting_screen/start_block.png',
        show_settings=False
    )

    # Blöcke mit Text und optionaler Schriftgröße
    labels = [
        "GAME OVER",
        f"Highscore: {highscore.highscore}\nYour Score: {score}",
        "TRY AGAIN",
        "BACK TO MENU"
    ]
    font_scales = [1.0, 0.5, 0.7, 0.7]

    screen.add_blocks(labels, start_y=GAME_HEIGHT*2/5, spacing=90, font_scales=font_scales)

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
                        # Wir nehmen nur den ersten Eintrag jeder Zeilenliste zum Checken
                        first_line = lines[0]
                        if first_line == "TRY AGAIN":
                            return "TRY_AGAIN", last_animal
                        if first_line == "BACK TO MENU":
                            return "BACK_TO_MENU", None

            if event.type == CLOUD_EVENT:
                screen.create_cloud()

        screen.draw()  # Alles: Hintergrund, Blöcke, Text, Wolken, Settings
        screen.move_clouds(speed=-2)
        pygame.display.update()
        clock.tick(60)