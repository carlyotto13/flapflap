# highscore.py

import os

highscore = 0.0  # globaler Highscore
HIGH_SCORE_FILE = os.path.join(os.path.dirname(__file__), "highscore.txt")

def load_highscore():
    global highscore
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            highscore = float((f.read().strip()))
    except FileNotFoundError:
        highscore = 0.0
    except ValueError:
        highscore = 0.0

def save_highscore():
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(highscore))

def update_highscore(score):
    global highscore
    if score > highscore:
        highscore = score
        save_highscore()