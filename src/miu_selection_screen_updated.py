import pygame
from sys import exit
from miu_screen import Screen
from miu_settings import GAME_WIDTH, GAME_HEIGHT
from miu_run import run_flappy
from miu_setting_screen import run_settings

def run_selection():
    pygame.init()
    window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    clock = pygame.time.Clock()


    labels = ["FROG", "HAMSTER", "PENGUIN", "DOG"]
    screen = Screen(
        window,
        '../assets/starting_screen/start_background.png',
        block_image_path='../assets/starting_screen/start_block.png',
        show_settings=True
    )
    screen.add_blocks(
        labels,
        start_y=GAME_HEIGHT * 2 / 5,
        spacing=90
    )


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