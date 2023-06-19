import random
import time

ask_name = input ("What is your name? ")
time.sleep(1)
print(f"\nWelcome to Rolling Dice Simulator {ask_name.title()}.\n")

def main():
	global play_game
	global number
	number = random.randint(1, 6)
	play_game = ''
	
def intro_game():
	global play_game

	play_game = input(" Do you want to play the game? ")

	while play_game not in ['y', 'n', 'Y', 'N']:
		play_game = input("Do you want to play the game? y = yes and n = no.\n")

	if play_game == 'y' or play_game == 'Y':
		main()

	elif play_game == 'n' or play_game == 'N':
		print(f"Thankyou for playing the game, {ask_name}")
		exit()

def dice_simulator():
	global number

	while True:
	
		if number == 1:
			print("-------")
			print("       ")
			print("   0   ")
			print("       ")
			print("-------")

		elif number == 2:
			print("-------")
			print(" 0     ")
			print("       ")
			print("     0 ")
			print("-------")

		elif number == 3:
			print("-------")
			print(" 0     ")
			print("   0   ")
			print("     0 ")
			print("-------")

		elif number == 4:
			print("-------")
			print(" 0   0 ")
			print("       ")
			print(" 0   0 ")
			print("-------")

		elif number == 5:
			print("-------")
			print(" 0   0 ")
			print("   0   ")
			print(" 0   0 ")
			print("-------")

		elif number == 6:
			print("-------")
			print(" 0   0 ")
			print(" 0   0 ")
			print(" 0   0 ")
			print("-------")

		intro_game()
		

main()

dice_simulator()





