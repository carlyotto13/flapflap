import sys
from pathlib import Path

# import from src
#sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import pytest
from unittest.mock import patch, MagicMock
import gameover_screen
import pygame
from unittest.mock import patch, MagicMock


@patch("pygame.time.set_timer")
@patch("pygame.image.load", return_value=pygame.Surface((10, 10)))
@patch("pygame.display.set_mode")
@patch("pygame.font.SysFont")
@patch("pygame.event.get")
def test_run_game_over_try_again(
    mock_events, mock_font, mock_display, mock_load, mock_timer
):
    window = MagicMock()
    mock_display.return_value = window

    # simulate KEYDOWN Space
    event = MagicMock()
    event.type = pygame.KEYDOWN
    event.key = pygame.K_SPACE
    mock_events.return_value = [event]

    #import gameover_screen

    result = gameover_screen.run_game_over(10, "FROG")
    assert result == ("TRY_AGAIN", "FROG")


@patch("pygame.time.set_timer")
@patch("pygame.image.load", return_value=pygame.Surface((10, 10)))
@patch("pygame.display.set_mode")
@patch("pygame.font.SysFont")
@patch("pygame.event.get")
def test_run_game_over_back_to_menu(
    mock_events, mock_font, mock_display, mock_load, mock_timer
):
    window = MagicMock()
    mock_display.return_value = window

    rect_mock = MagicMock()
    rect_mock.collidepoint.return_value = True
    screen_mock = MagicMock()
    screen_mock.blocks = [(rect_mock, ["BACK TO MENU"], 1.0)]

    #import gameover_screen

    with patch("gameover_screen.Screen", return_value=screen_mock):
        event = MagicMock()
        event.type = pygame.MOUSEBUTTONDOWN
        mock_events.return_value = [event]
        result = gameover_screen.run_game_over(10, "FROG")
        assert result == ("BACK_TO_MENU", None)
