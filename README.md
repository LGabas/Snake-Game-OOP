## Snake Game 🐍
This is a simple Snake Game built using Python's turtle module. The player controls a snake that moves around the screen, eating food to grow longer while avoiding collisions with the walls or its own tail. The goal is to achieve the highest possible score by eating as much food as possible before colliding.

## Features
Snake movement controlled with arrow keys.
Food appears randomly on the screen for the snake to eat.
The snake grows longer with each piece of food consumed.
Score tracking system.
Game resets upon collision with walls or snake’s own body.

## Project Structure
main.py: The main script that runs the game.

snake.py: Contains the Snake class responsible for the snake's movement and behavior.

food.py: Contains the Food class that generates and refreshes the food.

scoreboard.py: Contains the Score class that tracks and displays the player's score.

## How to Play
Use the arrow keys to control the direction of the snake:
Up Arrow: Move up
Down Arrow: Move down
Left Arrow: Move left
Right Arrow: Move right
The snake will move continuously, and your objective is to eat the food that appears on the screen.
Each time the snake eats food, it grows longer, and the score increases.
The game will reset if:
The snake hits the wall.
The snake collides with its own body.
