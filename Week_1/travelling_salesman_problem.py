from itertools import permutations
from math import inf

address = (
    (0, 2),
    (2, 5),
    (5, 2),
    (6, 6),
    (8, 3)
        )


def my_euclid_dist(point_1, point_2):
    """Возвращает евклидово расстояния между точками на плоскости"""

    dist = ((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)**0.5
    return dist


def my_route_length(route, address=address):
    """Возвращает длину пути почтальона"""

    start = my_euclid_dist(address[0], address[route[0]])
    length = 0
    for i,j in zip(route[:-1], route[1:]):
        length += my_euclid_dist(address[i], address[j])
    finish = my_euclid_dist(address[route[-1]], address[0])
    result = start + length + finish
    return result


def my_answer_writer(route, address=address):
    """Возвращает строку с форматированным выводом результата"""

    length = 0
    res_route = list([0])
    res_route.extend(route)
    res_route.append(0)
    string = f'({address[res_route[0]][0]}, {address[res_route[0]][1]})'

    for i,j in zip(res_route[:-1], res_route[1:]):
        length += my_euclid_dist(address[i], address[j])
        string += f' -> ({address[j][0]}, {address[j][1]})[{length}]'

    finish_string = f' = {length}'
    res_string = string + finish_string
    return res_string

# print(my_answer_writer.__doc__)
# print(my_euclid_dist.__doc__)
# print(my_route_length.__doc__)

L = len(address) - 1 # количество промежуточных пунктов (само здание почты не считаем)
all_routes = list(permutations(list(range(1,L+1)),L))   # все 24 варианта маршрута
                                                        # первый и последний пункт - почта,
                                                        # его мы по умолчанию не указываем

min_dist = inf
min_index = -1
for i,route in enumerate(all_routes):
    dist = my_route_length(route)
    if min_dist > dist:
        min_dist = dist
        min_index = i

# print('Длина кратчайшего пути: ', min_dist)
# print('Порядковый номер кратчайшего маршрута: ', min_index)
# print('Порядок кратчайшего обхода адресатов: ', all_routes[min_index])

print(my_answer_writer(all_routes[min_index]))
# стоит отметить, что из-за свойств евклидова пространства, расстояние между точками не зависит от направления
# движения, поэтому помимо полученного маршрута такой же длинной обладает и симметричный ему
