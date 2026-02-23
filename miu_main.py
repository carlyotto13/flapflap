# main.py
from miu_selection_screen_updated import run_selection
from miu_animals.miu_frog import run_frog
from miu_gameover_screen import run_game_over
from miu_highscore import highscore, update_highscore

if __name__ == "__main__":
    last_animal = None
    while True:
        #Startscreen oder zurück zum Menü
        if not last_animal:
            choice = run_selection()  # z.B. "FROG"
            last_animal = choice
        else:
            choice = last_animal

        #Tier-Spiel starten
        if choice == "FROG":
            score = run_frog()

        #Game Over Screen
        action, last_animal = run_game_over(score, last_animal)

        #Entscheidung auswerten
        if action == "BACK_TO_MENU":
            last_animal = None  # Auswahl wieder möglich

