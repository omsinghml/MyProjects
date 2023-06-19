from tkinter import *
import random

window = Tk()
window.title("Hangman Game")
window.configure(background='black')

words = ['python', 'jupyter', 'java', 'machine', 'language', 'computer', 'harddrive', 'laptop',
	'mobile', 'college', 'demon', 'hunters', 'finance', 'management', 'human', 'resources', 'accounting',
	'principal', 'physics', 'chemistry', 'information', 'data', 'science', 'handbook', 'learning', 'deep', 'cyber',
	'security', 'statistics', 'linear', 'regression', 'visualization']

vow = 'aeiou'
Empty = []
guesses = 10


blankline = Label(window, text='', bg='black').grid(row=1)

Header = Label(window, text='Hangman Game', fg='black', bg='grey', font='Helvetica 16 bold').grid(row=2, columnspan=13)

word = random.choice(words)
print(word)

length1 = len(word)
Display = "_"*length1
dashes = Label(window, text=Display, fg='black').grid(row=3, columnspan=13)


def get_hint():
	global Display
	for a, char in enumerate(word):
		if char in vow:
			Empty.extend([char])
			Display = Display[:a] + char + Display[1+a:]
			dashes = Label(window, text=Display, fg='black').grid(row=3, columnspan=13)


def get_variable(var):
	global guesses
	global Display
	global word

	if var not in Empty and var in vow:
		i = word.find(var)
		word = word[:i] + "_" + word[i + 1:]
		Display = Display[:i] + var + Display[i+1:]
		dashes = Label(window, text=Display, fg='black').grid(row=3, columnspan=13)


	elif var in Empty:
		guesses-=1
		Lable2 = Label(window, text=f"Choose the consonants. You have now {guesses}, guesses").grid(row=9, columnspan=13)

	elif var in word:
		i = word.find(var)
		word = word[:i] + "_" + word[i + 1:]
		Display = Display[:i] + var + Display[i+1:]
		dashes = Label(window, text=Display, fg='black').grid(row=3, columnspan=13)

	else:
		guesses -= 1
		Label3 = Label(window, text=f"Sorry, wrong letter. You have now {guesses}, guesses").grid(row=9, columnspan=13)

		if guesses<=0:
			Display = "You Lost"
			dashes = Label(window, text=Display, fg='black').grid(row=3, columnspan=13)



def submit():
	global Display
	if '_' not in Display:
		Display = "You won!"
		dashes = Label(window, text=Display).grid(row=3, columnspan=13)

	elif guesses == 0:
		Display = "You Lost!"
		dashes = Label(window, text=Display).grid(row=3, columnspan=13)



#------------------------------------------------ UI Design --------------------------------------------------------------------------

#display = Entry(window)
#display.grid(columnspan=length1, sticky=N+E+W+S)

Button(window, text="Hint", fg='black', bg='grey', font='Helvetica 10 bold', command= lambda: get_hint()).grid(row=4, columnspan=13, sticky=N+S+E+W)

Button(window, text="A", command= lambda: get_variable('a')).grid(row=6, column=0, sticky=N+S+E+W)
Button(window, text="B", command= lambda: get_variable('b')).grid(row=6, column=1, sticky=N+S+E+W)
Button(window, text="C", command= lambda: get_variable('c')).grid(row=6, column=2, sticky=N+S+E+W)
Button(window, text="D", command= lambda: get_variable('d')).grid(row=6, column=3, sticky=N+S+E+W)
Button(window, text="E", command= lambda: get_variable('e')).grid(row=6, column=4, sticky=N+S+E+W)
Button(window, text="F", command= lambda: get_variable('f')).grid(row=6, column=5, sticky=N+S+E+W)
Button(window, text="G", command= lambda: get_variable('g')).grid(row=6, column=6, sticky=N+S+E+W)
Button(window, text="H", command= lambda: get_variable('h')).grid(row=6, column=7, sticky=N+S+E+W)
Button(window, text="I", command= lambda: get_variable('i')).grid(row=6, column=8, sticky=N+S+E+W)
Button(window, text="J", command= lambda: get_variable('j')).grid(row=6, column=9, sticky=N+S+E+W)
Button(window, text="K", command= lambda: get_variable('k')).grid(row=6, column=10, sticky=N+S+E+W)
Button(window, text="L", command= lambda: get_variable('l')).grid(row=6, column=11, sticky=N+S+E+W)
Button(window, text="M", command= lambda: get_variable('m')).grid(row=6, column=12, sticky=N+S+E+W)

Button(window, text="N", command= lambda: get_variable('n')).grid(row=7, column=0, sticky=N+S+E+W)
Button(window, text="O", command= lambda: get_variable('o')).grid(row=7, column=1, sticky=N+S+E+W)
Button(window, text="P", command= lambda: get_variable('p')).grid(row=7, column=2, sticky=N+S+E+W)
Button(window, text="Q", command= lambda: get_variable('q')).grid(row=7, column=3, sticky=N+S+E+W)
Button(window, text="R", command= lambda: get_variable('r')).grid(row=7, column=4, sticky=N+S+E+W)
Button(window, text="S", command= lambda: get_variable('s')).grid(row=7, column=5, sticky=N+S+E+W)
Button(window, text="T", command= lambda: get_variable('t')).grid(row=7, column=6, sticky=N+S+E+W)
Button(window, text="U", command= lambda: get_variable('u')).grid(row=7, column=7, sticky=N+S+E+W)
Button(window, text="V", command= lambda: get_variable('v')).grid(row=7, column=8, sticky=N+S+E+W)
Button(window, text="W", command= lambda: get_variable('w')).grid(row=7, column=9, sticky=N+S+E+W)
Button(window, text="X", command= lambda: get_variable('x')).grid(row=7, column=10, sticky=N+S+E+W)
Button(window, text="Y", command= lambda: get_variable('y')).grid(row=7, column=11, sticky=N+S+E+W)
Button(window, text="Z", command= lambda: get_variable('z')).grid(row=7, column=12, sticky=N+S+E+W)

Button(window, text="SUBMIT", fg='black', bg='grey', font='Helvetica 10 bold', command= lambda: submit()).grid(row=8, columnspan=13)


window.mainloop()