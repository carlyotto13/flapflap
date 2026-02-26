import sys
from pathlib import Path

# von src importieren
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import pytest
from unittest.mock import patch
from run import GameState, Player, PipeManager
from settings import GAME_HEIGHT, PIPE_SPEED
import pygame


# ---------- PLAYER TESTS ----------

@patch("pygame.image.load")
@patch("pygame.transform.scale")
def test_player_falls_due_to_gravity(mock_scale, mock_load):
    # Arrange
    mock_load.return_value = pygame.Surface((10, 10))
    mock_scale.side_effect = lambda img, size: img
    player = Player("dummy.png", {})
    player.velocity_y = 1  # Gravity sichtbar
    start_y = player.rect.y

    # Act
    player.update()

    # Assert
    assert player.rect.y > start_y


@patch("pygame.image.load")
@patch("pygame.transform.scale")
def test_player_dies_when_falling_below_screen(mock_scale, mock_load):
    # Arrange
    mock_load.return_value = pygame.Surface((10, 10))
    mock_scale.side_effect = lambda img, size: img
    player = Player("dummy.png", {})
    player.rect.y = GAME_HEIGHT + 10

    # Act
    player.update()

    # Assert
    assert player.alive is False


# ---------- GAME STATE TESTS ----------

def test_game_state_reset():
    state = GameState()
    state.score = 10
    state.game_over = True

    state.reset()

    assert state.score == 0
    assert state.game_over is False


def test_score_increment():
    state = GameState()

    state.increment_score(0.5)

    assert state.score == 0.5


# ---------- PIPE MANAGER TESTS ----------

@patch("pygame.image.load")
@patch("pygame.transform.scale")
@patch("pygame.transform.rotate")
def test_pipe_cleanup(mock_rotate, mock_scale, mock_load):
    # Arrange
    mock_load.return_value = pygame.Surface((10, 10))
    mock_scale.side_effect = lambda img, size: img
    mock_rotate.side_effect = lambda img, angle: img  # Korrekt 2 Argumente

    manager = PipeManager("dummy.png")

    # Fake pipe außerhalb des Bildschirms
    class DummyPipe:
        def __init__(self):
            self.x = -1000  # update() benutzt pipe.x
            self.img = None
            self.passed = False
            self.type = "top"

    manager.pipes.append(DummyPipe())

    # Act
    manager.update()

    # Assert
    assert len(manager.pipes) == 0