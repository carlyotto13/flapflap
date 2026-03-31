import sys
from pathlib import Path

# import from src
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import pytest
import builtins
from unittest.mock import mock_open, patch
import highscore


def test_load_highscore_file_exists():
    m = mock_open(read_data="42.5")
    with patch("builtins.open", m):
        highscore.load_highscore()
    assert highscore.highscore == 42.5


def test_load_highscore_file_not_exists():
    with patch("builtins.open", side_effect=FileNotFoundError):
        highscore.load_highscore()
    assert highscore.highscore == 0.0


def test_load_highscore_invalid_value():
    m = mock_open(read_data="abc")
    with patch("builtins.open", m):
        highscore.load_highscore()
    assert highscore.highscore == 0.0


def test_save_highscore_writes_file():
    m = mock_open()
    highscore.highscore = 99.9
    with patch("builtins.open", m):
        highscore.save_highscore()
    m.assert_called_once()
    handle = m()
    handle.write.assert_called_once_with("99.9")


def test_update_highscore_updates_global_and_saves():
    m = mock_open()
    highscore.highscore = 10
    with patch("builtins.open", m):
        highscore.update_highscore(20)
    assert highscore.highscore == 20
    handle = m()
    handle.write.assert_called_once_with("20")


def test_update_highscore_not_changed_if_lower():
    highscore.highscore = 50
    highscore.update_highscore(20)
    assert highscore.highscore == 50
