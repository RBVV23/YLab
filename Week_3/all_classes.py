from math import sin, pi, sqrt, cos
import numpy as np


class Shape():
    title = 'Shape'
    precision = 3
    # для плоских фигур мера Лебега - это площадь, а для объемных - объем
    def __init__(self, a):
        self.a = a

    def lebesgue_measure(self):
        print('Метод "Shape.lebesgue_measure()"')
        # pass

    # для плоских фигур мера Лебега границы - это периметр, а для объёмных - площадь поверхности
    def border_lebesgue_measure(self):
        print('Метод "Shape.border_lebesgue_measure()"')


class PlanShape(Shape):
    title = 'PlanShape'
    lebesgue_measure_name = 'Площадь'
    border_lebesgue_measure_name = 'Периметр'
    is_plan = True
    is_circle = False

    def __init__(self):
        # self.a = a
        self.area = self.lebesgue_measure()
        self.perimeter = self.border_lebesgue_measure()

    def lebesgue_measure(self): # площадь фигуры на плоскости
        # self.area = -1
        print('Метод "PlanShape"')
        return -1

    def border_lebesgue_measure(self): #  периметр плоской на плоскости
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


    def building(self):
        A = (0,0)
        B = (A[0] + self.a, 0)
        D = (A[0] + self.b*cos(pi*self.alpha/180), A[1] + self.b*sin(pi*self.alpha/180))
        C = (D[0] + self.a, D[1])
        return (A,B,C,D)


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

    def building(self):
        A = (0,0)
        B = (0, A[1] + self.a)
        C = (B[0] + self.a, B[1])
        D = (C[0], C[1] - self.a)
        return (A,B,C,D)


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

    def building(self):
        A = (0,0)
        B = (0, A[1] + self.b)
        C = (B[0] + self.a, B[1])
        D = (C[0], C[1] - self.b)
        return (A,B,C,D)


class Disk(PlanShape):
    title = 'Disk'
    input_instructions = ['Введите радиус r: ']
    is_circle = True
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

    def building(self):
        return self.r


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

    def building(self):
        C = (0,0)
        B = (C[0] + self.a, C[1])
        A = (C[0] + self.b*cos(pi*self.alpha/180), C[1] + self.b*sin(pi*self.alpha/180))
        return (A,B,C)


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

    def building(self):
        A = (0,0)
        B = (A[0] + self.a, 0)
        D = (A[0] + self.c*cos(pi*self.alpha/180), A[1] + self.c*sin(pi*self.alpha/180))
        C = (D[0] + self.b, D[1])
        return (A,B,C,D)


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
    is_ball = True
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

    def building(self):
        return np.array([self.r])

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

    def building(self):
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

    def building(self):
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

    def building(self):
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

    def building(self):
        return np.array([self.r, self.h])

class RightCone(StereoShape):
    title = 'Right cone'
    input_instructions = ['Введите радиус r: ',
                          'Введите высоту h: ']
    is_polyhedron = False
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

    def building(self):
        return np.array([self.r, self.h])
