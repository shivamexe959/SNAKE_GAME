# Snake Game — Project Explanation

## Overview
This is a classic Snake game built in Python using the built-in `turtle` graphics library. The player controls a snake that moves around a 600x600 black screen, eats food to grow longer and increase the score, and the game ends if the snake hits the wall or collides with its own tail.

The project is split into four files, each handling one responsibility:

```
snake_game/
├── main.py         # Game loop, controls, collision detection
├── snake.py         # Snake class: movement, growth, direction
├── food.py           # Food class: random spawning
└── scoreboard.py      # Scoreboard class: score display, game over text
```

## How It Works — File by File

### 1. `main.py` — The Game Loop
This is the entry point that ties everything together.

- Sets up the screen (600x600, black background, title "SNAKE GAME").
- `screen.tracer(0)` turns off automatic screen updates so I can manually control animation with `screen.update()` — this makes the movement smooth instead of flickery.
- Creates one `Snake`, one `Food`, and one `Scoreboard` object.
- `screen.listen()` + `screen.onkey(...)` binds the arrow keys to the snake's direction methods (`up`, `down`, `left`, `right`).
- **Main `while` loop** runs every 0.1 seconds and does four things each frame:
  1. `snake.move()` — moves the snake forward.
  2. **Food collision** — if the snake's head is within 15 pixels of the food, it counts as "eaten": the food respawns, the score goes up, and the snake grows by one segment.
  3. **Wall collision** — if the head goes past ±280 on the x or y axis, the game ends.
  4. **Tail collision** — loops through every body segment (except the head) and checks if the head is within 10 pixels of it; if so, the game ends.
- When the game ends, `scoreboard.game_over()` displays "GAME OVER" and the loop stops.

### 2. `snake.py` — The Snake Class
Handles everything about the snake itself.

- `STARTING_POSITIONS` places 3 starting segments 20px apart in a row.
- `create_snake()` builds the initial snake by calling `add_segment()` for each starting position.
- `add_segment(pos)` creates a white square `Turtle`, disables its pen, and places it at `pos`.
- `extend()` adds a new segment on top of the current last segment whenever food is eaten — it "grows" from the tail.
- **`move()` is the core trick of the whole game**: 
  - First, it saves the current position of every segment.
  - Then it moves the head forward by `MOVE_DISTANCE` (20px).
  - Then, starting from the *second* segment, each segment moves to where the segment in front of it used to be.
  - This creates the classic "follow the leader" snake movement without needing a complicated data structure.
- `up()`, `down()`, `left()`, `right()` change the head's heading, but each one checks that the snake isn't currently moving in the exact opposite direction — this stops the snake from being able to instantly reverse into itself.

### 3. `food.py` — The Food Class
A small class that extends `Turtle` directly.

- Draws a small red circle (`shapesize` shrinks it to half size).
- `speed(0)` makes it move instantly with no animation.
- `refresh()` picks a random `(x, y)` position within the play area (±280, matching the wall boundary in `main.py`) and teleports the food there. This is called both on creation and every time the snake eats it.

### 4. `scoreboard.py` — The Scoreboard Class
Also extends `Turtle`, but used purely for writing text (never actually "seen" as a shape).

- Positions itself at the top-center of the screen `(0, 270)` and writes the starting score.
- `hideturtle()` is called after writing so only the text shows, not a turtle icon/arrow.
- `increase_score()` clears the old text and rewrites the score with the updated number every time food is eaten.
- `game_over()` moves to the center of the screen and writes "GAME OVER" when the game ends.

## Key Concepts Used
- **Object-Oriented Programming**: each game element (snake, food, scoreboard) is its own class with its own responsibilities, instead of one giant script.
- **Turtle graphics**: using `Turtle` objects as visual game pieces and controlling them with `.goto()`, `.forward()`, `.setheading()`.
- **Manual screen refresh (`tracer(0)` + `screen.update()`)**: a common trick to get smooth, non-flickering animation in turtle instead of relying on its default (slow) auto-refresh.
- **Collision detection via distance**: instead of complex hitbox logic, collisions are detected simply by checking if the distance between two turtles is below a threshold.
- **State tracking without extra data structures**: the snake's body follow-the-leader movement is achieved just by remembering each segment's *previous* position for one frame.

## Status
The game is fully functional: the snake moves, eats food, grows, tracks score, and correctly ends the game on wall or self-collision.

## Possible Future Improvements
- Add a persistent high-score file so the best score is remembered between runs.
- Add sound effects for eating food and game over.
- Add a "press any key to restart" option instead of closing on click.
- Extract magic numbers (`15`, `280`, `10`) into named constants for readability.
