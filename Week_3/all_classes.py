from math import sin, pi, sqrt, cos

class Shape():
    title = 'Shape'
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
    def __init__(self, a, alpha):
        self.a = a
        self.b = a
        self.alpha = alpha
        self.betta = 180 - self.alpha
        super().__init__()

    def lebesgue_measure(self):
        return self.a*self.b*sin(pi*self.alpha/180)

    def border_lebesgue_measure(self):
        return 2*(self.a + self.b)

class Square(PlanShape):
    title = 'Square'
    def __init__(self, a):
        self.a = a
        self.b = self.a
        self.alpha = 90
        self.betta = 180 - self.alpha
        super().__init__()


    def lebesgue_measure(self):
        return self.a*self.a

    def border_lebesgue_measure(self):
        return 4*self.a

class Rectangle(PlanShape):
    title = 'Rectangle'
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.alpha = 90
        self.betta = 180 - self.alpha
        super().__init__()

    def lebesgue_measure(self):
        return self.a*self.b

    def border_lebesgue_measure(self):
        return 2*(self.a + self.b)

class Disk(PlanShape):
    title = 'Disk'
    def __init__(self, r):
        self.r = r
        super().__init__()


    def lebesgue_measure(self):
        return pi*self.r*self.r

    def border_lebesgue_measure(self):
        return 2*pi*self.r

    def info(self):
        print(f'TITLE: {self.title}')
        print(f'\tself.r = {self.r}')
        print(f'\tself.area = {self.area}')
        print(f'\tself.perimeter = {self.perimeter}')

class Triangle(PlanShape):
    title = 'Triangle'
    def __init__(self, a, b, alpha):
        self.a = a
        self.b = b
        self.alpha = alpha
        self.c = sqrt(self.a**2 + self.b**2 - 2*self.a*self.b*cos(pi*self.alpha/180))
        super().__init__()

    def lebesgue_measure(self):
        return 0.5*self.a*self.b*sin(pi*self.alpha/180)

    def border_lebesgue_measure(self):
        return self.a + self.b + self.c

    def info(self):
        super().info()
        # print(f'\tself.c = {self.c}')
        # print(f'\tself.gamma = {self.gamma}')

class Trapezoid(PlanShape):
    title = 'Trapezoid'
    def __init__(self, a, b, c, alpha):
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.d = sqrt((self.c/sin(pi*self.alpha/180))**2 + (self.b - self.a - self.c*cos(pi*self.alpha/180))**2)
        self.betta = 180 - self.alpha
        super().__init__()

    def lebesgue_measure(self):
        h = self.c/sin(pi*self.alpha/180)
        return 0.5*(self.a+self.b)*h

    def border_lebesgue_measure(self):
        return self.a + self.b + self.c + self.d

    def info(self):
        super().info()
        print(f'\tself.c = {self.c}')


class StereoShape(Shape):
    title = 'StereoShape'
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
    def __init__(self, r):
        self.r = r
        super().__init__()


    def lebesgue_measure(self):
        return 4*pi*self.r*self.r*self.r/3

    def border_lebesgue_measure(self):
        return 4*pi*self.r*self.r

    def info(self):
        print(f'TITLE: {self.title}')
        print(f'\tself.r = {self.r}')
        print(f'\tself.volume = {self.volume}')
        print(f'\tself.surface_area = {self.surface_area}')

class Cube(StereoShape):
    title = 'Cube'
    def __init__(self, a):
        self.a = a
        self.b = self.a
        self.h = self.a
        super().__init__()


    def lebesgue_measure(self):
        return self.a*self.a*self.a

    def border_lebesgue_measure(self):
        return 6*self.a*self.a

class Cuboid(StereoShape):
    title = 'Cuboid'
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
        super().__init__()

    def lebesgue_measure(self):
        return self.a*self.b*self.h

    def border_lebesgue_measure(self):
        return 2*(self.a*self.b + self.b*self.h + self.a*self.h)

class RightTetrahedron(StereoShape):
    title = 'Right tetrahedron'
    def __init__(self, a):
        self.a = a
        self.b = a
        self.h = sqrt(2*self.a*self.a/3)
        self.alpha = 60
        super().__init__()

    def lebesgue_measure(self):
        S_base = 0.5*self.a*self.b*sin(pi*self.alpha/180)
        return S_base*self.h/3

    def border_lebesgue_measure(self):
        S_base = 0.5 * self.a * self.b * sin(pi * self.alpha / 180)
        return 4*S_base

class RightCylinder(StereoShape):
    title = 'Right cylinder'
    def __init__(self, r, h):
        self.r = r
        self.h = h
        super().__init__()


    def lebesgue_measure(self):
        return pi*self.r*self.r*self.h

    def border_lebesgue_measure(self):
        return 2*pi*self.r*(self.r + self.h)

    def info(self):
        print(f'TITLE: {self.title}')
        print(f'\tself.r = {self.r}')
        print(f'\tself.h = {self.h}')
        print(f'\tself.volume = {self.volume}')
        print(f'\tself.surface_area = {self.surface_area}')

class RightCone(StereoShape):
    title = 'Right cone'
    def __init__(self, r, h):
        self.r = r
        self.h = h
        super().__init__()


    def lebesgue_measure(self):
        return pi*self.r*self.r*self.h/3

    def border_lebesgue_measure(self):
        slant_height = sqrt(self.r**2 + self.h**2)
        return pi*self.r*(self.r + slant_height)

    def info(self):
        print(f'TITLE: {self.title}')
        print(f'\tself.r = {self.r}')
        print(f'\tself.h = {self.h}')
        print(f'\tself.volume = {self.volume}')
        print(f'\tself.surface_area = {self.surface_area}')
