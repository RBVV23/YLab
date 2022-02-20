from tkinter import *
from all_classes import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class_dict = {'Круг': Disk,
              'Квадрат': Square,
              'Прямоугольник': Rectangle,
              'Треугольник': Triangle,
              'Трапеция': Trapezoid,
              'Ромб': Rhombus,
              'Куб': Cube,
              'Кубоид': Cuboid,
              'Правильный тетраэдр': RightTetrahedron,
              'Правильный конус': RightCone,
              'Правильный цилиндр': RightCylinder,
              'Шар': Ball
              }

window = Tk()

max_entry_fields = 4
entry_instruction_lbls = []
input_ents = []

for n in range(1, max_entry_fields+1):
    lbl = Label(window, text=f'Поле ввода параметра #{n}: ', height=2, width=25, font='Arial 18')
    lbl.grid(column=0, row=n)
    entry_instruction_lbls.append(lbl)

    ent = Entry(window, width=5, state='disabled', font='Arial 18')
    ent.grid(column=1, row=n)
    input_ents.append(ent)


def choose_mode():
    FigureType = class_dict[combo.get()]
    text = f'Текущий класс: {FigureType.title}'
    lbl.configure(text=text)


    for n, instruction in enumerate(FigureType.input_instructions):
        entry_instruction_lbls[n].configure(text=instruction)
        input_ents[n].configure(state='normal')
    lbl.configure(text=text, fg='green')
    btn_2 = Button(window, text="Подтвердить\nпараметры", font='Arial 18',
                   command=lambda: check_inputs(FigureType))
    btn_2.grid(column=1, row=5)


def check_inputs(FigureType):
    flag = True
    for n, instruction in enumerate(FigureType.input_instructions):
        if float(input_ents[n].get()) <= 0:
            messagebox.showinfo('Некорректный ввод', 'Введите положительное число!')
            input_ents[n].delete(0, END)
            input_ents[n].focus()
            flag = False
    if flag:
        choose_parameters(FigureType)
    else:
        choose_mode()


def choose_parameters(FigureType):
    lbl.configure(fg='black')
    parameters = []
    for n, instruction in enumerate(FigureType.input_instructions):
        parameter = float(input_ents[n].get())
        parameters.append(parameter)
    Figure = FigureType(parameters)
    show_results(Figure)


def show_results(Figure):

    name_result_lbl_1 = Label(window, text=f'{Figure.border_lebesgue_measure_name}:', height=2, width=25,
                              font='Arial 18')
    name_result_lbl_1.grid(column=0, row=6)
    result_lbl_1 = Label(window, text=Figure.border_lebesgue_measure(), height=2, width=10, font='Arial 18')
    result_lbl_1.grid(column=1, row=6)

    name_result_lbl_2 = Label(window, text=f'{Figure.lebesgue_measure_name}:', height=2, width=25, font='Arial 18')
    name_result_lbl_2.grid(column=0, row=7)
    result_lbl_2 = Label(window, text=Figure.lebesgue_measure(), height=2, width=10, font='Arial 18')
    result_lbl_2.grid(column=1, row=7)


    fig = Builder(Figure)
    fig.to_draw()

    result_screen = FigureCanvasTkAgg(fig.drawing, master=window)
    result_screen.get_tk_widget().grid(column=3, row=0, rowspan=9, columnspan=9)




window.title('Добро пожаловать в приложение "Геометрический калькулятор на костылях"!')

font = ("Arial", 18, "normal")
combo = Combobox(window,
                 values=tuple(class_dict.keys()),
                 height=2,
                 width=25,
                 font=font)

window.option_add('*TCombobox*Listbox.font', font)
combo.current(0)

combo.grid(column=0, row=0)

figure_type_lbl = Label(window, text='Выбранная фигура: ', height=4, width=25, font='Arial 18')
figure_type_lbl.grid(column=0, row=5)

choose_figure_btn = Button(window, text="Выбрать\nфигуру", command=choose_mode, font='Arial 18')
choose_figure_btn.grid(column=1, row=0)

window.mainloop()

