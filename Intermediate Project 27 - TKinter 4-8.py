""""
Project Twenty Seven - TKinter Miles to Kms.
Easy Tkinter program that converts miles to kms
"""
from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=150, height=100)

# Labels
label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label2 = Label(text="Km")
label2.grid(column=2, row=1)
label3 = Label(text="is equal to")
label3.grid(column=0, row=1)
label4 = Label(text="")
label4.grid(column=1, row=1)


# Buttons
def action():
    x = float(entry.get())
    ans = x * 1.609
    label4.config(text=ans)


# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

# Entries
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="0")

# Gets text in entry
print(entry.get())
entry.grid(column=1, row=0)


window.mainloop()
