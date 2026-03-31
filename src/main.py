"""Main file to run for gameplay"""

import pygame
from selection import run_selection
from gameover_screen import run_game_over
from highscore import load_highscore, check_and_update_highscore
from run import run_flappy
from sound import update_background_music
from pathlib import Path

ASSETS_PATH = Path(__file__).parents[1] / "assets"


class GameInitializer:
    """
    Responsible for initializing the global game system.
    """

    @staticmethod
    def initialize():
        """Initializes pygame, sound system and highscore."""
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load(ASSETS_PATH / "sounds" / "background_music.wav")
        pygame.mixer.music.set_volume(0.1)


class Game:
    """Controls game loop (selection, starting, gameover, ..."""

    def __init__(self):
        """Saves last selected animal for replay."""
        self.last_animal = None

        GameInitializer.initialize()

    def run(self):
        """Runs main game loop"""
        update_background_music()

        while True:
            if self.last_animal is None:
                choice = run_selection()
                self.last_animal = choice
            else:
                choice = self.last_animal

            update_background_music()

            score = run_flappy(choice)

            check_and_update_highscore(score)

            action, self.last_animal = run_game_over(score, choice)

            if action == "BACK_TO_MENU":
                self.last_animal = None


if __name__ == "__main__":
    """Entry point for game: Initializes systems"""
    game = Game()
    game.run()
