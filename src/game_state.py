"""Responsible for the state of the game."""


class GameState:
    """
    Holds the current state of the game.
    - Tracks score
    """

    def __init__(self):
        """
        Initialize default game state.
        """
        self.score = 0
        self.game_over = False
        self.paused = False

    def reset(self):
        """
        Reset the game state to starting values.
        """
        self.score = 0
        self.game_over = False
        self.paused = False

    def increment_score(self, amount=1):
        """
        Increase the score.
        """
        self.score += amount
