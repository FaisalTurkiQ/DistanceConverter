from tkinter import *
from tkinter import messagebox

# Dictionary of distance units and their conversion factors
distanceUnits = {
    "Meters": 1.0,
    "Kilometers": 1000.0,
    "Miles": 1609.34,
    "Yards": 0.9144,
    "Feet": 0.3048,
    "Centimeters": 0.01,
    "Millimeters": 0.001,
    "Inches": 0.0254,
    "Nautical Miles": 1852.0,
    "Leagues": 4828.03
}

def calculateDistance():
    try:
        value = valueEntry.get().strip()  # Get the value from the entry field and remove leading/trailing whitespaces
        if not value:
            messagebox.showerror("Error", "Input value is empty", parent=window)
            return
        value = float(value)
        fromUnit = var1.get()
        toUnit = var2.get()
        meters = value * distanceUnits[fromUnit]

        result = meters / distanceUnits[toUnit]
        answerLabel.config(text=f'Answer :\n {result:.2f} {toUnit}')
        valueEntry.delete(0, END)
    except ValueError:
        messagebox.showerror("Error", "Invalid input: Not a number", parent=window)

def clear():
    valueEntry.delete(0, END)
    answerLabel.config(text='Answer :\n')

window = Tk()
window.title('Convert Distance')

# Create a label for the title
titleLabel = Label(window, text="Convert Distance", font=('Arial', 26, 'bold'))
titleLabel.grid(row=0, column=0, columnspan=3)

# Create a label for the input description
inputLabel = Label(window, text='Value to Convert:', font=('Arial', 17))
inputLabel.grid(row=3, column=1)

# Create a label for the input hint
hintLabel = Label(window, text='Enter a real number or scientific notation', font=('Arial', 10, 'italic'), fg='gray')
hintLabel.grid(row=4, column=1)

# Create an entry field for the value to convert
valueEntry = Entry(window)
valueEntry.grid(row=5, column=1)

# Create a frame to hold the "From" and "To" labels and dropdown menus
unitFrame = Frame(window)
fromLabel = Label(unitFrame, text='From:')
fromLabel.grid(row=0, column=0)
toLabel = Label(unitFrame, text='To:')
toLabel.grid(row=1, column=0)

# Create dropdown menus for selecting the "From" and "To" units
var1 = StringVar(window)
var1.set('Kilometers')
fromDropdown = OptionMenu(unitFrame, var1, *distanceUnits)
fromDropdown.config(width=10)
fromDropdown.grid(row=0, column=1)

var2 = StringVar(window)
var2.set('Meters')
toDropdown = OptionMenu(unitFrame, var2, *distanceUnits)
toDropdown.config(width=10)
toDropdown.grid(row=1, column=1)

unitFrame.grid(row=6, column=1)

# Create a button to clear the input and answer
clearButton = Button(window, text="Clear", command=clear)
clearButton.grid(row=7, column=0)

# Create a button to calculate the conversion
calculateButton = Button(window, text="Calculate", command=calculateDistance)
calculateButton.grid(row=7, column=2)

# Create a label for displaying the answer
answerLabel = Label(window, text='Answer :\n', font=('Arial', 17))
answerLabel.grid(row=8, column=1)

window.mainloop()
