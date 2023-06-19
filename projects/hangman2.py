import random

def show_name():

	name = input("What is your name? ")
	print(f"\nWelcome to the game, {name}")

	print(f"You have to guess the word, one letter at a time. Good luck!.\n")


def describe_game():

	guesses = 'aeiou'
	turns = 2
	words = ['python', 'jupyter', 'java', 'machine', 'language', 'computer', 'harddrive', 'laptop',
	'mobile', 'college', 'demon', 'hunters', 'finance', 'management', 'human', 'resources', 'accounting',
	'principal', 'physics', 'chemistry', 'information', 'data', 'science', 'handbook', 'learning', 'deep', 'cyber',
	'security', 'statistics', 'linear', 'regression', 'visualization']
	list1 = ['a', 'e', 'i', 'o', 'u']

	word = random.choice(words)


	while turns > 0:

		failed = 0

		for alpha in word:

			if alpha in guesses:

				print(alpha)

			else:
				print('_')

				failed += 1


		if failed == 0:
			print("You win.")
			print("The correct word is", word)
			break

		guess = input("Guess a letter: ")

		if guess in list1:
			print("Guess the consonants")
			continue

		elif guess == 'q':
			print("Thankyou for playing.")
			break

		else:	
			guesses += guess

		if guess not in word:
			turns -= 1

			print(f"You have", turns, "no of guesses")

		if turns == 0:
			print("You dont have more guesses. You loose")
			print("The correct word is", word)
			break

show_name()
describe_game()