# ==================================
# 5/27/2026
# This file serves as a general template of how Tkinter
# GUIs are programmed. They are composed of these 3 fundamental components:
# 1.) A root window object.
# 2.) Widgets of UI.
# 3.) A .mainloop() acting on the root window object.
# ==================================
# Import module
from tkinter import *

# Create root window
root = Tk()

# Root window title and dimensions
root.title("Welcome to Elijah's First GUI")
# Set geometry (widthxheight)
root.geometry('350x200')

# =====Widgets=====

# === Menu Bar
menu = Menu(root) # add menu bar in root window

# new item in menu bar is labelled as 'New'
item = Menu(menu) 
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# === Label
# Adding a label to the root window
label = Label(root, text="Hi, how are ya?")
label.grid()

# === Entry Field
# Adding entry field
txt = Entry(root, width=10)
txt.grid(column=1, row=0)

# === Button
# Function to display text when button is clicked
def button_clicked():
    res = "You wrote " + txt.get() #.get() retrieves data from Entry field object
    label.configure(text=res)

# Button widget with red color text inside
button = Button(root, text = "Click me", fg="red", command=button_clicked)

# Set Button grid
button.grid(column=2, row=0)

# =================

# Execute Tkinter
root.mainloop()
