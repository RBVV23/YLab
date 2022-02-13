from tkinter import *
from all_classes import *
from tkinter.ttk import Combobox, Notebook

# def clicked():
#     # lbl.configure(text="Кнопка нажата", fg="red")
#     # i = btns.index(btn)
#     i = 0
#     res = f"Считано {input_txts[i].get()}, {j} и {combos[i].get()}"
#     lbls[i].configure(text=res, fg="green")
#     input_txts[i].configure(width=5, state='disabled')

window = Tk()

lbl_1 = Label(window, text=f'Поле ввода параметра #{1}: ')
lbl_1.grid(column=0, row=1)
input_1 = Entry(window, width=10, state='disabled')
input_1.grid(column=1, row=1)

lbl_2 = Label(window, text=f'Поле ввода параметра #{2}:  ')
lbl_2.grid(column=0, row=2)
input_2 = Entry(window, width=10, state='disabled')
input_2.grid(column=1, row=2)

lbl_3 = Label(window, text=f'Поле ввода параметра #{3}:  ')
lbl_3.grid(column=0, row=3)
input_3 = Entry(window, width=10, state='disabled')
input_3.grid(column=1, row=3)

lbl_4 = Label(window, text=f'Поле ввода параметра #{4}:  ')
lbl_4.grid(column=0, row=4)
input_4 = Entry(window, width=10, state='disabled')
input_4.grid(column=1, row=4)

def choose_mode():
    text = combo.get()
    text = f'Выбранная фигура: {combo.get()}'
    lbl.configure(text=text)
    if combo.get() == combo['values'][0]:
        lbl_1 = Label(window, text=f'Введите радиус r: ')
        lbl_1.grid(column=0, row=1)
        # input_1 = Entry(window, width=10)
        # input_1.grid(column=1, row=1)
        lbl.configure(text=text, fg='green')
        btn_2 = Button(window, text="Подтвердить")
        btn_2.grid(column=1, row=2)

    if combo.get() == combo['values'][1]:
        lbl_1 = Label(window, text=f'Введите сторону a: ')
        lbl_1.grid(column=0, row=1)
        # input_1 = Entry(window, width=10)
        # input_1.grid(column=1, row=1)
        lbl.configure(text=text, fg='green')
        btn_2 = Button(window, text="Подтвердить")
        btn_2.grid(column=1, row=2)

    if combo.get() == combo['values'][2]:
        lbl_1.configure(text=f'Введите сторону a: ')
        input_1.configure(state='normal')
        # input_1 = Entry(window, width=10)
        # input_1.grid(column=1, row=1)
        # lbl_2.configure(window, text=f'Введите сторону b: ')
        # lbl_2.grid(column=0, row=2)
        input_2.configure(state='normal')
        # input_2 = Entry(window, width=10)
        # input_2.grid(column=1, row=2)
        lbl.configure(text=text, fg='green')
        btn_2 = Button(window, text="Подтвердить", command=choose_parameters)
        btn_2.grid(column=2, row=3)


def choose_parameters():
    lbl.configure(fg='black')
    a = float(input_1.get())
    b = float(input_2.get())
    figure = Rectangle(a,b)
    final_lbl_1 = Label(window, text=figure.perimeter)
    final_lbl_1.grid(column=3, row=1)
    final_lbl_2 = Label(window, text=figure.lebesgue_measure())
    # final_lbl_2 = Label(window, text=figure.area)
    final_lbl_2.grid(column=3, row=2)


window.title('Добро пожаловать в приложение "Геометрический калькулятор"!')
combo = Combobox(window)
combo['values'] = ('Круг', 'Квадрат', 'Прямоугольник', 'Треугольник', 'Трапеция', 'Ромб')
combo.current(0)  # установите вариант по умолчанию

combo.grid(column=0, row=0)

lbl = Label(window, text='Выбранная фигура: ')
lbl.grid(column=2, row=-0)

btn = Button(window, text="Подтвердить", command=choose_mode)
btn.grid(column=1, row=0)



# задание размеров окна
H = 1200
W = 675
window.geometry(f'{H}x{W}')




















window.mainloop()

# print(f'a = {a}, b = {b}')
# добавление надписей
# x = 0
# y = 0
# lbl = Label(tabs[0], text=f'({x}, {y})', font=("Arial Bold", 14))
# lbl.grid(column=x, row=y)
#
# x = 125
# y = 25
# lbl2 = Label(tabs[0], text=f'({x}, {y})', padx=x, pady=y, font=("Arial Bold", 14))
# lbl2.grid(column=x, row=y)
#
# # добавление кнопок
# x = 1
# y = 0
# btn = Button(tabs[0], text="Кнопка", command=clicked)
# btn.grid(column=x, row=y)

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




# figure = RightCone(3, 4)
# print(f'\nfigure = RightCone(3, 10)')
# figure.info()