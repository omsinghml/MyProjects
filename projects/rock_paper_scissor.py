import random

#preparig list for computer to select from
game = ['rock', 'paper', 'scissor']

#computer chooses randomly from the list above
comp = random.choice(game)

#user inputs their choice
user = input("Rock, Paper or Scissor? ")

def user_choice():
	play = input("Do you want to continue? press y or n for yes and no respectively. ")

	if play == y:
		choices = 0
		play_game()
	elif play == n:
		print("Thankyou for playing!")
		exit()

#conditions to the game
#if user inputs scissor to computer's rock, then comp wins
def play_game():
	while choices == 0:	
		if user == comp:
			print("Tie!")
			print("Comp: " + comp + "and User:", user)