# Написати функцію square, яка приймає 1 аргумент - сторону квадрата,
# і повертає 3 значення (за допомогою кортежу): периметр квадрата,
# площу квадрата і діагональ квадрата.

def square(side):
    from math import sqrt
    perimeter_square = side * 4
    area_square = side ** 2
    diagonal_square = sqrt(side ** 2 + side ** 2)

    return perimeter_square, area_square, diagonal_square
