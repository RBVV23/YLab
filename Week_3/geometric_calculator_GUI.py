

class Shape():
    title = 'Shape'
    # для плоских фигур мера Лебега - это площадь, а для объемных - объем
    def __init__(self, a):
        self.a = a

    def lebesgue_measure(self):
        print('Метод "Shape"')
        # pass

    # для плоских фигур мера Лебега границы - это периметр, а для объёмных - площадь поверхности
    def border_lebesgue_measure(self):
        print('Метод "Shape"')


class PlanShape(Shape):
    title = 'PlanShape'
    def __init__(self):
        self.area = self.lebesgue_measure()
        self.perimeter = self.border_lebesgue_measure()

    def lebesgue_measure(self): # площадь фигуры на плоскости
        self.area = -1
        print('Метод "PlanShape"')

    def border_lebesgue_measure(self): #  периметр плоской на плоскости
        self.perimeter = -1
        print('Метод "PlanShape"')

class Parallelogram(PlanShape):
    title = 'Parallelogram'
    def __init__(self, a, b, alpha):
        super().__init__()
        self.b = b
        self.alpha = alpha
        self.betta = 180 - self.alpha
    def info(self):
        print(f'TITLE: {self.title}')
        print(f'\tself.a = {self.a}')
        print(f'\tself.b = {self.b}')
        print(f'\tself.alpha = {self.alpha}')
        print(f'\tself.betta = {self.betta}')


class Square(Parallelogram):
    title = 'Square'
    def __init__(self, a):
        self.a = a
        self.b = a
        self.alpha = 90
        self.betta = 180 - self.alpha
        print(f'self.a = {self.a}')

    def lebesgue_measure(self):
        return self.a*self.a

    def border_lebesgue_measure(self):
        return 4*self.a

class Rectangle(Parallelogram):
    title = 'Rectangle'
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.alpha = 90
        self.betta = 180 - self.alpha

    def lebesgue_measure(self):
        return self.a*self.b

    def border_lebesgue_measure(self):
        return 2*(self.a + self.b)


class StereoShape(Shape):
    title = 'StereoShape'
    def lebesgue_measure(self): # объем фигуры в пространстве
        self.volume = -1
        pass

    def border_lebesgue_measure(self): #  площадь поверхности фигуры в пространстве
        self.border_area = -1
        pass



figure = Square(10)
print(f'figure = Square(10)')
print(figure.lebesgue_measure())
print(figure.border_lebesgue_measure())
figure.info()

figure = Rectangle(10, 15)
print(f'figure = Rectangle(10)')
print(figure.lebesgue_measure())
print(figure.border_lebesgue_measure())
figure.info()

figure = PlanShape()
print(f'figure = PlanShape()')
print(figure.lebesgue_measure())
print(figure.border_lebesgue_measure())
print(f'figure.area() = {figure.area}')
print(f'figure.perimeter() = {figure.perimeter}')