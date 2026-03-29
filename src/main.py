import pygame
from selection_screen_updated import run_selection
from gameover_screen import run_game_over
from highscore import check_and_update_highscore
from run import run_flappy
from sound import update_background_music
from settings import GAME_WIDTH, GAME_HEIGHT


class GameInitializer:
    @staticmethod
    def initialize():
        pygame.init()
        pygame.mixer.init()

        # TODO use Path and get from settings file
        pygame.mixer.music.load("../assets/sounds/background_music.wav")
        pygame.mixer.music.set_volume(0.1)


class MenuRunner:
    def __init__(self):
        self.last_animal = None

        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

    def run(self):
        update_background_music()

        while True:
            # TODO: None check always with is
            if self.last_animal is None:
                choice = run_selection(self.window)
                self.last_animal = choice
            else:
                choice = self.last_animal

            # TODO: why call again?
            update_background_music()

            score = run_flappy(choice)

            check_and_update_highscore(score)

            action, self.last_animal = run_game_over(score, choice)

            # Entscheidung auswerten
            if action == "BACK_TO_MENU":
                self.last_animal = None


if __name__ == "__main__":
    GameInitializer.initialize()
    menu = MenuRunner()
    menu.run()
