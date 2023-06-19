from numpy import*
from tkinter import*

#set up gui frame

win=Tk() #create window assigned to variable win
welc=Label(win,text="Welcome to Hangman!").grid(row=0)
inst=Message(win,text="instructions: To play start by guessing a letter in the secret word. if the letter is in the word it will fill in a blank if not you lose a life. Continue guessing untill you have guessed the secret word.").grid(row=1)
guess_text=Label(win,text="Enter a letter or Word").grid(row=2)
blank_text=Label(win,text="Secret Word").grid(row=3)
lives_text=Label(win,text="Lives Remaining").grid(row=4)
e=Entry(win)
e.grid(row=2,column=1)

#library of secret words
lib=['hanakah','christmas','holly','thanksgiving','reigndeer','family','presents','santa','kwanza', 'chocolate', 'cheesecake']
n=len(lib)

#randomly pick secret word
inx=random.randint(1,n)
secret=lib[inx]

#set up game 
lives_remaining=10
guessed_letters=''


#define function to play game
def play():
    word=secret
    while True:
        guess=get_guess(word)
        print(guess)
        print(type(guess))
        if process_guess(guess,word):
            Label(win,text="You Win!").grid(row=6)
            break
        if lives_remaining==0:
            Label(win,text="You Lose!").grid(row=6)
            Label(win,text="The secret word was: "+word).grid(row=7)
            break
Button(win,text=("Play"),command=play).grid(row=5,column=0)

def get_guess(word):
    blanks(word)
    guess=e.get()
    return guess

#diplay guessed letter in postion of word
def blanks(word):
    Label(win,text=lives_remaining).grid(row=4,column=1)
    display_word=''
    for letter in word:
        if guessed_letters.find(letter)> -1:
                  #LETTER found
            display_word=display_word+letter
        else:
            #letter not found
            display_word=display_word+'-'
    Label(win,text=display_word).grid(row=3,column=1)

def process_guess(guess,word):
    if len(guess)>1 and len(guess)==len(word):
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)

def whole_word_guess(guess, word):

    if guess.lower() == word.lower():
        return True
    else:
        lives_remaining=lives_remaining+(-1)
        return False                  


def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        # letter guess was incorrect
        lives_remaining = lives_remaining+(-1)
        guessed_letters = guessed_letters + guess.lower()
    if all_letters_guessed(word):
        return True
    return False

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter.lower()) == -1:
            return False
    return True
mainloop()