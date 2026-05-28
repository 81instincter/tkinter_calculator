# ==================================
# 5/27/2026
# At first I made it a simple four function calculator (add, sub, mult, div).
# I later expanded it to include a more expansive range of operations, handle decimal 
# numbers more smoothly, and can hold memory of past operations and display it on the side of the window.
#
# I plan to later use it to make an even more advanced calculator that can calculate
# integrals and derivatives, solve polynomials, and can perform arithmetic in different 
# number systems (e.g. binary, hexadecimal, octal).
# ==================================

from tkinter import *
expr = "" # Global expression string. Must change later to not be global since global vars are bad practice.

def press(key):
    global expr 
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try: 
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

#def negate():
    

def clear():
    global expr
    expr = ""
    display.set("")

# ==================================

if __name__ == "__main__": 

    root = Tk()
    root.configure(bg="SkyBlue4")
    root.title("Four Function Calculator")
    root.geometry("270x150")

    display = StringVar() # used to link widget values to Python code
    entry = Entry(root, textvariable=display, fg="white", bg="gray70")
    entry.grid(columnspan=4, ipadx=70)

    # ==================================
    # Number buttons: define number button widgets, and set their locations
    zero_button = Button(root, text="0", fg="black", bg="papaya whip",
                         command=lambda: press(0), height=1, width=7)
    zero_button.grid(row=5, column=1)
    
    one_button = Button(root, text="1", fg="black", bg="papaya whip",
                        command=lambda: press(1), height=1, width=7)
    one_button.grid(row=2, column=0)

    two_button = Button(root, text="2", fg="black", bg="papaya whip",
                        command=lambda: press(2), height=1, width=7)
    two_button.grid(row=2, column=1)

    three_button = Button(root, text="3", fg="black", bg="papaya whip",
                        command=lambda: press(3), height=1, width=7)
    three_button.grid(row=2, column=2)

    four_button = Button(root, text="4", fg="black", bg="papaya whip",
                        command=lambda: press(4), height=1, width=7)
    four_button.grid(row=3, column=0)

    five_button = Button(root, text="5", fg="black", bg="papaya whip",
                        command=lambda: press(5), height=1, width=7)
    five_button.grid(row=3, column=1)

    six_button = Button(root, text="6", fg="black", bg="papaya whip",
                        command=lambda: press(6), height=1, width=7)
    six_button.grid(row=3, column=2)

    seven_button = Button(root, text="7", fg="black", bg="papaya whip",
                        command=lambda: press(7), height=1, width=7)
    seven_button.grid(row=4, column=0)

    eight_button = Button(root, text="8", fg="black", bg="papaya whip",
                        command=lambda: press(8), height=1, width=7)
    eight_button.grid(row=4, column=1)

    nine_button = Button(root, text="9", fg="black", bg="papaya whip",
                        command=lambda: press(9), height=1, width=7)
    nine_button.grid(row=4, column=2)

    # ==================================
    # Operator Buttons
    plus_button = Button(root, text='+', fg="black", bg="papaya whip",
                         command=lambda: press('+'), height=1, width=7)
    plus_button.grid(row=2, column=3)

    minus_button = Button(root, text='-', fg="black", bg="papaya whip",
                          command=lambda: press('-'), height=1, width=7)
    minus_button.grid(row=3, column=3)

    mult_button = Button(root, text='*', fg="black", bg="papaya whip",
                         command=lambda: press('*'), height=1, width=7)
    mult_button.grid(row=4, column=3)

    div_button = Button(root, text='/', fg="black", bg="papaya whip",
                          command=lambda: press('/'), height=1, width=7)
    div_button.grid(row=5, column=3)

    # ==================================
    # Other Buttons
    equal_button = Button(root, text='=', fg="black", bg="papaya whip",
                          command=equal, height=1, width=7)
    equal_button.grid(row=5, column=2)

    clear_button = Button(root, text="Clear", fg="black", bg="papaya whip",
                          command=clear, height=1, width=7)
    clear_button.grid(row=6, column=3)

    decimal_button = Button(root, text='.', fg="black", bg="papaya whip",
                            command=lambda: press('.'), height=1, width=7)
    decimal_button.grid(row=6, column=0)

    # Need to design the negate() function so negate_button works
    #negate_button = Button(root, text="+/-", fg="black", bg="papaya whip",
    #                       command=negate, height=1, width=7)
    #negate_button.grid(row=5, column=0)

    open_par_button = Button(root, text='(', fg="black", bg="papaya whip",
                           command=lambda: press('('), height=1, width=7)
    open_par_button.grid(row=8, column=3)

    close_par_button = Button(root, text='(', fg="black", bg="papaya whip",
                           command=lambda: press(')'), height=1, width=7)
    close_par_button.grid(row=8, column=4)

    exp_button = Button(root, text='^', fg="black", bg="papaya whip",
                           command=lambda: press('^'), height=1, width=7)
    exp_button.grid(row=8, column=2)

    modulo_button = Button(root, text='%', fg="black", bg="papaya whip",
                           command=lambda: press('%'), height=1, width=7)
    modulo_button.grid(row=8, column=1)

    # ==================================
    # Run program
    root.mainloop()