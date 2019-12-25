"""
* Best of n
"""

from random import *
victory = 0
tie = 0

for y in range (1, 6):
        choice = input("Rock, Paper, Scissors: ")
        x = randint(1, 3)

        if choice == "Rock" or choice == "Paper" or choice == "Scissors":
                if x == 1:
                        if choice == "Rock":
                                print("AI chooses scissors, you win!")
                                victory += 1
                        elif choice == "Paper":
                                print("AI chooses rock, you win!")
                                victory += 1
                        elif choice == "Scissors":
                                print("AI chooses paper, you win!")
                                victory += 1
                elif x == 2:
                        if choice == "Rock":
                                print("AI chooses paper, you lose!")
                        elif choice == "Paper":
                                print("AI chooses scissors, you lose!")
                        elif choice == "Scissors":
                                print("AI chooses rock, you lose!")
                elif x == 3:
                        print("It's a draw.")
                        tie += 1
        else:
                print("Invalid Input")

print("You won" , victory , "out of 5 times!")
print("You drew" , tie , "out of 5 times!")
