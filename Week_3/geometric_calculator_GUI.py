

class Shape():
    # для плоских фигур мера Лебега - это площадь, а для объемных - объем
    def lebesgue_measure(self):
        print('Метод "Shape"')
        # pass

    # для плоских фигур мера Лебега границы - это периметр, а для объёмных - площадь поверхности
    def border_lebesgue_measure(self):
        print('Метод "Shape"')


class PlanShape(Shape):
    def lebesgue_measure(self): # площадь фигуры на плоскости
        print('Метод "PlanShape"')

    def border_lebesgue_measure(self): #  периметр плоской на плоскости
        print('Метод "PlanShape"')

class Parallelogram(PlanShape):
    pass

class StereoShape(Shape):
    def lebesgue_measure(self): # объем фигуры в пространстве
        pass

    def border_lebesgue_measure(self): #  площадь поверхности фигуры в пространстве
        pass


figure = Parallelogram()

figure.lebesgue_measure()