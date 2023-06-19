import random
#library in order to choose 
#random words from a list of words

name = input(f"What is your name? ")
#here user is asked to input his name first

words = ['python', 'jupyter', 'java', 'machine', 'language', 'computer', 'harddrive', 'laptop',
	'mobile', 'college', 'demon', 'hunters', 'finance', 'management', 'human', 'resources', 'accounting',
	'principal', 'physics', 'chemistry', 'information', 'data', 'science', 'handbook', 'learning', 'deep', 'cyber',
	'security', 'statistics', 'linear', 'regression', 'visualization']
#lists of words from where words will be randomly chosen

list1 = ['a', 'e', 'i', 'o', 'u']

word = random.choice(words)

guesses = 'aeiou'

turns = 2

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
