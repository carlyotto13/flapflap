import pygame
from sys import exit
from miu_screen import Screen
from miu_settings import GAME_WIDTH, GAME_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, CIRCLE_WIDTH, CIRCLE_HEIGHT, \
    SETTINGS_BUTTON_WIDTH, SETTINGS_BUTTON_HEIGHT, BLOCK_WIDTH, SOUND_SETTINGS


def run_settings():
    pygame.init()
    window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    clock = pygame.time.Clock()

    screen = Screen(window, '../assets/starting_screen/start_background.png', block_image_path='../assets/starting_screen/start_block.png', show_settings=False)

    # Buttons und Circles
    button_image = pygame.image.load("../assets/settings_screen/button.png")
    button_image = pygame.transform.scale(button_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

    circle_image = pygame.image.load("../assets/settings_screen/circle.png")
    circle_image = pygame.transform.scale(circle_image, (CIRCLE_WIDTH, CIRCLE_HEIGHT))

    button_status = [
        SOUND_SETTINGS.get("background", True),
        SOUND_SETTINGS.get("game", True)
    ]

    # Back-Button
    back_button_image = pygame.image.load("../assets/settings_screen/back_button.png")
    back_button_image = pygame.transform.scale(back_button_image, (SETTINGS_BUTTON_WIDTH, SETTINGS_BUTTON_HEIGHT))
    back_button_rect = back_button_image.get_rect(topright=(GAME_WIDTH - 20, 20))



    # Anzeige-Labels mit Zeilen und Skalierung
    labels = [
        (["SETTINGS"]),
        (["BACKGROUND SOUND"]),
        (["GAME SOUND"])
    ]

    font_scales = [1.0, 0.55, 0.55]

    screen.add_blocks(labels, start_y=GAME_HEIGHT*2/5, spacing=90, x_positions=[GAME_WIDTH/4 ,GAME_WIDTH/8 , GAME_WIDTH/8], font_scales= font_scales)

    CLOUD_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOUD_EVENT, 3000)

    # Button-Rechtecke erstellen
    button_rects = []
    circle_rects = []

    # x-Offset rechts neben Block
    x_offset = BLOCK_WIDTH + 20

    # Die unteren drei Blöcke
    for i in range(1, 3):
        block_rect, _, _ = screen.blocks[i]

        # Button-Rechteck rechts vom Block
        b_rect = button_image.get_rect(
            midleft=(block_rect.right + 20, block_rect.centery)
        )
        button_rects.append(b_rect)

        # Circle-Rechteck
        circle_rects.append(circle_image.get_rect())


    font = pygame.font.SysFont("Comic Sans MS", 18)

    while True:

        # ---------- EVENTS ----------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == CLOUD_EVENT:
                screen.create_cloud()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Back-Button
                if back_button_rect.collidepoint(pos):
                    return

                # Button-Klicks
                for i in range(2):
                    if button_rects[i].collidepoint(pos):
                        # Status umschalten
                        button_status[i] = not button_status[i]

                        # ⚡ Sound-Einstellungen aktualisieren
                        if i == 0:  # Hintergrundmusik
                            SOUND_SETTINGS["background"] = button_status[i]
                            from miu_sound import update_background_music
                            update_background_music()  # sofort reagieren

                        elif i == 1:  # Game-Sounds
                            SOUND_SETTINGS["game"] = button_status[i]

        # ---------- ZEICHNEN ----------
        screen.draw()

        for i in range(2):

            # 1️⃣ Button zeichnen (WICHTIG!)
            screen.window.blit(button_image, button_rects[i])

            # 2️⃣ Circle-Position setzen
            if button_status[i]:  # ON → rechts
                circle_rects[i].midright = (
                    button_rects[i].right - 8,
                    button_rects[i].centery
                )
            else:  # OFF → links
                circle_rects[i].midleft = (
                    button_rects[i].left + 8,
                    button_rects[i].centery
                )

            # 3️⃣ Circle zeichnen
            screen.window.blit(circle_image, circle_rects[i])

            # 4️⃣ Status-Text
            status_text = font.render(
                "ON" if button_status[i] else "OFF",
                True,
                (255, 255, 255)
            )
            text_rect = status_text.get_rect(
                midleft=(button_rects[i].right + 10, button_rects[i].centery)
            )
            screen.window.blit(status_text, text_rect)

            screen.window.blit(circle_image, circle_rects[i])

        screen.window.blit(back_button_image, back_button_rect)

        screen.move_clouds(speed=-2)

        pygame.display.update()
        clock.tick(60)

