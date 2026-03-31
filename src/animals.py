"""assigns background, player and pipe pictures to selected animal."""

from pathlib import Path

ASSETS_PATH = Path(__file__).parents[1] / "assets"

ANIMALS = {
    "FROG": {
        "background": ASSETS_PATH / "frog" / "frog_background.png",
        "player": ASSETS_PATH / "frog" / "frog_01.png",
        "obstacle": ASSETS_PATH / "frog" / "frog_obstacle.png",
    },
    "PENGUIN": {
        "background": ASSETS_PATH / "penguin" / "penguin_background.png",
        "player": ASSETS_PATH / "penguin" / "penguin_01.png",
        "obstacle": ASSETS_PATH / "penguin" / "penguin_obstacle.png",
    },
    "DOG": {
        "background": ASSETS_PATH / "dog" / "dog_background.png",
        "player": ASSETS_PATH / "dog" / "dog_01.png",
        "obstacle": ASSETS_PATH / "dog" / "dog_obstacle.png",
    },
    "HAMSTER": {
        "background": ASSETS_PATH / "hamster" / "hamster_background.png",
        "player": ASSETS_PATH / "hamster" / "hamster_01.png",
        "obstacle": ASSETS_PATH / "hamster" / "hamster_obstacle.png",
    },
}
