import random
player=int(input("Select a number between 1, 2 & 3:"))
computer=random.randint(1, 3)
Rock = 1
Paper = 2
Scissors = 3
"""
if 1<=player<=3:
    if player == computer:
        print("It's a tie!")
    elif (player == Rock and computer == Scissors) or \
        (player == Paper and computer == Rock) or \
        (player == Scissors and computer == Paper): 
        print("You win!")
    else:
        print("You lose!")
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}    
    print(f"Computer chose: {choices[computer]}")
    print(f"You chose: {choices[player]}")
    print("Thanks for playing!")
else:
    print("Invalid choice! Please select a number between 1 and 3.")

"""
if 1<=player<=3:
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}  
    print(f"Computer chose: {choices[computer]}")
    print(f"You chose: {choices[player]}")
    if player == computer:
        print("It's a tie!")
    elif player==Rock and computer==Paper:
        print("Paper covers Rock, you lose!")
    elif player==Rock and computer==Scissors:
        print("Rock crushes Scissors, you win!")
    elif player==Paper and computer==Rock:
        print("Paper covers Rock, you win!")
    elif player==Paper and computer==Scissors:
        print("Scissors cut Paper, you lose!")
    elif player==Scissors and computer==Rock:   
        print("Rock crushes Scissors, you lose!")
    elif player==Scissors and computer==Paper:
        print("Scissors cut Paper, you win!")
    else:
        print("Invalid choice! Please select a number between 1 and 3.")
  

    print("Thanks for playing!")

else:
    print("Invalid choice! Please select a number between 1 and 3.")
