# miu_stats.py
highscore = 0  # globaler Highscore

def update_highscore(score):
    global highscore
    if score > highscore:
        highscore = score