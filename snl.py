import tkinter as tk
import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "Tie!"

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You Win!"
        user_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(
        text=f"You: {user_choice}\nComputer: {computer_choice}\n\n{result}"
    )

    score_label.config(
        text=f"Your Score: {user_score}    Computer Score: {computer_score}"
    )

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18))
title.pack(pady=10)

tk.Button(root, text="🪨 Rock", width=15,
          command=lambda: play("rock")).pack(pady=5)

tk.Button(root, text="📄 Paper", width=15,
          command=lambda: play("paper")).pack(pady=5)

tk.Button(root, text="✂️ Scissors", width=15,
          command=lambda: play("scissors")).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Your Score: 0    Computer Score: 0")
score_label.pack()

root.mainloop()