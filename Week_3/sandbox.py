from tkinter import *
from all_classes import *
from tkinter.ttk import Combobox, Notebook
import matplotlib.pyplot as plt
# from matplotlib.patches import *
import numpy as np



class_dict = {'Круг': Disk,
              'Квадрат': Square,
              'Прямоугольник': Rectangle,
              'Треугольник': Triangle,
              'Трапеция': Trapezoid,
              'Ромб': Rhombus
              }


window = Tk()

max_entry_fields = 4
entry_instruction_lbls = []
input_ents = []
for n in range(1, max_entry_fields+1):
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
        # a = float(input_1.get())
        # b = float(input_2.get())

    Figure = FigureType(parameters)
    final_lbl_1 = Label(window, text=Figure.border_lebesgue_measure())
    final_lbl_1.grid(column=3, row=3)
    final_lbl_2 = Label(window, text=Figure.lebesgue_measure())
    # final_lbl_2 = Label(window, text=figure.area)
    final_lbl_2.grid(column=3, row=4)
    final_lbl_3 = Label(window, text=Figure.title)
    final_lbl_3.grid(column=3, row=5)
    points = ((40, 110), (160, 110), (190, 180), (10, 180))
    cnv.create_polygon(points)

window.title('Добро пожаловать в приложение "Геометрический калькулятор"!')

class_names = ('Круг', 'Квадрат', 'Прямоугольник', 'Треугольник', 'Трапеция', 'Ромб')

combo = Combobox(window)
combo['values'] = tuple(class_dict.keys())
combo.current(0)  # установите вариант по умолчанию

combo.grid(column=0, row=0)

lbl = Label(window, text='Выбранная фигура: ')
lbl.grid(column=2, row=-0)

btn = Button(window, text="Подтвердить", command=choose_mode)
btn.grid(column=1, row=0)

cnv = Canvas(window, width=400, height=400, bg='white')
cnv.grid(column=3, row=1)



# задание размеров окна
H = 1200
W = 675
window.geometry(f'{H}x{W}')


















# window.mainloop()

X = [1, 5, 1, 5]
Y = [1, 1, 5, 5]


#
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
#
# points = np.array([[1, 3],
#           [3, 1],
#           [1, 3],
#           [3, 3]])
# print(points.shape)
# points = [[0.1, 0.3],
#           [0.3, 0.1],
#           [0.1, 0.3],
#           [0.3, 0.3]]
#
# rect = Rectangle((-1, -1), 2.5, 3.5)
#
# # fig = plt.figure()
#
# poly = Polygon(xy=points, facecolor='g')
#
# ax.set(xlim=(-3, 3), ylim=(-3, 3))
# ax.add_patch(poly)
#
#
# print(type(fig))
#
# # plt.show()







points = [[-1, -1],
          [-1, 1],
          [1, 1],
          [1, -1]]

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid()
axes = plt.gca()
axes.set_aspect("equal")

print(type(axes))
poly = plt.Polygon(xy=points, fill=False, closed=True)
axes.add_patch(poly)
plt.show()