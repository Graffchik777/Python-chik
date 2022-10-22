#  33. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от -100 до 100) многочлена и записать в файл многочлен степени k.

from random import randint
import itertools as it


def koof_list(k):
    koof = [randint(-100, 100) for i in range(k + 1)]
    if koof[0] == 0:
        koof[0] = randint(-100, 101)
    return koof


def polynom_list(coof, koof):
    step = ['*x^']*(coof-1) + ['*x']
    polynom = [[a, b, c] for a, b, c in it.zip_longest(koof, step, range(coof, 1, -1), fillvalue='') if a != 0]
    for x in polynom:
        x.append(' + ')
    polynom = list(it.chain(*polynom))
    polynom[-1] = ' = 0'
    return " ".join(map(str, polynom)).replace(' 1*x', ' x')


coof = randint(2, 9)
koof = koof_list(coof)
polynom = polynom_list(coof, koof)
print(polynom)
