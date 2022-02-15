from tkinter import *
from all_classes import *
from tkinter.ttk import Combobox
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

def find_size(points):
    x_max = -float('inf')
    y_max = -float('inf')
    x_min = float('inf')
    y_min = float('inf')
    for x, y in points:
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
        if x < x_min:
            x_min = x
        if y < y_min:
            y_min = y

    result = max(abs(x_max-x_min), abs(y_max-y_min))
    return result

def find_center(points):
    x_sum=0
    y_sum=0
    for x,y in points:
        x_sum += x
        y_sum += y
    center = (x_sum/len(points), y_sum/len(points))
    return center

def find_center_3D(points):
    x_sum=0
    y_sum=0
    z_sum=0
    for x,y,z in points:
        x_sum += x
        y_sum += y
        z_sum += z
    center = (x_sum/len(points), y_sum/len(points), z_sum/len(points))
    return center

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
    result_lm_lbl = Label(window, text=f'{Figure.border_lebesgue_measure_name}:', height=2, width=25, font='Arial 18')
    result_lm_lbl.grid(column=0, row=6)

    final_lbl_2 = Label(window, text=Figure.lebesgue_measure(), height=2, width=10, font='Arial 18')
    final_lbl_2.grid(column=1, row=7)
    result_blm_lbl = Label(window, text=f'{Figure.lebesgue_measure_name}:', height=2, width=25, font='Arial 18')
    result_blm_lbl.grid(column=0, row=7)

    final_lbl_3 = Label(window, text=Figure.title, height=2, width=10, font='Arial 18')
    final_lbl_3.grid(column=1, row=8)
    result_cls_lbl = Label(window, text='Класс фигуры: ', height=2, width=25, font='Arial 18')
    result_cls_lbl.grid(column=0, row=8)

    fig = plt.figure(figsize=(3,3))
    if Figure.is_plan:
        axes = fig.add_subplot(111)
        plt.grid()
        axes = plt.gca()
        axes.set_aspect("equal")

        if Figure.is_circle:
            border = 1.2
            plt.xlim(-points*border, points*border)
            plt.ylim(-points*border, points*border)
            poly = plt.Circle((0,0), radius=points, fill=False, color='green', lw=3)
        else:
            x0, y0 = find_center(points)
            size = find_size(points)
            plt.xlim(x0 - size, x0 + size)
            plt.ylim(y0 - size, y0 + size)
            poly = plt.Polygon(xy=points, fill=False, closed=True, color='green', lw=3)
        axes.add_patch(poly)
    else:
        axes = fig.add_subplot(111, projection="3d")

        if Figure.is_polyhedron:

            x0, y0, z0 = find_center_3D(points)
            size = max(parameters)

            axes.set_xlim(x0 - size, x0 + size)
            axes.set_ylim(y0 - size, y0 + size)
            axes.set_zlim(z0 - size, z0 + size)

            hull = ConvexHull(list(points))
            for s in hull.simplices:

                face = Poly3DCollection(points[s])
                face.set_color('g')
                face.set_alpha(0.5)
                axes.add_collection3d(face)
        else:
            dphi = 360
            if Figure.is_ball:
                r = points[0]

                u = np.linspace(0, 2 * pi, dphi)
                v = np.linspace(0, pi, dphi//2)

                x = r * np.outer(np.cos(u), np.sin(v))
                y = r * np.outer(np.sin(u), np.sin(v))
                z = r * np.outer(np.ones(np.size(u)), np.cos(v))

            else:
                dl = 100

                h = points[1]
                r = points[0]

                u = np.linspace(0, 2 * pi, dphi)
                dh = np.linspace(0, 1, dl)
                x = np.outer(np.sin(u), np.ones(len(dh)))
                y = np.outer(np.cos(u), np.ones(len(dh)))

                if FigureType == RightCylinder:
                    x = r * np.outer(np.sin(u), np.ones(len(dh)))
                    y = r * np.outer(np.cos(u), np.ones(len(dh)))
                    z = h * np.outer(np.ones(len(u)), dh)
                else:
                    x = r * np.outer(np.sin(u), dh)
                    y = r * np.outer(np.cos(u), dh)
                    z = h * np.outer(np.ones(len(u)), dh)
            axes.plot_surface(x, y, z, color='g')



    canvas1 = FigureCanvasTkAgg(fig, master=window)
    canvas1.get_tk_widget().grid(column=3, row=0, rowspan=9)




window.title('Добро пожаловать в приложение "Геометрический калькулятор на костылях"!')

class_names = ('Круг', 'Квадрат', 'Прямоугольник', 'Треугольник', 'Трапеция', 'Ромб')

combo = Combobox(window, height=2, width=25, font='Arial 18')
combo['values'] = tuple(class_dict.keys())
combo.current(0)

combo.grid(column=0, row=0)

lbl = Label(window, text='Выбранная фигура: ', height=4, width=25, font='Arial 18')
lbl.grid(column=0, row=5)

btn = Button(window, text="Выбрать\nфигуру", command=choose_mode, font='Arial 18')
btn.grid(column=1, row=0)


# задание размеров окна
# H = 1200
# W = 675
# window.geometry(f'{H}x{W}')

window.mainloop()
