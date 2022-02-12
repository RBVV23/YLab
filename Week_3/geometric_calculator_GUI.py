from math import sin, pi

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
        print(f'\tself.betta = {self.betta}')
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
        self.c = self.a + self.b - 1
        self.alpha = alpha
        self.betta = 90
        self.gamma = 90 - self.alpha
        super().__init__()

    def lebesgue_measure(self):
        return 0.5*self.a*self.b*sin(pi*self.alpha/180)

    def border_lebesgue_measure(self):
        return self.a + self.b + self.c

    def info(self):
        super().info()
        print(f'\tself.c = {self.c}')
        print(f'\tself.gamma = {self.gamma}')

class Trapezoid(PlanShape):
    title = 'Trapezoid'
    def __init__(self, a, b, c, alpha):
        self.a = a
        self.b = b
        self.c = c
        self.d = c
        self.alpha = alpha
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
        print(f'\tself.d = {self.d}')


class StereoShape(Shape):
    title = 'StereoShape'
    def __init__(self):
        self.volume = self.lebesgue_measure()
        self.perimeter = self.border_lebesgue_measure()

    def lebesgue_measure(self): # объем фигуры в пространстве
        print('Метод "StereoShape"')
        return -1

    def border_lebesgue_measure(self): #  площадь поверхности фигуры в пространстве
        print('Метод "StereoShape"')
        return -1




figure = PlanShape()
print(f'\nfigure = PlanShape()')
print(f'figure.area() = {figure.area}')
print(f'figure.perimeter() = {figure.perimeter}')


figure = Square(10)
print(f'\nfigure = Square(10)')
figure.info()

figure = Rectangle(10, 15)
print(f'\nfigure = Rectangle(10, 15)')
figure.info()

figure = Rhombus(5, 30)
print(f'\nfigure = Rectangle(5, 30)')
figure.info()

figure = Disk(10)
print(f'\nfigure = Disk(10)')
figure.info()

figure = Triangle(3, 4, 30)
print(f'\nfigure = Triangle(3, 4, 30)')
figure.info()

figure = Trapezoid(3, 4, 10, 30)
print(f'\nfigure = Trapezoid(3, 4, 10, 30)')
figure.info()