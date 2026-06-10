# 🪨📄✂️ Rock Paper Scissors

A classic Rock Paper Scissors game built with Python — available in two versions: a **GUI version** using Tkinter and a **terminal version** for the command line.

---

## Features

- **Two game modes** — play via a graphical interface or directly in your terminal
- **Real-time scoreboard** — tracks your score vs. the computer across rounds
- **Random computer opponent** — the computer picks its move using Python's `random` module
- **Replay support** — keep playing as many rounds as you like

---

## Files

| File | Description |
|------|-------------|
| `snl.py` | GUI version built with Tkinter |
| `rps.py` | Terminal/command-line version |

---

## Requirements

- Python 3.x
- `tkinter` (included with most standard Python installations)

---

## How to Run

### GUI Version (Tkinter)

```bash
python snl.py
```

A window will open with three buttons — Rock, Paper, and Scissors. Click your choice and the result appears instantly along with the live score.

### Terminal Version

```bash
python rps.py
```

You'll be prompted to type your choice (`rock`, `paper`, or `scissors`). After each round, the scorecard is shown. Press `C` to continue or `E` to exit and see the final result.

---

## How to Play

1. Choose **Rock**, **Paper**, or **Scissors**
2. The computer randomly selects its move
3. The winner is decided by the classic rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
4. Scores are tracked across all rounds until you exit

---

## Project Structure

```
Rock_Paper_Scissors/
├── rps.py        # Terminal version
├── snl.py        # GUI version (Tkinter)
└── README.md
```

---

## Author

**Avantika Bijalwan** — [@avantikabijalwan19-ux](https://github.com/avantikabijalwan19-ux)
