"""TODO."""

# TODO refactor the name to not include updated
#  remeber you have git for version control ;)
import pygame
from sys import exit
from screen import Screen
from run import run_flappy
from setting_screen import run_settings
from settings import GAME_HEIGHT


def run_selection(window: pygame.Surface):
    # pygame.init()  # TODO unnecessary. this will only run from the MenuRunner and
    #  there pygame is initialized

    # TODO: you init a new window every time - thus objects are potentially rendered to
    #  different apps.
    # window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

    # TODO: you dont need a clock here. You dont need a frame rate limit in the menu
    #  The clocks will be asps if you rm the clock
    # clock = pygame.time.Clock()

    labels = ["FROG", "HAMSTER", "PENGUIN", "DOG"]
    # TODO: use Path - and import it from Settings ASSETS_DIR
    screen = Screen(
        window,
        "../assets/starting_screen/start_background.png",
        block_image_path="../assets/starting_screen/start_block.png",
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
        # clock.tick(60)
