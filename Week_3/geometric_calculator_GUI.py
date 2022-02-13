from all_classes import *

figure = PlanShape()
print(f'\nfigure = PlanShape()')
print(f'figure.area() = {figure.area}')
print(f'figure.perimeter() = {figure.perimeter}')

#  плоские тесты
# figure = Square(10)
# print(f'\nfigure = Square(10)')
# figure.info()
#
# figure = Rectangle(10, 15)
# print(f'\nfigure = Rectangle(10, 15)')
# figure.info()
#
# figure = Rhombus(5, 30)
# print(f'\nfigure = Rectangle(5, 30)')
# figure.info()
#
# figure = Disk(10)
# print(f'\nfigure = Disk(10)')
# figure.info()
#
# figure = Triangle(3, 4, 30)
# print(f'\nfigure = Triangle(3, 4, 30)')
# figure.info()
#
# figure = Trapezoid(3, 4, 10, 30)
# print(f'\nfigure = Trapezoid(3, 4, 10, 30)')
# figure.info()

figure = StereoShape()
print(f'\nfigure = StreoShape()')
print(f'figure.volume() = {figure.volume}')
print(f'figure.surface_area() = {figure.surface_area}')

figure = Ball(10)
print(f'\nfigure = Ball(10)')
figure.info()

figure = Cube(2)
print(f'\nfigure = Cube(2)')
figure.info()

figure = Cuboid(3, 4, 5)
print(f'\nfigure = Cuboid(3, 4, 5)')
figure.info()

figure = RightTetrahedron(3)
print(f'\nfigure = RightTetrahedron(3)')
figure.info()

figure = RightCylinder(3, 10)
print(f'\nfigure = Cylinder(3, 10)')
figure.info()

figure = RightCone(3, 4)
print(f'\nfigure = RightCone(3, 10)')
figure.info()