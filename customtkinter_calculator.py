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

img = Image.open("delete.png")

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
    entry = CTkEntry(master=root, textvariable=display, 
                     fg_color="#BAA7BF", border_color="#F3F3FF", text_color="#514354",
                     width=500, height=100, font=("Arial", 30))
    entry.grid(columnspan=4, ipadx=70)

    # Displaying past arithmetic expressions and their results.
    calc_history_box = CTkTextbox(master=root, 
                         border_color="#EAE2ED",fg_color="#D7C9DB", text_color="#514354", scrollbar_button_color="#724060",
                         width=300, height=100, border_width = 0.5, corner_radius=16)
    calc_history_box.grid(row=0, column=4, padx = 10, pady=10)

    # =================================================
    # Number buttons: define number button widgets, and set their locations.
    zero_button = CTkButton(master=root, text="0", 
                            border_color = "papaya whip", fg_color = "#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=lambda: press(0),
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    zero_button.grid(row=7, column=1, padx=0, pady=0, sticky="nsew")
    
    one_button = CTkButton(master=root, text="1",
                           border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                           command=lambda: press(1),
                           height=75, width=75, border_width = 0.5, font=("Arial",28))
    one_button.grid(row=4, column=0, padx=0, pady=0, sticky="nsew")

    two_button = CTkButton(master=root, text="2",
                           border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                           command=lambda: press(2),
                           height=75, width=75, border_width = 0.5, font=("Arial",28))
    two_button.grid(row=4, column=1, padx=0, pady=0, sticky="nsew")

    three_button = CTkButton(master=root, text="3", 
                             border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                             command=lambda: press(3),
                             height=75, width=75, border_width = 0.5, font=("Arial",28))
    three_button.grid(row=4, column=2, padx=0, pady=0, sticky="nsew")

    four_button = CTkButton(master=root, text="4",
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=lambda: press(4),
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    four_button.grid(row=5, column=0, padx=0, pady=0, sticky="nsew")

    five_button = CTkButton(master=root, text="5",
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=lambda: press(5),
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    five_button.grid(row=5, column=1, padx=0, pady=0, sticky="nsew")

    six_button = CTkButton(master=root, text="6",
                           border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                           command=lambda: press(6),
                           height=75, width=75, border_width = 0.5, font=("Arial",28))
    six_button.grid(row=5, column=2, padx=0, pady=0, sticky="nsew")

    seven_button = CTkButton(master=root, text="7",
                             border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                             command=lambda: press(7),
                             height=75, width=75, border_width = 0.5, font=("Arial",28))
    seven_button.grid(row=6, column=0, padx=0, pady=0, sticky="nsew")

    eight_button = CTkButton(master=root, text="8",
                             border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                             command=lambda: press(8),
                             height=75, width=75, border_width = 0.5, font=("Arial",28))
    eight_button.grid(row=6, column=1, padx=0, pady=0, sticky="nsew")

    nine_button = CTkButton(master=root, text="9",
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=lambda: press(9),
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    nine_button.grid(row=6, column=2, padx=0, pady=0, sticky="nsew")

    # ==================================
    # Operator Buttons.
    div_button = CTkButton(master=root, text='/',
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=lambda: press('/'),
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    div_button.grid(row=2, column=3, padx=0, pady=0, sticky="nsew")

    mult_button = CTkButton(master=root, text='*',
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=lambda: press('*'),
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    mult_button.grid(row=3, column=3, padx=0, pady=0, sticky="nsew")

    minus_button = CTkButton(master=root, text='-',
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=lambda: press('-'),
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    minus_button.grid(row=4, column=3, padx=0, pady=0, sticky="nsew")
    
    plus_button = CTkButton(master=root, text='+',
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=lambda: press('+'),
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    plus_button.grid(row=5, column=3, padx=0, pady=0, sticky="nsew")

    # ==================================
    # Other Buttons.

    modulo_button = CTkButton(master=root, text='%',
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=lambda: press('%'),
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    modulo_button.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")

    clear_entry_button = CTkButton(master=root, text='CE',
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=clear_entry,
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    clear_entry_button.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")

    clear_button = CTkButton(master=root, text="Clear",
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=clear,
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    clear_button.grid(row=1, column=2, padx=0, pady=0, sticky="nsew")

    clear_history_button = CTkButton(master=root, text="Clear History", 
                                     border_color = "papaya whip", hover_color = "#2B3A67", text_color="white", fg_color="#2A0C2F", 
                                     command=clear_history,
                                     height=30, width=50, border_width = 0.5, font=("Arial",20))
    clear_history_button.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")

# image is there but is just black and blends in with button
    backspace_button = CTkButton(master=root, text="",
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=backspace,
                            height=75, width=75, border_width = 0.5, font=("Arial",28),
                            image = CTkImage(dark_image=img, light_image=img))
    backspace_button.grid(row=1, column=3, padx=0, pady=0, sticky="nsew")

    inverse_button = CTkButton(master=root, text="1/x",
                               border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                               command=inverse, 
                               height=75, width=75, border_width = 0.5, font=("Arial",28))
    inverse_button.grid(row=2, column=0, padx=0, pady=0, sticky="nsew") # padx=0 and pady=0 removes spacing between widget and its grid neighbors

    exp_button = CTkButton(master=root, text='^',
                           border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                           command=lambda: press('^'),
                           height=75, width=75, border_width = 0.5, font=("Arial",28))
    exp_button.grid(row=2, column=1, padx=0, pady=0, sticky="nsew")

    sqr_root_button = CTkButton(master=root, text="√",
                                border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                                command=inverse, 
                                height=75, width=75, border_width = 0.5, font=("Arial",28))
    sqr_root_button.grid(row=2, column=2, padx=0, pady=0, sticky="nsew")

    square_button = CTkButton(master=root, text="x^2",
                              border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                              command=square,
                              height=75, width=75, border_width = 0.5, font=("Arial",28))
    square_button.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")

    open_par_button = CTkButton(master=root, text='(', 
                                border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                                command=lambda: press('('),
                                height=75, width=75, border_width = 0.5, font=("Arial",28))
    open_par_button.grid(row=3, column=1, padx=0, pady=0, sticky="nsew")

    close_par_button = CTkButton(master=root, text=')', 
                                border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                                command=lambda: press(')'),
                                height=75, width=75, border_width = 0.5, font=("Arial",28))
    close_par_button.grid(row=3, column=2, padx=0, pady=0, sticky="nsew")

    negate_button = CTkButton(master=root, text="+/-", 
                               border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                               command=lambda: press('-'),
                               height=75, width=75, border_width = 0.5, font=("Arial",28))
    negate_button.grid(row=7, column=0, padx=0, pady=0, sticky="nsew")

    decimal_button = CTkButton(master=root, text='.',
                               border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                               command=lambda: press('.'),
                               height=75, width=75, border_width = 0.5, font=("Arial",28))
    decimal_button.grid(row=7, column=2, padx=0, pady=0, sticky="nsew")

    equal_button = CTkButton(master=root, text='=', 
                            border_color = "papaya whip", fg_color="#2A0C2F", bg_color="papaya whip", hover_color = "#2B3A67", text_color="white",
                            command=equal,
                            height=75, width=75, border_width = 0.5, font=("Arial",28))
    equal_button.grid(row=7, column=3, padx=0, pady=0, sticky="nsew")

    # =================================================
    # Run calculator app.
    root.mainloop()