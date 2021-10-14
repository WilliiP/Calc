import tkinter as tk
import math as m

def Click(number):
          val = entry.get()
          entry.delete(0, tk.END)
          entry.insert(0, val + number)

def Clear():
    entry.delete(0, tk.END)

def Add():
    try:
         entry.get()
         global num
         global operator
         operator = "addition"
         num = int(float(entry.get()))
         entry.delete(0, tk.END)
    except ValueError:
        entry.insert(0, "")

def Multiply():
    try:
        entry.get()
        global num
        global operator
        operator = "multiply"
        num = int(float(entry.get()))
        entry.delete(0, tk.END)
    except ValueError:
        entry.insert(0, "")

def Divide():
    try:
        entry.get()
        global num
        global operator
        operator = "division"
        num = int(float(entry.get()))
        entry.delete(0, tk.END)
    except ValueError:
        entry.insert(0, "")

def Subtract():
    try:
        entry.get()
        global num
        global operator
        operator = "subtraction"
        num = int(float(entry.get()))
        entry.delete(0, tk.END)
    except ValueError:
        entry.insert(0, "")

def Sqrt():
    entry.get()
    global num
    global operator
    operator = "sqrt"
    num = entry.get()
    entry.delete(0, tk.END)

def Percentage():
    entry.get()
    global num
    global operator
    operator = "percentage" 
    num = int(float(entry.get()))
    entry.delete(0, tk.END)

def Equal():
    global answer
    if operator == "addition":
         num2 = entry.get()
         entry.delete(0, tk.END)
         answer = entry.insert(0, num + int(num2))
    if operator == "multiply":
        num2 = entry.get()
        entry.delete(0, tk.END)
        answer = entry.insert(0, num * int(num2))
    if operator == "division":
        try:
             num2 = entry.get()
             entry.delete(0, tk.END)
             answer = entry.insert(0, num / int(num2))
        except ZeroDivisionError:
             entry.insert(0, "Error")     
    if operator == "subtraction":
        num2 = entry.get()
        entry.delete(0, tk.END)
        answer = entry.insert(0, num - int(num2))
    if operator == "sqrt":
        answer = str(m.sqrt(float(num)))
        entry.insert(0, answer)
    if operator == "percentage":
        num2 = entry.get()
        entry.delete(0, tk.END)
        answer = entry.insert(0, (num * int(num2) / 100))
    
WIDTH = 300
HEIGHT = 400

window = tk.Tk()
window.title("Children's Calculator")

window.resizable(0, 0)

canvas = tk.Canvas(window, height = HEIGHT, width = WIDTH)
canvas.pack()

backgroundImage = tk.PhotoImage(file = "Background.png")
background = tk.Label(window, image = backgroundImage)
background.place(relwidth = 1, relheight = 1)

frame = tk.Frame(window, bg = "pink")
frame.place(relx = 0.5, rely = 0.1, relwidth=0.75, relheight = 0.1, anchor = "n")

entry = tk.Entry(frame, bg = "light pink", font = "aeriel", justify = "right", relief = "solid")
entry.place(relwidth = 1, relheight= 1)

lowerFrame = tk.Frame(window, bg ="black")
lowerFrame.place(relx = 0.5, rely = 0.2, relwidth = 0.75, relheight = 0.65, anchor = "n" )

button1 = tk.Button(lowerFrame, text = "1", width = 7, height = 3, relief = "solid", command = lambda: Click("1"))
button2 = tk.Button(lowerFrame,text = "2", width = 7, height = 3, relief = "solid",command = lambda: Click("2"))
button3 = tk.Button(lowerFrame,text = "3", width = 7, height = 3, relief = "solid",command = lambda: Click("3"))
button4 = tk.Button(lowerFrame,text = "4", width = 7, height = 3, relief = "solid", command = lambda: Click("4"))
button5 = tk.Button(lowerFrame,text = "5", width = 7, height = 3, relief = "solid",command = lambda: Click("5"))
button6 = tk.Button(lowerFrame,text = "6", width = 7, height = 3, relief = "solid",command = lambda: Click("6"))
button7 = tk.Button(lowerFrame,text = "7", width = 7, height = 3, relief = "solid",command = lambda: Click("7"))
button8 = tk.Button(lowerFrame,text = "8", width = 7, height = 3, relief = "solid",command = lambda: Click("8"))
button9 = tk.Button(lowerFrame,text = "9", width = 7, height = 3, relief = "solid",command = lambda: Click("9"))
button0 = tk.Button(lowerFrame,text = "0", width = 7, height = 3, relief = "solid",command = lambda: Click("0"))
buttonDecimal = tk.Button(lowerFrame,text = ".", width = 7, height = 3, relief = "solid", command = lambda: Click("."))
buttonEqual = tk.Button(lowerFrame, text = "=", width = 14, pady = 7, relief = "solid", command = lambda: Equal())
buttonClear = tk.Button(lowerFrame,text = "C", width = 7, height = 3, relief = "solid",command = lambda: Clear())
buttonAdd = tk.Button(lowerFrame, text = "+", width = 6, height = 3, relief = "solid", command = lambda: Add())
buttonSubtract = tk.Button(lowerFrame, text = "-", width = 6, height = 3, relief = "solid", command = lambda: Subtract())
buttonMultiply = tk.Button(lowerFrame, text = "*", width = 6, height = 3, relief = "solid", command = lambda: Multiply())
divideImage = tk.PhotoImage(file = "divide.png")
buttonDivide = tk.Button(lowerFrame, image = divideImage, width = 45, height = 50, relief = "solid", command = lambda: Divide())
sqrtImage = tk.PhotoImage(file = "sqrt.png")
buttonSqrt = tk.Button(lowerFrame, image = sqrtImage, width = 53, height = 32, relief = "solid", command = lambda: Sqrt())
percentImage = tk.PhotoImage(file = "percentage.png")
buttonPercent = tk.Button(lowerFrame, image = percentImage, width = 53, height = 32, relief = "solid", command = lambda: Percentage())

button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button7.grid(row = 3, column = 0)
button8.grid(row = 3, column = 1)
button9.grid(row = 3, column = 2)
button0.grid(row = 4, column = 0)

buttonEqual.grid(row = 0, column = 2, columnspan = 2)
buttonClear.grid(row=4, column = 1)
buttonDecimal.grid(row = 4, column = 2)
buttonAdd.grid(row = 1, column = 3)
buttonSubtract.grid(row = 2, column = 3)
buttonMultiply.grid(row = 4, column = 3)
buttonDivide.grid(row = 3, column = 3)
buttonSqrt.grid(row = 0, column = 0)
buttonPercent.grid(row = 0, column = 1)

window.mainloop()


