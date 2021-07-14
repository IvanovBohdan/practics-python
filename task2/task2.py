from tkinter import *
buttons = []
current_result = 0
current_number = 0
current_operand = ""
flag = False
first = True
def addNumber(number):
	global current_number
	global flag
	if flag:
		current_number = 0
		inputArea['text'] = '0'
		flag = False
	if len(inputArea['text']) < 9:
		if inputArea['text'] != '0':
			inputArea['text'] += str(number)
		else:
			inputArea['text'] = str(number)
	current_number = int(inputArea['text'])

def operation(operand):
	global flag
	global current_result
	global current_number
	global current_operand
	current_number = int(inputArea['text'])
	operandArea['text'] = operand
	current_operand = operand
	if first:
		current_result = current_number

	flag = True

def calc():
	global current_number
	global current_result
	global current_operand
	global flag

	if current_operand == "+":
		current_result += current_number
	elif current_operand == "-":
		current_result -= current_number
	elif current_operand == "*":
		current_result *= current_number
	elif current_operand == "/":
		current_result /= current_number

	inputArea['text'] = str(current_result)
	operandArea = ""
	current_operand = ""
	flag = True

def clear():
	current_number = 0
	inputArea['text'] = '0'


root = Tk()
root.title("Calculator")
root.resizable(width = False, height = False)
inputArea = Label(root, anchor="w", bg = "#fff", text = "0", font = "Arial 20", width = 14)
inputArea.pack()
operandArea = Label(root, width = 30, anchor="w")
operandArea.pack()

f_kb = Frame(root)

for i in range(10):
	buttons.append(Button(f_kb, width = 7, height = 3, text = str(i), command = lambda number = i: addNumber(number)))

plus = Button(f_kb, width = 7, height = 3, text = "+", command = lambda arg="+": operation(arg))
minus = Button(f_kb, width = 7, height = 3, text = "-", command = lambda arg="-": operation(arg))
mult = Button(f_kb, width = 7, height = 3, text = "*", command = lambda arg="*": operation(arg))
div = Button(f_kb, width = 7, height = 3, text = "/", command = lambda arg="/": operation(arg))
clear = Button(f_kb, width = 7, height = 3, text = "C", command = clear)
equal = Button(f_kb, width = 7, height = 3, text = "=", command = calc)

f_kb.pack()

n = 1
for i in range(3):
	for j in range(3):
		buttons[n].grid(row = i, column = j)
		n += 1
buttons[0].grid(row = 3, column = 0)
plus.grid(row = 0, column = 4)
minus.grid(row = 1, column = 4)
mult.grid(row = 2, column = 4)
div.grid(row = 3, column = 4)
equal.grid(row = 3, column = 1)
clear.grid(row = 3, column = 2)




root.mainloop()
