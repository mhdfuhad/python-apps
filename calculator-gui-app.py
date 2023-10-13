from tkinter import *

root = Tk()
root.title("Calculator")


def create_button(root, text, row, column, command=None):
    btn = Button(root, text=text, pady=20, padx=30, command=command)
    btn.grid(row=row, column=column)
    return btn


e = Entry(root, width=30, borderwidth=2)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


previousInserted = ""


def inputIntoEntry(data):
    global previousInserted

    if previousInserted.strip() in ["+", "-", "/", "*"] and data.strip() in ["+", "-", "/", "*"]:
        pass
    else:
        e.insert(len(e.get()), data)
        previousInserted = data


# Number Buttons
for i in range(10):
    row, col = divmod(i + 3, 3)
    create_button(root, str(9 - i), row, col,
                  command=lambda num=(9 - i): inputIntoEntry(str(num)))


def evalButton():
    global previousInserted
    strToEval = [i for i in e.get().split(" ") if i.isdigit()
                 or i.replace(".", "", 1).isdigit() or i.replace("-", "", 1).isdigit()]
    operatorsInSequence = [i for i in e.get().split(" ") if i in [
        "+", "-", "/", "*"]]

    value = float(strToEval[0]) if "." in strToEval[0] else int(strToEval[0])

    for i in range(len(operatorsInSequence)):
        if operatorsInSequence[i] == "+":
            value += int(strToEval[i + 1])
        elif operatorsInSequence[i] == "-":
            value -= int(strToEval[i + 1])
        elif operatorsInSequence[i] == "/":
            value /= int(strToEval[i + 1])
        elif operatorsInSequence[i] == "*":
            value *= int(strToEval[i + 1])

    previousInserted = str(value)

    e.delete(0, END)
    e.insert(0, value)


# Clear Button
clearButton = create_button(
    root, "C", 0, 3, command=lambda: e.delete(0, END))

# Evaluate Button
evalBtn = Button(root, text="=", pady=20, padx=70,
                 command=evalButton)
evalBtn.grid(row=4, column=1, columnspan=2)

# Operator Buttons
operators = ["+", "-", "/", "*"]
for i, operator in enumerate(operators, start=1):
    create_button(root, operator, i, 3,
                  lambda op=operator: inputIntoEntry(f" {op} "))


root.mainloop()
