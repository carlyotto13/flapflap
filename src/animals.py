"""TODO modules docstrings like this."""

from pathlib import Path

# TODO: use Path object for Paths - OS independent and easy to handle
# TODO: use constants where you can
ASSETS_PATH = Path(__file__).parents[1] / "assets"
ANIMALS = {
    "FROG": {
        "background": ASSETS_PATH / "frog" / "frog_background.png",
        "player": ASSETS_PATH / "frog" / "frog_01.png",
        "obstacle": ASSETS_PATH / "frog" / "frog_obstacle.png",
    },
    "PENGUIN": {
        "background": "../assets/penguin/penguin_background.png",
        "player": "../assets/penguin/penguin_01.png",
        "obstacle": "../assets/penguin/penguin_obstacle.png",
    },
    "DOG": {
        "background": "../assets/dog/dog_background.png",
        "player": "../assets/dog/dog_01.png",
        "obstacle": "../assets/dog/dog_obstacle.png",
    },
    "HAMSTER": {
        "background": "../assets/hamster/hamster_background.png",
        "player": "../assets/hamster/hamster_01.png",
        "obstacle": "../assets/hamster/hamster_obstacle.png",
    },
}
