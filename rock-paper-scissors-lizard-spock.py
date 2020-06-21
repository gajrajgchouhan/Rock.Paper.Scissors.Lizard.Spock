from tkinter import *
import random
import time

# https://www.youtube.com/watch?v=x5Q6-wMx-K8
# https://the-big-bang-theory.com/rock-paper-scissors-lizard-spock/
# https://the-big-bang-theory.com/images/uploads/7/th_91035b831e518b169ab.png

"""
Rock Paper Scissors Lizard Spock was created by Internet Pioneer
Sam Kass. All hail Sam Kass!
It's very simple, Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors,
scissors decapitates lizard, lizard eats paper, paper disproves Spock,
Spock vaporizes rock, and as it always has, rock crushes scissors.
"""

GAME = ["rock", "paper", "scissor", "lizard", "spock"]
WEIGTAGE = {"rock" : 1, "paper" : 2, "scissor" : 3, "lizard" : 4, "spock" : 5}

root = Tk()
root.title("Rock Paper Scissors Lizard Spock")

def winner(computers_move, your_move):
	if computers_move == your_move:
		return 'TIE'
	if ((WEIGTAGE[computers_move] - WEIGTAGE[your_move])%5) < 3:
		return 1
	else:
		return 0

def RockPaperScissor(your_move):
	computers_move = random.choice(GAME)
	result = winner(computers_move, your_move)
	if  result == 'TIE':
		computers_score = your_score = 0
	else:
		computers_score = result
		your_score = 1 - result

	final = f"Your move: {your_move}\nComputer's move : {computers_move}\n" \
	f"Your score: {your_score}\nComputer's Score: {computers_score}"
	txt = Text(root, bg="#FFFF99", height=4, width=25)
	txt.pack()
	txt.insert(END, final)

RockButton = Button(root, text="rock", width=20, bg="Light Blue", command=lambda: RockPaperScissor("rock"))
PaperButton = Button(root, text="paper", width=20, bg="Pink", command=lambda: RockPaperScissor("paper"))
ScissorButton = Button(root, text="scissor", width=20, bg="Light Green", command=lambda: RockPaperScissor("scissor"))
LizardButton = Button(root, text="lizard", width=20, bg="Red", command=lambda: RockPaperScissor("lizard"))
SpockButton = Button(root, text="spock", width=20, bg="Light Grey", command=lambda: RockPaperScissor("spock"))
RockButton.pack()
PaperButton.pack()
ScissorButton.pack()
LizardButton.pack()
SpockButton.pack()

root.mainloop()