from tkinter.constants import END
from tkinter.messagebox import showerror


def click(number, entry):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def addiction(calculator, entry):
    calculator.sum = True
    calculator.first_number = entry.get()
    entry.delete(0, END)


def subtraction(calculator, entry):
    calculator.subtraction = True
    calculator.first_number = entry.get()
    entry.delete(0, END)


def multiplication(calculator, entry):
    calculator.multiplication = True
    calculator.first_number = entry.get()
    entry.delete(0, END)


def division(calculator, entry):
    calculator.division = True
    calculator.first_number = entry.get()
    entry.delete(0, END)


def show(calculator, entry):
    if not check_empty(entry.get()):
        calculator.second_number = entry.get()
        entry.delete(0, END)

        calculator.first_number = float(calculator.first_number)
        calculator.second_number = float(calculator.second_number)

        check_operations(calculator, entry)


def delete_last(entry):
    entry.delete(0, END)


def check_operations(calculator, entry):
    if calculator.sum:
        temp_sum = calculator.first_number + calculator.second_number
        entry.insert(0, str(temp_sum))
        calculator.sum = False

    elif calculator.subtraction:
        temp_subtraction = calculator.first_number - calculator.second_number
        entry.insert(0, temp_subtraction)
        calculator.subtraction = False

    elif calculator.multiplication:
        temp_molt = calculator.first_number * calculator.second_number
        entry.insert(0, temp_molt)
        calculator.multiplication = False

    elif calculator.division:
        temp_division = calculator.first_number / calculator.second_number
        entry.insert(0, temp_division)
        calculator.division = False


def check_empty(string):
    if not len(string):
        showerror(title='Operation Error', message='U should do same operation :)')
        return True

    else:
        return False
