# =================================================
# This program uses the CustomTkinter library to create a calculator app that is capable of arithemic operations.
# It shares a layout similar to the Windows calculator whilst having a color scheme similar to ProtonVPN.
# The style of my GUIs and apps I want to follow a style similar to Proton, since their combination of 
# dark cool colors focusing on purple and blue are very visually-appealing to me.
# I plan to expand this program later on to include capabilities of solving algebraic equations, evaluating
# integrals and derivatives, support different number systems (binary, hexadecimal, octal),
# and maybe even include graphing capabilities.
# =================================================
from customtkinter import *
from tkinter import END # The END constant allows me to index the end of a CTkTextbox() object for inserting and deleting lines.
from PIL import Image # For including icons in the app.

expr = "" 

# Memory and history of past expressions and their results.
past_expressions_list = []
past_results_list = []

img = Image.open("backspace_icon.png")

def press(key):
    global expr 
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try: 
        result = str(eval(expr))

        display.set(result)
        past_expressions_list.append(expr)
        past_results_list.append(result)

        # Display result of inverse function onto the calculator's history screen. 
        calc_history_box.insert(END, f"{past_expressions_list[-1]}\n\t = {past_results_list[-1]}\n")

        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

# Removes most recent number entered that comes after the latest operator in the expression.
def clear_entry(): 
    global expr
    if expr: # If expr is not empty.
        i = len(expr) - 1

        # Move backwards while characters are digits or decimal points.
        while i >= 0 and (expr[i].isnumeric() or expr[i] == '.'):  
            i -= 1

        # Keep everything up to and including the operator.
        expr = expr[:i+1]
        display.set(expr)

def clear_history():
    past_expressions_list.clear()
    past_results_list.clear()
    calc_history_box.delete("0.0", END) # Clears calculator history display.

def backspace():
    global expr
    if expr:
        expr = expr[:-1]
        display.set(expr)

def inverse():
    global expr
    inv_result = 1/float(eval(expr)) 

    past_expressions_list.append("1/" + expr)
    past_results_list.append(inv_result)
    display.set(inv_result)

    # Display result of inverse function onto the calculator's history screen. 
    calc_history_box.insert(END, f"{past_expressions_list[-1]}\n\t = {past_results_list[-1]}\n")

def square():
    global expr
    square_result = eval(expr)**2

    past_expressions_list.append(f"({expr})^2")
    past_results_list.append(square_result)
    display.set(square_result)

    # Display result of inverse function onto the calculator's history screen. 
    calc_history_box.insert(END, f"{past_expressions_list[-1]}\n\t = {past_results_list[-1]}\n")

# =================================================

if __name__ == "__main__": 

    root = CTk()
    root.title("CTk Calculator")
    root.geometry("500x400")
    set_appearance_mode("dark")

    # Displaying the numbers pressed and their results on the top display bar.
    display = StringVar()
    entry = CTkEntry(master=root, textvariable=display, width=500)
    entry.grid(columnspan=4, ipadx=70)

    # Displaying past arithmetic expressions and their results.
    calc_history_box = CTkTextbox(master=root, 
                         scrollbar_button_color="#FFCC70",
                         width=300, height=200, corner_radius=16)
    calc_history_box.grid(row=2, column=4)

    # =================================================
    # Number buttons: define number button widgets, and set their locations.
    zero_button = CTkButton(master=root, text="0", 
                            fg_color = "black", bg_color="white",
                            command=lambda: press(0),
                            height=50, width=50)
    zero_button.grid(row=7, column=1)
    
    one_button = CTkButton(master=root, text="1",
                           fg_color="black", bg_color="papaya whip",
                           command=lambda: press(1),
                           height=50, width=50)
    one_button.grid(row=4, column=0)

    two_button = CTkButton(master=root, text="2",
                           fg_color="black", bg_color="papaya whip",
                           command=lambda: press(2),
                           height=50, width=50)
    two_button.grid(row=4, column=1)

    three_button = CTkButton(master=root, text="3", 
                             fg_color="black", bg_color="papaya whip",
                             command=lambda: press(3),
                             height=50, width=50)
    three_button.grid(row=4, column=2)

    four_button = CTkButton(master=root, text="4",
                            fg_color="black", bg_color="papaya whip",
                            command=lambda: press(4),
                            height=50, width=50)
    four_button.grid(row=5, column=0)

    five_button = CTkButton(master=root, text="5",
                            fg_color="black", bg_color="papaya whip",
                            command=lambda: press(5),
                            height=50, width=50)
    five_button.grid(row=5, column=1)

    six_button = CTkButton(master=root, text="6",
                           fg_color="black", bg_color="papaya whip",
                           command=lambda: press(6),
                           height=50, width=50)
    six_button.grid(row=5, column=2)

    seven_button = CTkButton(master=root, text="7",
                             fg_color="black", bg_color="papaya whip",
                             command=lambda: press(7),
                             height=50, width=50)
    seven_button.grid(row=6, column=0)

    eight_button = CTkButton(master=root, text="8",
                             fg_color="black", bg_color="papaya whip",
                             command=lambda: press(8),
                             height=50, width=50)
    eight_button.grid(row=6, column=1)

    nine_button = CTkButton(master=root, text="9",
                            fg_color="black", bg_color="papaya whip",
                            command=lambda: press(9),
                            height=50, width=50)
    nine_button.grid(row=6, column=2)

    # ==================================
    # Operator Buttons.
    div_button = CTkButton(master=root, text='/',
                            fg_color="black", bg_color="papaya whip",
                            command=lambda: press('/'),
                            height=50, width=50)
    div_button.grid(row=2, column=3)

    mult_button = CTkButton(master=root, text='*',
                            fg_color="black", bg_color="papaya whip",
                            command=lambda: press('*'),
                            height=50, width=50)
    mult_button.grid(row=3, column=3)

    minus_button = CTkButton(master=root, text='-',
                            fg_color="black", bg_color="papaya whip",
                            command=lambda: press('-'),
                            height=50, width=50)
    minus_button.grid(row=4, column=3)
    
    plus_button = CTkButton(master=root, text='+',
                            fg_color="black", bg_color="papaya whip",
                            command=lambda: press('+'),
                            height=50, width=50)
    plus_button.grid(row=5, column=3)

    # ==================================
    # Other Buttons.

    modulo_button = CTkButton(master=root, text='%',
                            fg_color="black", bg_color="papaya whip",
                            command=lambda: press('%'),
                            height=50, width=50)
    modulo_button.grid(row=1, column=0)

    clear_entry_button = CTkButton(master=root, text='CE',
                            fg_color="black", bg_color="papaya whip",
                            command=clear_entry,
                            height=50, width=50)
    clear_entry_button.grid(row=1, column=1)

    clear_button = CTkButton(master=root, text="Clear",
                            fg_color="black", bg_color="papaya whip",
                            command=clear,
                            height=50, width=50)
    clear_button.grid(row=1, column=2)

    clear_history_button = CTkButton(master=root, text="Clear History",
                                     fg_color="black", bg_color="papaya whip",
                                     command=clear_history,
                                     height=30, width=50)
    clear_history_button.grid(row=4, column=4)

# image is there but is just black and blends in with button
    backspace_button = CTkButton(master=root, text="",
                            fg_color="black", bg_color="papaya whip",
                            command=backspace,
                            height=50, width=50,
                            image = CTkImage(dark_image=img, light_image=img))
    backspace_button.grid(row=1, column=3)

    inverse_button = CTkButton(master=root, text="1/x",
                               fg_color="black", bg_color="papaya whip",
                               command=inverse, 
                               height=50, width=50)
    inverse_button.grid(row=2, column=0)

    exp_button = CTkButton(master=root, text='^',
                           fg_color="black", bg_color="papaya whip",
                           command=lambda: press('^'),
                           height=50, width=50)
    exp_button.grid(row=2, column=1)

    sqr_root_button = CTkButton(master=root, text="√",
                                fg_color="black", bg_color="papaya whip",
                                command=inverse, 
                                height=50, width=50)
    sqr_root_button.grid(row=2, column=2)

    square_button = CTkButton(master=root, text="x^2",
                              fg_color="black", bg_color="papaya whip",
                              command=square,
                              height = 50, width=50)
    square_button.grid(row=3, column=0)

    open_par_button = CTkButton(master=root, text='(', 
                                fg_color="black", bg_color="papaya whip",
                                command=lambda: press('('),
                                height=50, width=50)
    open_par_button.grid(row=3, column=1)

    close_par_button = CTkButton(master=root, text=')', 
                                fg_color="black", bg_color="papaya whip",
                                command=lambda: press(')'),
                                height=50, width=50)
    close_par_button.grid(row=3, column=2)

    negate_button = CTkButton(master=root, text="+/-", 
                               fg_color="black", bg_color="papaya whip",
                               command=lambda: press('-'),
                               height=50, width=50)
    negate_button.grid(row=7, column=0)

    decimal_button = CTkButton(master=root, text='.',
                               fg_color="black", bg_color="papaya whip",
                               command=lambda: press('.'),
                               height=50, width=50)
    decimal_button.grid(row=7, column=2)

    equal_button = CTkButton(master=root, text='=', 
                            fg_color="black", bg_color="papaya whip",
                            command=equal,
                            height=50, width=50)
    equal_button.grid(row=7, column=3)

    # =================================================
    # Run calculator app.
    root.mainloop()