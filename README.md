# SNAKE GAME 🐍

A classic Snake game written in Python (turtle graphics) by **Shivam Joshi**.

## Play it in your browser

**[▶ Play the web version](https://shivamexe959.github.io/SNAKE_GAME)**

> **Note on the web version:** The browser edition (`docs/index.html`) is an
> AI-assisted port of the Python original, created so the game can be played
> by anyone in a browser via GitHub Pages. The game logic is a faithful port
> of the Python source — the Python files below remain the original work.

## The original (Python)

Run it locally with Python 3:

```bash
python main.py
```

### Files

| File | What it does |
|---|---|
| `main.py` | Game setup, main loop, food & collision detection, wall modes |
| `snake.py` | Snake movement, growth, and direction controls |
| `food.py` | Random food spawning |
| `scoreboard.py` | Score display and game-over message |

### How to play

- **Controls:** Arrow keys or W / A / S / D
- **Choose your mode** at the start:
  - **Classic** — hitting a wall ends the game
  - **Wraparound** — Snake II style, the snake teleports to the opposite edge
- **Eat food** to grow and score **+7 points** per food
- **Don't bite your own tail!**

---

*Web edition: AI-assisted port for browser play. Python edition: original work by Shivam Joshi.*
