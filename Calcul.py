import tkinter as tk
from tkinter import ttk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, "end")
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1*num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1/num2
    insert_values(res)






window = tk.Tk()
window.title('Calculator')
window.geometry("350x350")
window.resizable(False, False)
button_add = ttk.Button(window, text="+", width=4, command=add, padding=8)
button_add.place(x=100, y=200)
button_sub = ttk.Button(window, text="-", width=4, command=sub, padding=8)
button_sub.place(x=150, y=200)
button_mul = ttk.Button(window, text="*", width=4, command=mul, padding=8)
button_mul.place(x=200, y=200)
button_div = ttk.Button(window, text="/", width=4, command=div, padding=8)
button_div.place(x=250, y=200)
number1_entry = ttk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number2_entry = ttk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = ttk.Entry(window, width=28)
answer_entry.place(x=100, y=290)
number1 = ttk.Label(window, text="Введите первое число:", font="Verdana 11 normal roman")
number1.place(x=115, y=50)
number2 = ttk.Label(window, text="Введите второе число:", font="Verdana 11 normal roman")
number2.place(x=115, y=125)
answer = ttk.Label(window, text="Ваш ответ:", font="Verdana 11 normal roman")
answer.place(x=150, y=265)
window.mainloop()