# main.py
from miu_selection_screen_updated import run_selection
#from miu_animals.miu_frog import run_frog
from miu_gameover_screen import run_game_over
import miu_highscore
from miu_run import run_flappy
import pygame
from miu_sound import update_background_music

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("../assets/sounds/background_music.wav")
pygame.mixer.music.set_volume(0.1)  # 0.0 - 1.0

# Highscore beim Programmstart laden
miu_highscore.load_highscore()

if __name__ == "__main__":
    last_animal = None
    update_background_music()

    while True:
        #Startscreen oder zurück zum Menü
        if not last_animal:
            choice = run_selection()  # z.B. "FROG"
            last_animal = choice

            if choice == "SETTINGS":
                run_settings()
                update_background_music()
                continue  # zurück zum Startscreen nach Settings

        else:
            choice = last_animal

        update_background_music()

        #Tier-Spiel starten
        score = run_flappy(choice)

        #Game Over Screen
        miu_highscore.update_highscore(score)
        action, last_animal = run_game_over(score, choice)

        #Entscheidung auswerten
        if action == "BACK_TO_MENU":
            last_animal = None  #   Auswahl wieder möglich

