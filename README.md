# Flap Flap Game

## Description 
A simple Flappy Bird clone written in Python using Pygame.  
Players try to navigate their chosen animal through an endless series of randomly generated obstacles.
This project is a fun way to practice game development, object-oriented programming, and handling user input and collisions.

## Table of Contents 
- Features
- Installation
- Usage
- Project structure

## Features
- Selection between different animals 
- Player-controlled animal that can fly upwards
- Randomly generated pipes as obstacles
- Score tracking for each successful pass
- Collision detection with pipes and ground
- Basic start and game-over screens
- Saving the highscore
- Implementation of sounds (background, game)
- setting screen with option to turn of sounds

## Installation
Make sure you have Python 3.12 or higher installed.

1. Clone the repository:
    ```bash
    git clone <https://github.com/carlyotto13/flapflap.git>
   ```
2. Navigate to the project folder: 
    ```bash
    cd flapflap
    ```
3. install dependencies: 
    ```bash
    pip install -r requirements.txt
    ```
4. Run the game: 
    ```bash 
    python3 main.py
   ```

## Usage

#### Controls: 
- On Starting screen:
  - click animal -> game starts with chosen animal
  - click settings -> open Settings
- On Game Over screen:
  - Space bar, Up arrow or click "Try Again" -> retry
  - clock "Back to Menu" -> back to starting screen
- In Game: 
  - spacebars or UP arrow -> make the bird flap upwards

#### Settings: 
- On Setting screen: 
  - toggle background music and game sounds 


## Project Structure

```text
flapflap/
│
├── assets/
├── src
│    └── main.py
│    └── run.py
│    └── animals.py
│    └── game_state.py
│    └── gameover_screen.py
│    └── highscore.py
│    └── highscore.txt
│    └── pipes.py
│    └── player.py
│    └── score.py
│    └── screen.py
│    └── selection.py
│    └── selection_screen.py
│    └── setting_screen.py
│    └── settings.py
│    └── sound.py
├── tests/
│
├── requirements.txt
├── LICENSE 
└── README.md 
```

## Architecture

- **main.py** handles program flow (menu → game → game over → settings)
- **run.py** contains the game loop and game mechanics
- **highscore.py** manages persistent highscore storage
- **sound.py** handles background music and sound effects
- **screen.py** provides reusable screen and block rendering logic
- **selection.py** and **gameover_screen.py** handle UI screens

This separation allows for easier maintenance, unit testing, and future feature expansion.

## Assets 
#### Images
All images were drawn with procreate by us.

#### Sounds 
All sounds were made with Garageband by us. 

## Possible features with more time

- Storyline and boss fights
- items
- animation of animals (jump up and down)
- muliplayer mode
- selecting difficulty level (speed and size of gap)