import sys
from pathlib import Path

# import from src
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import pytest
from unittest.mock import MagicMock, patch
from screen import Screen


# Test: add_blocks und create_cloud
@patch("pygame.transform.scale", side_effect=lambda img, size: img)
@patch("pygame.image.load")
def test_add_blocks_and_clouds(mock_load, mock_scale):
    mock_load.return_value = MagicMock()  # Mock-Surface
    window = MagicMock()
    screen = Screen(window, "bg.png")  # no real image

    # Test add_blocks
    labels = ["A", "B", "C"]
    screen.add_blocks(labels, start_y=50, spacing=20)
    assert len(screen.blocks) == 3
    for rect, lines, scale in screen.blocks:
        assert hasattr(rect, "x")
        assert isinstance(lines, list) or isinstance(lines, str)

    # Test create_cloud
    screen.create_cloud()
    assert len(screen.clouds) == 1
    cloud_rect, cloud_img = screen.clouds[0]
    assert hasattr(cloud_rect, "x") and hasattr(cloud_rect, "y")


@patch("pygame.transform.scale", side_effect=lambda img, size: img)
@patch("pygame.image.load")
def test_move_clouds_removes_offscreen(mock_load, mock_scale):
    mock_load.return_value = MagicMock()
    window = MagicMock()
    screen = Screen(window, "bg.png")

    # Cloud out of screen
    cloud_rect = MagicMock()
    cloud_rect.x = -300
    cloud_rect.width = 50
    screen.clouds.append((cloud_rect, MagicMock()))

    screen.move_clouds(speed=-2)
    assert len(screen.clouds) == 0  # remove cloud


@patch("pygame.transform.scale", side_effect=lambda img, size: img)
@patch("pygame.image.load")
@patch("pygame.font.SysFont")
def test_draw_calls_blit(mock_font, mock_load, mock_scale):
    mock_load.return_value = MagicMock()
    window = MagicMock()
    screen = Screen(window, "bg.png")

    # Add cloud and block
    cloud_mock = MagicMock()
    screen.clouds = [(cloud_mock, MagicMock())]
    block_rect = MagicMock()
    screen.blocks = [(block_rect, ["TEST"], 1.0)]

    # Font-Mocks
    font_instance = MagicMock()
    mock_font.return_value = font_instance
    font_instance.get_height.return_value = 10
    font_instance.render.return_value = MagicMock()

    # Act
    screen.draw()

    # Assert
    assert window.blit.called  # called upon at least once
