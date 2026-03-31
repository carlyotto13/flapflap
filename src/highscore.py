"""saves highscore in txt file"""

from pathlib import Path

HIGH_SCORE_FILE = Path(__file__).parent / "highscore.txt"


def load_highscore() -> float:
    """Loads highscore from file."""
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            highscore = float((f.read().strip()))
    except FileNotFoundError:
        highscore = 0.0
    except ValueError:
        highscore = 0.0
    return highscore


def save_highscore(highscore: float) -> None:
    """Saves highscore to highscore.txt"""
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(highscore))


def check_and_update_highscore(score: float):
    """
    Update highscore with new score if highscore changed.
    :param score: New highscore.
    """
    old_highscore = load_highscore()
    if score > old_highscore:
        save_highscore(score)
