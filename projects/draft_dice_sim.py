import tkinter 
from PIL import Image, ImageTk
import random
#tkinter is used to make GUI applications
#Image and ImageTk is used to perform operations regarding image on UI

#Below code is used to make a window where our dice rolling sim 
#would be executed
window = tkinter.Tk()
window.geometry('400x400')
window.title('Rolling Dice Simulator')
window.configure(background='black')

#this code puts a space between title and upper window
blankline = tkinter.Label(window, text='', bg='black')
blankline.pack()

#This code puts Title on the Interface (window)
Title = tkinter.Label(window, text='Dice Rolling Simulator',
	fg = "dark blue",
	bg = "light green",
	font = "Helvetica 16 bold italic")
Title.pack()

#Images 
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
#Simulating random number between 1 and 6 and generating Image
Image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#Construct label widget for the image
ImageLabel = tkinter.Label(window, image=Image1)
ImageLabel.image = Image1

#Packing the Image label widget in the parent window
ImageLabel.pack(expand=True)

def dice_simulator():
	Image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
	#update image
	ImageLabel.configure(image=Image1)
	#Keep a reference
	ImageLabel.image = Image1

button = tkinter.Button(window, text='Rolling Dice', fg='dark red', command=dice_simulator)

#Pack button widget on parent window
button.pack(expand=True)
#mainloop() is used to execute what we want to execute
#aka it let tkinter to start running application
window.mainloop()

