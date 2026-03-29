import pygame
from selection_screen_updated import run_selection
from gameover_screen import run_game_over
from highscore import load_highscore, check_and_update_highscore
from run import run_flappy
from sound import update_background_music


class GameInitializer:
    @staticmethod
    def initialize():
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load("../assets/sounds/background_music.wav")
        pygame.mixer.music.set_volume(0.1)


class Game:
    def __init__(self):
        self.last_animal = None

        GameInitializer.initialize()

    def run(self):
        update_background_music()

        while True:
            # TODO: None check always with is
            if self.last_animal is None:
                choice = run_selection()
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
    game = Game()
    game.run()
