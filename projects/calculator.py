from tkinter import *
from math import factorial

window = Tk()
window.title("Calculator")


#get variable
#i is the position of the input
i=0
def get_variable(num):
	global i
	display.insert(i, num)
	i+=num

def calculate():
	new_variable = display.get()
	try:
		result = eval(new_variable)
		clear_all()
		display.insert(0,result)
	except Exception:
		clear_all()
		display.insert(0, 'ERROR')

def clear_all():
	display.delete(0, END)

def get_operation(operator):
	global i
	length = len(operator)
	display.insert(i, operator)
	i+=length

def get_factorial(fact):
	fact = display.get()
	try:
		new_val = factorial(int(fact))
		clear_all()
		display.insert(0, new_val)
	except Exception:
		clear_all()
		display.insert(0, "ERROR")

def undo():
	entire_string = display.get()
	if len(entire_string):
		a = entire_string[:-1]
		clear_all()
		display.insert(0, a)
	else:
		clear_all()
		display.insert(0,"ERROR")

#----------------------------------------UI Design---------------------------------------------- 
 
display = Entry(window)
display.bind('<Key>', lambda b:"break")
display.grid(rows=1, columnspan=6, sticky=N+E+W+S)

Button(window, text="1", command= lambda: get_variable(1)).grid(row=2, column=0, sticky=N+S+E+W)
Button(window, text=" 2", command= lambda: get_variable(2)).grid(row=2, column=1, sticky=N+S+E+W)
Button(window, text=" 3", command= lambda: get_variable(3)).grid(row=2, column=2, sticky=N+S+E+W)

Button(window, text="4", command= lambda: get_variable(4)).grid(row=3, column=0, sticky=N+S+E+W)
Button(window, text=" 5", command= lambda: get_variable(5)).grid(row=3, column=1, sticky=N+S+E+W)
Button(window, text=" 6", command= lambda: get_variable(6)).grid(row=3, column=2, sticky=N+S+E+W)

Button(window, text=" 7", command= lambda: get_variable(7)).grid(row=4, column=0, sticky=N+S+E+W)
Button(window, text=" 8", command= lambda: get_variable(8)).grid(row=4, column=1, sticky=N+S+E+W)
Button(window, text=" 9", command= lambda: get_variable(9)).grid(row=4, column=2, sticky=N+S+E+W)

Button(window, text="0", command= lambda: get_variable(0)).grid(row=5, column=1, sticky=N+S+E+W)
Button(window, text=".", command= lambda: get_operation(".")).grid(row=5, column=2, sticky=N+S+E+W)

Button(window, text="*", command= lambda: get_operation("*")).grid(row=2, column=3, sticky=N+S+E+W)
Button(window, text="/", command= lambda: get_operation("/")).grid(row=3, column=3, sticky=N+S+E+W)
Button(window, text="-", command= lambda: get_operation("-")).grid(row=4, column=3, sticky=N+S+E+W)
Button(window, text="+", command= lambda: get_operation("+")).grid(row=5, column=3, sticky=N+S+E+W)

Button(window, text="<--", command= lambda: undo()).grid(row=2, column=4, sticky=N+S+E+W)

Button(window, text="!", command= lambda: get_factorial("!")).grid(row=3, column=4, sticky=N+S+E+W)

Button(window, text="=", command= lambda: calculate()).grid(row=6, columnspan=4, sticky=N+S+E+W)

Button(window, text="AC", command= lambda: clear_all()).grid(row=5, column=0, sticky=N+S+E+W)


window.mainloop()
