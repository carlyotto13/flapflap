"""TODO"""

from pathlib import Path

# TODO: Path is a bit easier to use and has more options
HIGH_SCORE_FILE = Path(__file__).parent / "highscore.txt"


# TODO: avoid using globals - it can get messy super fast!
# TODO could also be a hint as pipes clear are whole numbers
# TODO: write docstrings
def load_highscore() -> float:
    """Load highscore from file."""
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            highscore = float((f.read().strip()))
    except FileNotFoundError:
        highscore = 0.0
    except ValueError:
        highscore = 0.0

    return highscore


def save_highscore(highscore: float) -> None:
    """
    Saves highscore to file.

    :param highscore: Highscore to save.
    """
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
