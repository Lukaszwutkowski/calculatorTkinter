#!/usr/bin/env python3

# Author: LW
# Email: lwutkowski@student.wsb-nlu.edu.pl
# Version: 1.0 beta
# Title: Calculator

import tkinter as tk

def add_digit(digit):
    """
    Adds a digit or an operator to the display field.
    """
    current_text = display_field.get()
    display_field.delete(0, tk.END)
    display_field.insert(0, current_text + digit)

def calculate():
    """
    Calculates the expression entered in the display field using eval.
    Adds basic error handling for common errors.
    """
    expression = display_field.get()
    try:
        result = eval(expression)
        display_field.delete(0, tk.END)
        display_field.insert(0, str(result))
    except Exception as e:
        display_field.delete(0, tk.END)
        display_field.insert(0, "Error")

def clear():
    """
    Clears the display field.
    """
    display_field.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

display_field = tk.Entry(root, width=35, borderwidth=5)
display_field.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Buttons layout improvement
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1), ('+', 4, 0), ('-', 4, 2),
    ('*', 5, 0), ('/', 5, 1), ('=', 5, 2), ('C', 5, 3),
]

for text, row, col in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, command=calculate).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, command=lambda text=text: add_digit(text)).grid(row=row, column=col)

root.mainloop()
