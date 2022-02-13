from tkinter import *
from all_classes import *
from tkinter.ttk import Combobox, Notebook

class_dict = {
    'Круг': Disk,
    'Квадрат': Square,
    'Прямоугольник': Rectangle,
    'Треугольник': Triangle,
    'Трапеция': Trapezoid,
    'Ромб': Rhombus
}

window = Tk()

max_entry_fields = 4  # максимальное количество входных параметров
entry_instruction_lbls = []  # список меток (Label), поясняющих пользовательский ввод
input_ents = []  # список полей ввода пользователя (Entry)

for n in range(1, max_entry_fields + 1):
    lbl = Label(window, text=f'Поле ввода параметра #{n}: ')
    lbl.grid(column=0, row=n)
    entry_instruction_lbls.append(lbl)

    ent = Entry(window, width=10, state='disabled')
    ent.grid(column=1, row=n)
    input_ents.append(ent)


def choose_mode():
    FigureType = class_dict[combo.get()]
    text = f'Выбранная фигура: {FigureType.title}'
    lbl.configure(text=text)

    for n, instruction in enumerate(FigureType.input_instructions):
        entry_instruction_lbls[n].configure(text=instruction)
        input_ents[n].configure(state='normal')
    lbl.configure(text=text, fg='green')
    btn_2 = Button(window, text="Подтвердить", command=lambda: choose_parameters(FigureType))
    btn_2.grid(column=2, row=3)


def choose_parameters(FigureType):
    lbl.configure(fg='black')
    parameters = []
    for n, instruction in enumerate(FigureType.input_instructions):
        parameter = float(input_ents[n].get())
        parameters.append(parameter)

    Figure = FigureType(parameters)
    final_lbl_1 = Label(window, text=Figure.border_lebesgue_measure())
    final_lbl_1.grid(column=3, row=1)
    final_lbl_2 = Label(window, text=Figure.lebesgue_measure())
    final_lbl_2.grid(column=3, row=2)
    final_lbl_3 = Label(window, text=Figure.title)
    final_lbl_3.grid(column=3, row=3)


window.title('Добро пожаловать в приложение "Геометрический калькулятор"!')

class_names = ('Круг', 'Квадрат', 'Прямоугольник', 'Треугольник', 'Трапеция', 'Ромб')

combo = Combobox(window)
combo['values'] = tuple(class_dict.keys())
combo.current(0)

combo.grid(column=0, row=0)

lbl = Label(window, text='Выбранная фигура: ')
lbl.grid(column=2, row=-0)

btn = Button(window, text="Подтвердить", command=choose_mode)
btn.grid(column=1, row=0)

H = 1200
W = 675
window.geometry(f'{H}x{W}')
window.mainloop()
