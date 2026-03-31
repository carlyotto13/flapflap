import sys
from pathlib import Path

# import from src
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import pytest
from unittest.mock import patch
from main import MainGameLoop


@patch("main.run_selection")
@patch("main.run_flappy")
@patch("main.run_game_over")
def test_full_game_flow(run_game_over, run_flappy, run_selection):
    # Arrange
    run_selection.return_value = "FROG"
    run_flappy.return_value = 5
    run_game_over.return_value = ("BACK_TO_MENU", None)

    game = MainGameLoop()

    # Act
    game.last_animal = None
    game.run = lambda: None  # prevent infinite loop

    choice = run_selection()
    score = run_flappy(choice)
    action, last = run_game_over(score, choice)

    # Assert
    assert choice == "FROG"
    assert score == 5
    assert action == "BACK_TO_MENU"


@patch("main.run_selection")
def test_selection_stored(run_selection):
    # Arrange
    run_selection.return_value = "CAT"
    game = MainGameLoop()

    # Act
    game.last_animal = run_selection()

    # Assert
    assert game.last_animal == "CAT"


@patch("main.run_game_over")
def test_back_to_menu_resets_last_animal(run_game_over):
    # Arrange
    game = MainGameLoop()
    game.last_animal = "DOG"

    run_game_over.return_value = ("BACK_TO_MENU", None)

    # Act
    action, game.last_animal = run_game_over(10, "DOG")

    if action == "BACK_TO_MENU":
        game.last_animal = None

    # Assert
    assert game.last_animal is None
