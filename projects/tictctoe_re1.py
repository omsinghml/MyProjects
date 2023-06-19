from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic Tac Toe")
#window.geometry("1200x710")

# X's Turn
clicked = True
count = 0

def disable_all_buttons():
	pass

def button_clicked(b):
	global clicked
	global count

	if b['text'] == ' ' and clicked == True:
		b['text'] = 'X'
		count += 1
		clicked = False
		win()

	elif b['text'] == ' ' and clicked == False:
		b['text'] = 'O'
		count += 1
		clicked = True
		win()

	else:
		messagebox.showerror("Tic Tac Toe", "Hey!, That Button is already clicked, try another.\n")

def win():
	global winner
	winner = False
	if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
		b1.config(bg='red')
		b2.config(bg='red')
		b3.config(bg='red')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "Congratulations!, X wins.")
		disable_all_buttons()


#-----------GUI APPLICATION------------------

b1 = Button(window, text=' ', height = 3, width = 6, bg = "SystemButtonFace", command = lambda : button_clicked(b1))
b2 = Button(window, text=' ', height = 3, width = 6, bg = "SystemButtonFace", command = lambda : button_clicked(b2))
b3 = Button(window, text=' ', height = 3, width = 6, bg = "SystemButtonFace", command = lambda : button_clicked(b3))

b4 = Button(window, text=' ', height = 3, width = 6, bg = "SystemButtonFace", command = lambda : button_clicked(b4))
b5 = Button(window, text=' ', height = 3, width = 6, bg = "SystemButtonFace", command = lambda : button_clicked(b5))
b6 = Button(window, text=' ', height = 3, width = 6, bg = "SystemButtonFace", command = lambda : button_clicked(b6))

b7 = Button(window, text=' ', height = 3, width = 6, bg = "SystemButtonFace", command = lambda : button_clicked(b7))
b8 = Button(window, text=' ', height = 3, width = 6, bg = "SystemButtonFace", command = lambda : button_clicked(b8))
b9 = Button(window, text=' ', height = 3, width = 6, bg = "SystemButtonFace", command = lambda : button_clicked(b9))

b1.grid(row =0, column = 0)
b2.grid(row =0, column = 1)
b3.grid(row =0, column = 2)

b4.grid(row =1, column = 0)
b5.grid(row =1, column = 1)
b6.grid(row =1, column = 2)

b7.grid(row =2, column = 0)
b8.grid(row =2, column = 1)
b9.grid(row =2, column = 2)


window.mainloop()