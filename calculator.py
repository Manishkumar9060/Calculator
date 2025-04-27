from tkinter import *

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))  
        equation.set(total)
        expression = total  
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

root = Tk()
root.configure(bg="lightgray")
root.title("Simple Calculator")
root.geometry("544x644")

expression = ""
equation = StringVar()


entry_field = Entry(root, textvariable=equation, font="lucida 30 bold", justify='right' , bg="lightgrey")
entry_field.grid(columnspan=4, ipadx=8, ipady=15, padx=10, pady=10)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('/', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('0', 4, 0), ('00', 4, 1), ('%', 4, 2), ('=', 4, 3),
    ('C', 5, 0) ,("." , 5 ,1), ("-" , 5, 2),("Close",5,3)
]

for (text, row, col) in buttons:
    if text == '=':
        Button(root, text=text, fg='white', bg='green', height=2, width=7, font=('Arial', 14),
               command=equalpress).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'C':
        Button(root, text=text, fg='white', bg='pink', height=2, width=7, font=('Arial', 14),
               command=clear).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'Close':
        Button(root, text=text, fg='white', bg='red', height=2, width=7, font=('Arial', 14),
               command=root.destroy).grid(row=row, column=col, padx=5, pady=5)
        
    else:
        Button(root, text=text, height=2, width=7, font=('Arial', 14),
               command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()


