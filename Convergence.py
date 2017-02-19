import sys
import sympy
from sympy import *


def cauchy(expression):
    n = Symbol("n")
    return limit(expression ** (1 / n), n, oo)


def with_harmonic(expression):
    n = Symbol("n")
    return limit(expression / (1 / n), n, oo)


def with_convergent(expression):
    n = Symbol("n")
    return limit(expression / (1 / 2 * n), n, oo)


def is_convergent(expression):
    n = Symbol("n")
    pprint(expression)

    # Проверяем необходимое условие
    necessary = limit(expression, n, oo)
    if (necessary != 0):
        return "Sequence does not converge by the necessary condition"

    # Проверяем достаточное условие по признаку Коши
    enough_cauchy = cauchy(expression)
    if (enough_cauchy < 1):
        return "Sequence converges because cauchy < 1"
    if (enough_cauchy > 1):
        return "Sequence does not converge because cauchy > 1"

    # Признак Коши не дал ответа, сравниваем с расходящимся рядом (гармоничным)
    enough_n = with_harmonic(expression)
    if (enough_n > 0):
        return "Sequence does not converge because harmonic comparison > 0"

    # Сравнение с гармоничным рядом не дало ответа, сравниваем со сходящимся рядом
    enough_y = with_convergent(expression)
    if (enough_y >= 0):
        return "Sequence converges because comparison with convergent sequence >= 0"

    return "Something wrong"

