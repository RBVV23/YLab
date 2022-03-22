from math import sin, pi, sqrt, cos
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Builder():
    def __init__(self, figure, height=6, width=6):
        self.drawing = plt.figure(figsize=(height, width))
        self.figure = figure
        self.reference = figure.get_for_drawing()

    def set_figure_size(self):
        if self.figure.is_solid_of_revolution:
            self.size = 2 * self.reference
        else:
            points = self.reference
            dim = points.shape[1]
            maxs = np.zeros(dim) - float('inf')
            mins = np.zeros(dim) + float('inf')
            for i in range(dim):
                for p in points:
                    if p[i] > maxs[i]:
                        maxs[i] = p[i]
                    if p[i] < mins[i]:
                        mins[i] = p[i]

            self.size = max(maxs - mins)

    def set_xy_limits(self):
        if self.figure.is_plan:
            plt.xlim(self.center[0] - self.size, self.center[0] + self.size)
            plt.ylim(self.center[1] - self.size, self.center[1] + self.size)
        else:
            self.axes.set_xlim(self.center[0] - self.size, self.center[0] + self.size)
            self.axes.set_ylim(self.center[1] - self.size, self.center[1] + self.size)
            self.axes.set_zlim(self.center[2] - self.size, self.center[2] + self.size)

    def set_center_point(self):
        if self.figure.is_solid_of_revolution:
            self.center = (0, 0)
        else:
            points = self.reference
            dim = points.shape[1]
            sums = np.zeros(dim)
            for i in range(dim):
                for p in points:
                    sums[i] += p[i]
                sums[i] /= points.shape[0]

            self.center = sums

    def to_draw(self):
        if self.figure.is_plan:
            axes = self.drawing.add_subplot(111)
            plt.grid()
            axes = plt.gca()
            axes.set_aspect("equal")
            self.set_center_point()
            self.set_figure_size()
            self.set_xy_limits()

            if self.figure.is_solid_of_revolution:
                poly = plt.Circle(self.center, radius=self.reference, fill=False, color='green', lw=3)
            else:

                poly = plt.Polygon(xy=self.reference, fill=False, closed=True, color='green', lw=3)
            axes.add_patch(poly)
        else:
            self.axes = self.drawing.add_subplot(111, projection="3d")

            if self.figure.is_polyhedron:
                self.set_center_point()
                self.set_figure_size()
                self.set_xy_limits()

                points = self.reference
                hull = ConvexHull(list(points))
                for s in hull.simplices:
                    face = Poly3DCollection(points[s])
                    face.set_color('g')
                    face.set_alpha(0.5)
                    self.axes.add_collection3d(face)
            else:
                x = self.reference[0]
                y = self.reference[1]
                z = self.reference[2]
                self.axes.plot_surface(x, y, z, color='g')


class Shape():
    title = 'Shape'
    precision = 3
    input_instructions = []
    is_solid_of_revolution = False
    dl = 100
    dphi = 360

    def __init__(self, parameters):
        self.a = parameters[0]

    # для плоских фигур мера Лебега - это площадь, а для объемных - объем
    # этот метод переопределяется и становится специфичным для каждого класса
    def lebesgue_measure(self):
        print('Метод "Shape.lebesgue_measure()"')

    # для плоских фигур мера Лебега границы - это периметр, а для объёмных - площадь поверхности
    # этот метод переопределяется и становится специфичным для каждого класса
    def border_lebesgue_measure(self):
        print('Метод "Shape.border_lebesgue_measure()"')

    def get_for_drawing(self):
        return None

    def point_counter(self):
        return len(self.get_for_drawing())

    @staticmethod
    def print_pi():
        print(f'Значения констант, используемые при расчётах:\n\t\t {None}')

    @classmethod
    def help(cls):
        print('Формат ввода данных:')
        for instr in cls.input_instructions:
            print(f'\t {instr[:-2]}')


class PlanShape(Shape):
    title = 'PlanShape'
    lebesgue_measure_name = 'Площадь'
    border_lebesgue_measure_name = 'Периметр'
    is_plan = True

    def __init__(self):
        self.area = self.lebesgue_measure()
        self.perimeter = self.border_lebesgue_measure()

    def lebesgue_measure(self):  # площадь фигуры на плоскости
        # self.area = -1
        print('Метод "PlanShape"')
        return -1

    def border_lebesgue_measure(self):  # периметр плоской на плоскости
        # self.perimeter = -1
        print('Метод "PlanShape"')
        return -1

    def info(self):
        print(f'TITLE: {self.title}')
        print(f'\tself.a = {self.a}')
        print(f'\tself.b = {self.b}')
        print(f'\tself.alpha = {self.alpha}')
        print(f'\tself.area = {self.area}')
        print(f'\tself.perimeter = {self.perimeter}')


class Rhombus(PlanShape):
    title = 'Rhombus'
    input_instructions = ['Введите сторону a: ',
                          'Введите угол \u03B1: ']

    def __init__(self, parameters):
        self.a = parameters[0]
        self.b = self.a
        self.alpha = parameters[1]
        self.betta = 180 - self.alpha
        super().__init__()

    def lebesgue_measure(self):
        return round(self.a*self.b*sin(pi*self.alpha/180), self.precision)

    def border_lebesgue_measure(self):
        return round(2*(self.a + self.b), self.precision)

    def get_for_drawing(self):
        A = (0, 0)
        B = (A[0] + self.a, 0)
        D = (A[0] + self.b*cos(pi*self.alpha/180), A[1] + self.b*sin(pi*self.alpha/180))
        C = (D[0] + self.a, D[1])
        return np.array([A, B, C, D])


class Square(PlanShape):
    title = 'Square'
    input_instructions = ['Введите сторону a: ']

    def __init__(self, parameters):
        self.a = parameters[0]
        self.b = self.a
        self.alpha = 90
        self.betta = 180 - self.alpha
        super().__init__()

    def lebesgue_measure(self):
        return round(self.a*self.a, self.precision)

    def border_lebesgue_measure(self):
        return round(4*self.a, self.precision)

    def get_for_drawing(self):
        A = (0, 0)
        B = (0, A[1] + self.a)
        C = (B[0] + self.a, B[1])
        D = (C[0], C[1] - self.a)
        return np.array([A, B, C, D])


class Rectangle(PlanShape):
    title = 'Rectangle'
    input_instructions = ['Введите сторону a: ',
                          'Введите сторону b: ']

    def __init__(self, parameters):
        self.a = parameters[0]
        self.b = parameters[1]
        self.alpha = 90
        self.betta = 180 - self.alpha
        super().__init__()

    def lebesgue_measure(self):
        return round(self.a*self.b, self.precision)

    def border_lebesgue_measure(self):
        return round(2*(self.a + self.b), self.precision)

    def get_for_drawing(self):
        A = (0, 0)
        B = (0, A[1] + self.b)
        C = (B[0] + self.a, B[1])
        D = (C[0], C[1] - self.b)
        return np.array([A, B, C, D])


class Disk(PlanShape):
    title = 'Disk'
    input_instructions = ['Введите радиус r: ']
    is_solid_of_revolution = True

    def __init__(self, parameters):
        self.r = parameters[0]
        super().__init__()

    def lebesgue_measure(self):
        return round(pi*self.r*self.r, self.precision)

    def border_lebesgue_measure(self):
        return round(2*pi*self.r, self.precision)

    def info(self):
        print(f'TITLE: {self.title}')
        print(f'\tself.r = {self.r}')
        print(f'\tself.area = {self.area}')
        print(f'\tself.perimeter = {self.perimeter}')

    def get_for_drawing(self):
        return np.array([self.r])

    @staticmethod
    def print_pi():
        print(f'Значения констант, используемые при расчётах:\n\t\t \u03C0 = {pi}')


class Triangle(PlanShape):
    title = 'Triangle'
    input_instructions = ['Введите сторону a: ',
                          'Введите сторону b: ',
                          'Введите угол \u03B1: ']
    def __init__(self, parameters):
        self.a = parameters[0]
        self.b = parameters[1]
        self.alpha = parameters[2]
        self.c = sqrt(self.a**2 + self.b**2 - 2*self.a*self.b*cos(pi*self.alpha/180))
        super().__init__()

    def lebesgue_measure(self):
        return round(0.5*self.a*self.b*sin(pi*self.alpha/180), self.precision)

    def border_lebesgue_measure(self):
        return round(self.a + self.b + self.c, self.precision)

    def info(self):
        super().info()
        # print(f'\tself.c = {self.c}')
        # print(f'\tself.gamma = {self.gamma}')

    def get_for_drawing(self):
        C = (0,0)
        B = (C[0] + self.a, C[1])
        A = (C[0] + self.b*cos(pi*self.alpha/180), C[1] + self.b*sin(pi*self.alpha/180))
        return np.array([A,B,C])


class Trapezoid(PlanShape):
    title = 'Trapezoid'
    input_instructions = ['Введите основание a: ',
                          'Введите основание b: ',
                          'Введите боковую сторону c: ',
                          'Введите острый угол \u03B1: ']
    def __init__(self, parameters):
        self.a = max(parameters[0],parameters[1])
        self.b = min(parameters[0],parameters[1])
        self.c = parameters[2]
        self.alpha = parameters[3]
        self.d = sqrt((self.c*sin(pi*self.alpha/180))**2 + (self.a - self.b - self.c*cos(pi*self.alpha/180))**2)
        self.betta = 180 - self.alpha
        super().__init__()

    def lebesgue_measure(self):
        h = self.c*sin(pi*self.alpha/180)
        return round(0.5*(self.a+self.b)*h, self.precision)

    def border_lebesgue_measure(self):
        return round(self.a + self.b + self.c + self.d, self.precision)

    def info(self):
        super().info()
        print(f'\tself.c = {self.c}')

    def get_for_drawing(self):
        A = (0,0)
        B = (A[0] + self.a, 0)
        D = (A[0] + self.c*cos(pi*self.alpha/180), A[1] + self.c*sin(pi*self.alpha/180))
        C = (D[0] + self.b, D[1])
        return np.array([A,B,C,D])


class StereoShape(Shape):
    title = 'StereoShape'
    lebesgue_measure_name = 'Объем'
    border_lebesgue_measure_name = 'Площадь боковой поверхности'
    is_plan = False
    is_polyhedron = True
    is_ball = False

    def __init__(self):
        self.volume = self.lebesgue_measure()
        self.surface_area = self.border_lebesgue_measure()

    def lebesgue_measure(self): # объем фигуры в пространстве
        print('Метод "StereoShape"')
        return -1

    def border_lebesgue_measure(self): #  площадь поверхности фигуры в пространстве
        print('Метод "StereoShape"')
        return -1

    def info(self):
        print(f'TITLE: {self.title}')
        print(f'\tself.a = {self.a}')
        print(f'\tself.b = {self.b}')
        print(f'\tself.h = {self.h}')
        print(f'\tself.volume = {self.volume}')
        print(f'\tself.surface_area = {self.surface_area}')


class Ball(StereoShape):
    title = 'Ball'
    input_instructions = ['Введите радиус r: ']
    is_polyhedron = False
    is_solid_of_revolution = True
    def __init__(self, parameters):
        self.r = parameters[0]
        super().__init__()


    def lebesgue_measure(self):
        return round(4*pi*self.r*self.r*self.r/3, self.precision)

    def border_lebesgue_measure(self):
        return round(4*pi*self.r*self.r, self.precision)

    def info(self):
        print(f'TITLE: {self.title}')
        print(f'\tself.r = {self.r}')
        print(f'\tself.volume = {self.volume}')
        print(f'\tself.surface_area = {self.surface_area}')

    def get_for_drawing(self):
        dphi = self.dphi
        r = self.r

        u = np.linspace(0, 2 * pi, dphi)
        v = np.linspace(0, pi, dphi // 2)

        x = r * np.outer(np.cos(u), np.sin(v))
        y = r * np.outer(np.sin(u), np.sin(v))
        z = r * np.outer(np.ones(np.size(u)), np.cos(v))
        return np.array([x, y, z])

    @staticmethod
    def print_pi():
        print(f'Значения констант, используемые при расчётах:\n\t\t \u03C0 = {pi}')


class Cube(StereoShape):
    title = 'Cube'
    input_instructions = ['Введите ребро a: ']
    def __init__(self, parameters):
        self.a = parameters[0]
        self.b = self.a
        self.h = self.a
        super().__init__()


    def lebesgue_measure(self):
        return round(self.a*self.a*self.a, self.precision)

    def border_lebesgue_measure(self):
        return round(6*self.a*self.a, self.precision)

    def get_for_drawing(self):
        A = np.array([0, 0, 0])
        B = np.array([self.a, 0, 0])
        C = np.array([0, self.a, 0])
        D = np.array([self.a, self.a, 0])

        A_1 = A + [0,0, self.a]
        B_1 = B + [0,0, self.a]
        C_1 = C + [0,0, self.a]
        D_1 = D + [0,0, self.a]
        return np.array([A,B,C,D, A_1,B_1,C_1,D_1])


class Cuboid(StereoShape):
    title = 'Cuboid'
    input_instructions = ['Введите ребро a: ',
                          'Введите ребро b: ',
                          'Введите ребро c: ']
    def __init__(self, parameters):
        self.a = parameters[0]
        self.b = parameters[1]
        self.h = parameters[2]
        super().__init__()

    def lebesgue_measure(self):
        return round(self.a*self.b*self.h, self.precision)

    def border_lebesgue_measure(self):
        return round(2*(self.a*self.b + self.b*self.h + self.a*self.h), self.precision)

    def get_for_drawing(self):
        A = np.array([0, 0, 0])
        B = np.array([self.a, 0, 0])
        C = np.array([0, self.b, 0])
        D = np.array([self.a, self.b, 0])

        A_1 = A + [0,0, self.h]
        B_1 = B + [0,0, self.h]
        C_1 = C + [0,0, self.h]
        D_1 = D + [0,0, self.h]
        return np.array([A,B,C,D, A_1,B_1,C_1,D_1])


class RightTetrahedron(StereoShape):
    title = 'Right tetrahedron'
    input_instructions = ['Введите ребро a: ']
    def __init__(self, parameters):
        self.a = parameters[0]
        self.b = self.a
        self.h = sqrt(2*self.a*self.a/3)
        self.alpha = 60
        super().__init__()

    def lebesgue_measure(self):
        S_base = 0.5*self.a*self.b*sin(pi*self.alpha/180)
        return round(S_base*self.h/3, self.precision)

    def border_lebesgue_measure(self):
        S_base = 0.5 * self.a * self.b * sin(pi * self.alpha / 180)
        return round(4*S_base, self.precision)

    def get_for_drawing(self):
        C = np.array([0, 0, 0])
        B = np.array([self.a, 0, 0])
        A = np.array([C[0]+self.a*cos(pi * self.alpha / 180), C[1]+self.a*sin(pi * self.alpha / 180), 0])
        h = sqrt(2/3)*self.a
        Ort_center = np.array([2*C[0]+self.a*cos(pi * self.alpha / 360)/3, 2*C[1]+self.a*sin(pi * self.alpha / 360)/3, 0])
        H = Ort_center + np.array([0,0,h])

        return np.array([A,B,C,H])


class RightCylinder(StereoShape):
    title = 'Right cylinder'
    input_instructions = ['Введите радиус r: ',
                          'Введите высоту h: ']
    is_polyhedron = False
    is_solid_of_revolution = True
    def __init__(self, parameters):
        self.r = parameters[0]
        self.h = parameters[1]
        super().__init__()


    def lebesgue_measure(self):
        return round(pi*self.r*self.r*self.h, self.precision)

    def border_lebesgue_measure(self):
        return round(2*pi*self.r*(self.r + self.h), self.precision)

    def info(self):
        print(f'TITLE: {self.title}')
        print(f'\tself.r = {self.r}')
        print(f'\tself.h = {self.h}')
        print(f'\tself.volume = {self.volume}')
        print(f'\tself.surface_area = {self.surface_area}')

    def get_for_drawing(self):
        dl = self.dl
        dphi = self.dphi

        h = self.h
        r = self.r

        u = np.linspace(0, 2 * pi, dphi)
        dh = np.linspace(0, 1, dl)
        x = np.outer(np.sin(u), np.ones(len(dh)))
        y = np.outer(np.cos(u), np.ones(len(dh)))

        x = r * np.outer(np.sin(u), np.ones(len(dh)))
        y = r * np.outer(np.cos(u), np.ones(len(dh)))
        z = h * np.outer(np.ones(len(u)), dh)

        return np.array([x,y,z])

    @staticmethod
    def print_pi():
        print(f'Значения констант, используемые при расчётах:\n\t\t \u03C0 = {pi}')


class RightCone(StereoShape):
    title = 'Right cone'
    input_instructions = ['Введите радиус r: ',
                          'Введите высоту h: ']
    is_polyhedron = False
    is_solid_of_revolution = True
    def __init__(self, parameters):
        self.r = parameters[0]
        self.h = parameters[1]
        super().__init__()


    def lebesgue_measure(self):
        return round(pi*self.r*self.r*self.h/3, self.precision)


    def border_lebesgue_measure(self):
        slant_height = sqrt(self.r**2 + self.h**2)
        return round(pi*self.r*(self.r + slant_height), self.precision)

    def info(self):
        print(f'TITLE: {self.title}')
        print(f'\tself.r = {self.r}')
        print(f'\tself.h = {self.h}')
        print(f'\tself.volume = {self.volume}')
        print(f'\tself.surface_area = {self.surface_area}')


    def get_for_drawing(self):
        dl = self.dl
        dphi = self.dphi

        h = self.h
        r = self.r

        u = np.linspace(0, 2 * pi, dphi)
        dh = np.linspace(0, 1, dl)
        x = np.outer(np.sin(u), np.ones(len(dh)))
        y = np.outer(np.cos(u), np.ones(len(dh)))

        x = r * np.outer(np.sin(u), dh)
        y = r * np.outer(np.cos(u), dh)
        z = h * np.outer(np.ones(len(u)), dh)

        return np.array([x,y,z])

    @staticmethod
    def print_pi():
        print(f'Значения констант, используемые при расчётах:\n\t\t \u03C0 = {pi}')
