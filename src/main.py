"""Main file to run for gameplay"""

import pygame
from selection import run_selection
from gameover_screen import run_game_over
from highscore import check_and_update_highscore
from run import run_flappy
from sound import update_background_music
from pathlib import Path
from settings import GAME_WIDTH, GAME_HEIGHT

ASSETS_PATH = Path(__file__).parents[1] / "assets"


class GameInitializer:
    """
    Responsible for initializing the global game system.
    """

    @staticmethod
    def initialize() -> None:
        """Initializes pygame, sound system and highscore."""
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load(ASSETS_PATH / "sounds" / "background_music.wav")
        pygame.mixer.music.set_volume(0.1)


class MenuRunner:
    last_animal: str | None
    window: pygame.Surface
    """Controls game loop (selection, starting, gameover, ..."""

    def __init__(self) -> None:
        """Saves last selected animal for replay."""
        self.last_animal = None

        #GameInitializer.initialize()
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

    def run(self) -> None:
        """Runs main game loop"""
        update_background_music()

        while True:
            if self.last_animal is None:
                choice = run_selection(self.window)
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
    #game = Game()
    #game.run()
    GameInitializer.initialize()
    menu = MenuRunner()
    menu.run()
