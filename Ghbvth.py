import tkinter as tk

def add():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 + num2
    answer_entry.delete(0, "end")
    answer_entry.insert(0, res)









window = tk.Tk()
window.title('Calculator')
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=4, height=2, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text="-", width=4, height=2)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="*", width=4, height=2)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text="/", width=4, height=2)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=290)
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=115, y=50)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=115, y=125)
answer = tk.Label(window, text="Ваш ответ:")
answer.place(x=150, y=265)
window.mainloop()