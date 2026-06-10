import random
items = ["rock","paper","scissors"]
user_scr=0
comp_scr=0
while True:
    print("Welcome to the game of ROCK PAPER AND SCISSORS")
    user = input("Choose your weapon : ").lower()
    computer=random.choice(items)

    if user == computer:
        print("Tie")
    elif user == "rock" and computer == "scissors":
        print("You won, computer chose scissors")
        user_scr+=1 
    elif user == "paper" and computer == "rock":
        print("You won, computer chose rock")
        user_scr+=1 
    elif user == "scissors" and computer == "paper":
        print("You won, computer chose paper")
        user_scr+=1 
    else :
        print ("computer won , computer chose",computer)
        comp_scr+=1
    
    print("SCORECARD :\n")
    print("User\n",user_scr)
    print("computer\n",comp_scr)

    
    choice=input("PRESS C TO CONTINUE AND E TO EXIT:").lower()
    if choice == "e": 
        break
    
print("Overall result:\n")
if user_scr > comp_scr:
    print("You won")
else:
    print("Computer won")