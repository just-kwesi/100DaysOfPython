from tkinter import *

window = Tk()
window.minsize(width=150, height=100)
window.config(padx=40, pady=20)
window.title("Mile to KM Converter")

milesLabel = Label(text="Miles")
otherLabel = Label(text="is equal to")
kmLabel = Label(text="Km")
resultLabel = Label(text="0", font=("Arial", 24, "bold"))


def convert():
    miles = float(inputLabel.get())
    km = round((miles * 1.60934),2)
    kmStr = str(km)

    resultLabel.config(text=km)


# Entry
inputLabel = Entry()

# button
button = Button(text="Calculate", command=convert)

inputLabel.grid(column=1, row=0)
milesLabel.grid(column=2, row=0)
otherLabel.grid(column=0, row=1)
resultLabel.grid(column=1, row=1)
kmLabel.grid(column=2, row=1)
button.grid(column=1, row=2)

window.mainloop()
