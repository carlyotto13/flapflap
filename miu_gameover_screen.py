import pygame
from sys import exit
from miu_screen import Screen
from miu_settings import GAME_WIDTH, GAME_HEIGHT
import random
from miu_highscore import highscore

def run_game_over(score, last_animal):
    pygame.init()
    window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    clock = pygame.time.Clock()

    # Screen Setup
    screen = Screen(
        window,
        background_path='assets/starting_screen/start_background.png',
        block_image_path='assets/starting_screen/start_block.png'
    )

    # Klick-Labels (einfach für Mouse-Events)
    click_labels = ["GAME OVER", "Highscore", "TRY AGAIN", "BACK TO MENU"]
    screen.add_blocks(click_labels, start_y=GAME_HEIGHT*2/5, spacing=90)

    # Anzeige-Labels mit Zeilen und Skalierung
    display_labels = [
        (["GAME OVER"], 1.0),
        ([f"Highscore: {highscore}", f"Your Score: {score}"], 0.5),
        (["TRY AGAIN"], 0.7),
        (["BACK TO MENU"], 0.7)
    ]

    # Schriftgrößen speichern
    block_fonts = [pygame.font.SysFont("Comic Sans MS", int(30*scale)) for _, scale in display_labels]

    # Cloud-Event
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
                for rect, label in screen.blocks:
                    if rect.collidepoint(pos):
                        if label == "TRY AGAIN":
                            return "TRY_AGAIN", last_animal
                        if label == "BACK TO MENU":
                            return "BACK_TO_MENU", None
            if event.type == CLOUD_EVENT:
                screen.create_cloud()

        # Hintergrund
        window.blit(screen.background, (0, 0))

        # Wolken zeichnen
        for cloud, img in screen.clouds:
            window.blit(img, cloud)

        # Blöcke zeichnen und Text (mehrzeilig) rendern
        for i, (rect, _) in enumerate(screen.blocks):
            if screen.block_image:
                window.blit(screen.block_image, rect)

            lines, scale = display_labels[i]
            font = pygame.font.SysFont("Comic Sans MS", int(30 * scale))
            line_height = font.get_height()
            total_height = line_height * len(lines)

            for j, line in enumerate(lines):
                text = font.render(line, True, (255, 255, 255))
                text_rect = text.get_rect(
                    center=(
                        rect.centerx,
                        rect.centery - total_height / 2 + j * line_height + line_height / 2
                    )
                )
                window.blit(text, text_rect)

        # Wolken bewegen
        screen.move_clouds(speed=-2)

        pygame.display.update()
        clock.tick(60)