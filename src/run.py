"""responsible for game loop and game mechanics"""

import pygame
from sys import exit
from settings import GAME_WIDTH, GAME_HEIGHT
from gameover_screen import run_game_over
from highscore import check_and_update_highscore
from animals import ANIMALS
from player import Player
from pipes import PipeManager
from sound import SoundManager
from game_state import GameState
from score import ScoreManager


class FlappyBirdGame:
    """
    Main game controller
    Handles game loop
    """

    def __init__(self, animal_key):
        """
        Setup the game environment and load assets.
        """
        pygame.init()
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption("Flap Flap")
        self.clock = pygame.time.Clock()

        self.config = ANIMALS[animal_key]
        self.animal_key = animal_key

        # Managers
        self.sound_manager = SoundManager()
        self.game_state = GameState()
        self.score_manager = ScoreManager(self.game_state, self.sound_manager)

        # Assets
        self.background = pygame.image.load(self.config["background"])

        # Entities
        self.player = Player(self.config["player"], self.config)
        self.pipe_manager = PipeManager(self.config["obstacle"])

        # Timed pipe spawn event
        self.CREATE_PIPE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.CREATE_PIPE_EVENT, 1500)

        self.font = pygame.font.SysFont("Comic Sans MS", 45)

    def handle_events(self):
        """
        Process user input and game events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == self.CREATE_PIPE_EVENT and not self.game_state.game_over:
                self.pipe_manager.create_pipes()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    if not self.game_state.game_over:
                        self.player.jump()
                        self.sound_manager.play("flap")
                    else:
                        return "RESTART"

        return "CONTINUE"

    def check_game_over(self):
        """
        Check whether the player has lost the game.
        """
        if not self.player.alive or self.pipe_manager.check_collision(self.player):
            if not self.game_state.game_over:
                self.sound_manager.play("gameover")
                self.game_state.game_over = True
                check_and_update_highscore(self.game_state.score)

    def update(self):
        """
        Update all gameplay systems.
        """
        self.player.update()
        self.pipe_manager.update()
        self.score_manager.update(self.player, self.pipe_manager.pipes)
        self.check_game_over()

    def draw(self):
        """
        Draw the current frame.
        """
        self.window.blit(self.background, (0, 0))
        self.player.draw(self.window)

        for pipe in self.pipe_manager.pipes:
            pipe.draw(self.window)

        score_text = self.font.render(
            str(int(self.game_state.score)), True, (255, 255, 255)
        )
        self.window.blit(score_text, (5, 0))

    def reset(self):
        """
        Reset game entities after restart.
        """
        self.game_state.reset()
        self.player = Player(self.config["player"], self.config)
        self.pipe_manager.pipes.clear()

    def run(self):
        """
        Main game loop.
        """
        while True:
            action = self.handle_events()

            if action == "QUIT":
                pygame.quit()
                exit()

            elif action == "RESTART":
                self.reset()
                continue

            if not self.game_state.game_over:
                self.update()

            self.draw()

            if self.game_state.game_over:
                action, _ = run_game_over(
                    self.game_state.score, last_animal=self.animal_key
                )
                if action == "TRY_AGAIN":
                    return run_flappy(self.animal_key)
                elif action == "BACK_TO_MENU":
                    return

            pygame.display.update()
            self.clock.tick(60)


def run_flappy(animal_key):
    """
    Entry point for starting the game.
    """
    game = FlappyBirdGame(animal_key)
    game.run()
