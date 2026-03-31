"""Checks and assigns scores."""


class ScoreManager:
    """
    Handles scores based on pipe passing.
    """

    def __init__(self, game_state, sound_manager):
        """
        Current game state
        sound_manager used for point sound
        """
        self.game_state = game_state
        self.sound_manager = sound_manager

    def update(self, player, pipes):
        """
        Check if player passed pipes and if yes gives points.
        """
        for pipe in pipes:
            if not pipe.passed and player.rect.x > pipe.x + pipe.width:
                self.game_state.increment_score(0.5)
                pipe.passed = True
                self.sound_manager.play("point")
