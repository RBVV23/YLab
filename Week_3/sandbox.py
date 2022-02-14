from tkinter import *
from all_classes import *
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull



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
    text = f'Выбранная фигура: {FigureType.title}'
    lbl.configure(text=text)


    for n, instruction in enumerate(FigureType.input_instructions):
        entry_instruction_lbls[n].configure(text=instruction)
        input_ents[n].configure(state='normal')
    lbl.configure(text=text, fg='green')
    btn_2 = Button(window, text="Подтвердить\nпараметры", font='Arial 18',
                   command=lambda: choose_parameters(FigureType))
    btn_2.grid(column=1, row=5)




def choose_parameters(FigureType):
    lbl.configure(fg='black')
    parameters = []
    for n, instruction in enumerate(FigureType.input_instructions):
        parameter = float(input_ents[n].get())
        parameters.append(parameter)

    Figure = FigureType(parameters)
    points = Figure.building()
    final_lbl_1 = Label(window, text=Figure.border_lebesgue_measure(), height=2, width=10, font='Arial 18')
    final_lbl_1.grid(column=1, row=6)
    result_lm_lbl = Label(window, text=Figure.lebesgue_measure_name, height=2, width=25, font='Arial 18')
    result_lm_lbl.grid(column=0, row=6)
    final_lbl_2 = Label(window, text=Figure.lebesgue_measure(), height=2, width=10, font='Arial 18')
    result_blm_lbl = Label(window, text=Figure.border_lebesgue_measure_name, height=2, width=25, font='Arial 18')
    result_blm_lbl.grid(column=0, row=7)
    final_lbl_2.grid(column=1, row=7)
    final_lbl_3 = Label(window, text=Figure.title, height=2, width=10, font='Arial 18')
    final_lbl_3.grid(column=1, row=8)
    result_cls_lbl = Label(window, text='Класс фигуры: ', height=2, width=25, font='Arial 18')
    result_cls_lbl.grid(column=0, row=8)

    fig = plt.figure(figsize=(3,3))
    if Figure.is_plan:
        axes = fig.add_subplot(111)
        plt.xlim(-5, 10)
        plt.ylim(-5, 10)
        plt.grid()
        axes = plt.gca()
        axes.set_aspect("equal")

        if Figure.is_circle:
            poly = plt.Circle((0,0), radius=points, fill=False, color='green', lw=3)
        else:
            poly = plt.Polygon(xy=points, fill=False, closed=True, color='green', lw=3)
        axes.add_patch(poly)
    else:
        axes = fig.add_subplot(111, projection="3d")

        hull = ConvexHull(list(points))
        for s in hull.simplices:
            face = Poly3DCollection(points[s])
            face.set_color('g')
            face.set_alpha(0.5)
            axes.add_collection3d(face)


    canvas1 = FigureCanvasTkAgg(fig, master=window)
    # canvas1.draw()
    canvas1.get_tk_widget().grid(column=3, row=0, rowspan=9)
    # canvas1.show()

    # canvas1.get_tk_widget().pack(side=TOP, fill=NONE, expand=0)



window.title('Добро пожаловать в приложение "Геометрический калькулятор"!')

class_names = ('Круг', 'Квадрат', 'Прямоугольник', 'Треугольник', 'Трапеция', 'Ромб')

combo = Combobox(window, height=2, width=25, font='Arial 18')
combo['values'] = tuple(class_dict.keys())
combo.current(0)  # установите вариант по умолчанию

combo.grid(column=0, row=0)

lbl = Label(window, text='Выбранная фигура: ', height=4, width=25, font='Arial 18')
lbl.grid(column=0, row=5)

btn = Button(window, text="Выбрать\nфигуру", command=choose_mode, font='Arial 18')
btn.grid(column=1, row=0)

# cnv = Canvas(window, width=400, height=400, bg='white')
# cnv.grid(column=3, row=1)



# задание размеров окна
# H = 1200
# W = 675
# window.geometry(f'{H}x{W}')















window.mainloop()



# mA = [[0,0,0], [1,0,0], [0,1,0], [1,1,0], [0.5,0.5,1]]
A = np.array([[0,0,0], [1,0,0], [0,1,0], [1,1,0], [0.5,0.5,1]])


figure = Cube([0.5])
print(figure.building())
A=figure.building()

fig = plt.figure(figsize=(3,3))
axes = fig.add_subplot(111, projection="3d")

hull = ConvexHull(list(A))
for s in hull.simplices:
    face = Poly3DCollection(A[s])
    face.set_color('g')
    face.set_alpha(0.5)
    axes.add_collection3d(face)

# hull = ConvexHull(mA)
# for s in hull.simplices:
#     tri = Poly3DCollection(mA[s])
#     tri.set_color(color)
#     tri.set_alpha(0.5)
#     axes.add_collection3d(tri)
# plt.show()

