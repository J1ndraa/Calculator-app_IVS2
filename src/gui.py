from tkinter import *
import tkinter as tk
from args_handler import InputArgs

BUTTON_WIDTH = 6
BUTTON_HEIGHT = 2
BUTTON_TEXT_SIZE = 20
DARKBLUE = "#1167b1"
LIGHTBLUE = "#2a9df4"


calculation = ""

def check_text():
    return

def append_char(parameter):
    global calculation

    if (parameter < '0' or parameter > '9') and parameter != "+" and parameter != "-" and parameter != "*" and parameter != "/" and parameter != "^" and parameter != "%" and parameter != "(" and parameter != ")" and parameter != "." and parameter != "!" and parameter != "√":
        print("Key not allowed", parameter)
        check_text
        return 

    if calculation == "Error":
        text_result.delete(1.0, "end")
        calculation = ""

    text_result.insert("end", parameter)
    calculation += str(parameter)
    print(calculation)

def remove_char():
    print("removing char...")
    global calculation
    if len(calculation) != 0:
        if calculation == "Error":
            calculation = ""
            text_result.delete(1.0, "end")
        else:
            calculation = calculation[:-1]
            text_result.delete("end-2c", "end")
    print(calculation)

def export_list():
    global calculation
    if len(calculation) == 0:
        return 
    text_result.delete(1.0, "end")

    global result
    print("String to process:",calculation)

    try:
        inputArgs = InputArgs(calculation)
        result = inputArgs.run_calc(3)
    except:
        result = "Error"

    calculation = str(result)
    text_result.insert(1.0, result)

def clear_list():
    print("Clearing input...")
    text_result.delete(1.0, "end")
    global calculation
    calculation = ""

def key_click(event):
    append_char(event.char)

def enter_click(event):
    export_list()

def backspace_click(event):
    remove_char()

def numpad_enter_click(event):
    export_list()

root = tk.Tk()
root.geometry("655x515")
root.resizable(False, False)
root.title("Klidecek Calculator")

text_result = tk.Text(root, height=3, width=36, bg="white", font=("Arial", 24))
text_result.grid(columnspan=6, pady=0, padx=0)
root.bind("<Return>", enter_click)
root.bind("<Key>", key_click)
root.bind("<BackSpace>", backspace_click)
root.bind("<KP_Enter>", numpad_enter_click)

button_1 = tk.Button(root, text="1", command=lambda: append_char("1"), bg=DARKBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE,))
button_1.grid(row=5, column=1)

button_2 = tk.Button(root, text="2", command=lambda: append_char("2"), bg=DARKBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_2.grid(row=5, column=2)

button_3 = tk.Button(root, text="3", command=lambda: append_char("3"), bg=DARKBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_3.grid(row=5, column=3)

button_4 = tk.Button(root, text="4", command=lambda: append_char("4"), bg=DARKBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_4.grid(row=4, column=1)

button_5 = tk.Button(root, text="5", command=lambda: append_char("5"), bg=DARKBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_5.grid(row=4, column=2)

button_6 = tk.Button(root, text="6", command=lambda: append_char("6"), bg=DARKBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_6.grid(row=4, column=3)

button_7 = tk.Button(root, text="7", command=lambda: append_char("7"), bg=DARKBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_7.grid(row=3, column=1)

button_8 = tk.Button(root, text="8", command=lambda: append_char("8"), bg=DARKBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_8.grid(row=3, column=2)

button_9 = tk.Button(root, text="9", command=lambda: append_char("9"), bg=DARKBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_9.grid(row=3, column=3)

button_0 = tk.Button(root, text="0", command=lambda: append_char("0"), bg=DARKBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_0.grid(row=6, column=2)

button_plus = tk.Button(root, text="+", command=lambda: append_char("+"), bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_plus.grid(row=5, column=4)

button_minus = tk.Button(root, text="-", command=lambda: append_char("-"), bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_minus.grid(row=4, column=4)

button_mul = tk.Button(root, text="*", command=lambda: append_char("*"), bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_mul.grid(row=3, column=4)

button_div = tk.Button(root, text="/", command=lambda: append_char("/"), bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_div.grid(row=2, column=4)

button_left_par = tk.Button(root, text="(", command=lambda: append_char("("), bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_left_par.grid(row=2, column=1)

button_right_par = tk.Button(root, text=")", command=lambda: append_char(")"), bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_right_par.grid(row=2, column=2)

button_comma = tk.Button(root, text=",", command=lambda: append_char("."), bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_comma.grid(row=6, column=3)

button_sqrt = tk.Button(root, text="√", command=lambda: append_char("√"), bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_sqrt.grid(row=4, column=5)

button_exp = tk.Button(root, text="^", command=lambda: append_char("^"), bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_exp.grid(row=5, column=5)

button_fact = tk.Button(root, text="!", command=lambda: append_char("!"), bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_fact.grid(row=2, column=3)

button_mod = tk.Button(root, text="%", command=lambda: append_char("%"), bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_mod.grid(row=3, column=5)

button_all_clear = tk.Button(root, text="AC", command=clear_list, bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_all_clear.grid(row=2, column=5)

button_delete = tk.Button(root, text="C", command=remove_char, bg=LIGHTBLUE, fg="white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_delete.grid(row=6, column=1)

button_equals = tk.Button(root, text="=", command=export_list, bg=DARKBLUE, fg="white", width=15, height=BUTTON_HEIGHT, font=("Arial", BUTTON_TEXT_SIZE))
button_equals.grid(row=6, column=4, columnspan=2)

root.mainloop()
