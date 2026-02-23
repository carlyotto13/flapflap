# Flap Flap Game

## Description 
A simple Flappy Bird clone written in Python using Pygame.  
This project is a fun way to practice game development, object-oriented programming, and handling user input and collisions.
The difference to the original game is that you can choose between characters. 

## Table of Contents 
- [Features]
- [Installation] 
- [Usage]
- [Project structure]

## Features
- Selection between different animals 
- Player-controlled animal that can fly upwards
- Randomly generated pipes as obstacles
- Score tracking for each successful pass
- Collision detection with pipes and ground
- Basic start and game-over screens

## Installation
Make sure you have Python 3.12 or higher installed.

1. Clone the repository:
    ```bash
    git clone <https://github.com/carlyotto13/flapflap.git>
2. Navigate to the project folder: 
   cd ... 
3. install dependencies: 
   python3 -m pip install pygame 

## Usage 
run the main game script: 
python3 main.py 

controls: 
*Spacebar* -> make the bird flap upwards


## Project Structure

```text
flapflap/
│
├── main.py
├── player.py 
├── obstacles.py 
├── menu.py 
├── assets/
├── tests/
│   └── test_main.py
│
├── requirements.txt
├── LICENSE 
└── README.md 
```

## TODO

- drawing 
  - animals 
  - background 
  - pipes 
- coding 
- changing Project structure in the READme  
- sounds 
- settings 
- highscore 
- animation ? 
- simplify code 
- docstrings !!! 
- change it so that SPACE is also a sign for retry 