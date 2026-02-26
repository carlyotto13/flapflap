import pygame
from selection_screen_updated import run_selection
from gameover_screen import run_game_over
import highscore
from run import run_flappy
from sound import update_background_music


class GameInitializer:
    @staticmethod
    def initialize():
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load("../assets/sounds/background_music.wav")
        pygame.mixer.music.set_volume(0.1)

        highscore.load_highscore()


class MainGameLoop:
    def __init__(self):
        self.last_animal = None

    def run(self):
        update_background_music()

        while True:
            # Startscreen oder zurück zum Menü
            if not self.last_animal:
                choice = run_selection()
                self.last_animal = choice
            else:
                choice = self.last_animal

            update_background_music()

            # Tier-Spiel starten
            score = run_flappy(choice)

            # Game Over Screen
            highscore.update_highscore(score)
            action, self.last_animal = run_game_over(score, choice)

            # Entscheidung auswerten
            if action == "BACK_TO_MENU":
                self.last_animal = None


if __name__ == "__main__":
    GameInitializer.initialize()
    game = MainGameLoop()
    game.run()