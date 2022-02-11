from tkinter import *
from tkinter.ttk import Combobox, Notebook

def clicked():
    # lbl.configure(text="Кнопка нажата", fg="red")
    res = f"Считано {input_txt.get()} и {combo.get()}"
    lbl.configure(text=res, fg="green")
    input_txt.configure(width=5, state='disabled')

window = Tk()
window.title("Добро пожаловать в приложение!")

tab_control = Notebook(window)

tab_names = tuple(['Первая', 'Вторая', 'Третья', 'Четвёртая'])
tabs = []

for i, tab_name in enumerate(tab_names):
    tab = Frame(tab_control)
    tabs.append(tab)
    tab_control.add(tabs[i], text=tab_name)

tab_control.pack(expand=1, fill='both')

# задание размеров окна
H = 400
W = 250
window.geometry(f'{H}x{W}')

# добавление надписей
x = 0
y = 0
lbl = Label(window, text=f'({x}, {y})', font=("Arial Bold", 14))
lbl.grid(column=x, row=y)

x = 125
y = 25
lbl2 = Label(window, text=f'({x}, {y})', padx=x, pady=y, font=("Arial Bold", 14))
lbl2.grid(column=x, row=y)

# добавление кнопок
x = 1
y = 0
btn = Button(tabs[0], text="Кнопка", command=clicked)
btn.grid(column=x, row=y)

# # создание поля ввода
# input_txt = Entry(window, width=10)
# x = 2
# y = 0
# input_txt.grid(column=x, row=y)
#
#
# # добавление выпадающего списка
# combo = Combobox(window)
# combo['values'] = (1, 2, 3, 4, 5)
# combo.current(0)  # установите вариант по умолчанию
# x = 0
# y = 1
# combo.grid(column=x, row=y)
#
# # добавление списка с флажками
window.mainloop()
