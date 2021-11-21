import tkinter as tk

from calculator import Calculator
from commands import *


def gui():
    calculator = Calculator(0, 0, False, False, False, False)

    window = tk.Tk()
    window.resizable(width=False, height=False)

    entry = tk.Entry(window, width=40, font=("Arial", 10))
    entry.grid(row=0, column=0, columnspan=3)

    tk.Button(window,
              text="7",
              bg="#932aa3",
              fg="#ffffff",
              activebackground="#932aa3",
              padx=41,
              pady=25,
              command=lambda: click(7, entry)).grid(row=1, column=0)

    tk.Button(window,
              text="8",
              bg="#932aa3",
              fg="#ffffff",
              activebackground="#932aa3",
              padx=41,
              pady=25,
              command=lambda: click(8, entry)).grid(row=1, column=1)

    tk.Button(window,
              text="9",
              bg="#932aa3",
              fg="#ffffff",
              activebackground="#932aa3",
              padx=41,
              pady=25,
              command=lambda: click(9, entry)).grid(row=1, column=2)

    tk.Button(window,
              text="-",
              bg="#932aa3",
              fg="#ffffff",
              activebackground="#932aa3",
              padx=50,
              pady=25,
              command=lambda: subtraction(calculator, entry)).grid(row=1, column=4)

    tk.Button(window,
              text="4",
              bg="#932aa3",
              fg="#ffffff",
              padx=41,
              activebackground="#932aa3",
              pady=25,
              command=lambda: click(4, entry)).grid(row=2, column=0)

    tk.Button(window,
              text="5",
              bg="#932aa3",
              fg="#ffffff",
              padx=41,
              activebackground="#932aa3",
              pady=25,
              command=lambda: click(5, entry)).grid(row=2, column=1)

    tk.Button(window,
              text="6",
              bg="#932aa3",
              fg="#ffffff",
              padx=41,
              activebackground="#932aa3",
              pady=25,
              command=lambda: click(6, entry)).grid(row=2, column=2)

    tk.Button(window,
              text="*",
              bg="#932aa3",
              fg="#ffffff",
              activebackground="#932aa3",
              padx=50,
              pady=25,
              command=lambda: multiplication(calculator, entry)).grid(row=2, column=4)

    tk.Button(window,
              text="1",
              bg="#932aa3",
              fg="#ffffff",
              padx=41,
              activebackground="#932aa3",
              pady=25,
              command=lambda: click(1, entry)).grid(row=3, column=0)

    tk.Button(window,
              text="2",
              bg="#932aa3",
              fg="#ffffff",
              padx=41,
              activebackground="#932aa3",
              pady=25,
              command=lambda: click(2, entry)).grid(row=3, column=1)

    tk.Button(window,
              text="3",
              bg="#932aa3",
              fg="#ffffff",
              padx=41,
              activebackground="#932aa3",
              pady=25,
              command=lambda: click(3, entry)).grid(row=3, column=2)

    tk.Button(window,
              text="/",
              bg="#932aa3",
              fg="#ffffff",
              padx=50,
              activebackground="#932aa3",
              pady=25,
              command=lambda: division(calculator, entry)).grid(row=3, column=4)

    tk.Button(window,
              text="0",
              bg="#932aa3",
              fg="#ffffff",
              padx=41,
              activebackground="#932aa3",
              pady=25,
              command=lambda: click(0, entry)).grid(row=4, column=1)

    tk.Button(window,
              text="+",
              bg="#932aa3",
              fg="#ffffff",
              padx=41,
              activebackground="#932aa3",
              pady=25,
              command=lambda: addiction(calculator, entry)).grid(row=4, column=0)

    tk.Button(window,
              text="=",
              bg="#932aa3",
              fg="#ffffff",
              padx=41,
              activebackground="#932aa3",
              pady=25,
              command=lambda: show(calculator, entry)).grid(row=4, column=2)

    tk.Button(window,
              text="CE",
              bg="#932aa3",
              fg="#ffffff",
              padx=46,
              activebackground="#932aa3",
              pady=25,
              command=lambda: delete_last(entry)).grid(row=4, column=4)

    window.mainloop()
