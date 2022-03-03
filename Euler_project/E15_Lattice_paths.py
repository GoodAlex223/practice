"""Problem 15. 04.02.21
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

SOlUTION:
We have n x n grid, where n -- even number. If only being able to move to the right and down, there are exactly n * 2
moves to the bottom right corner, n moves to the right, n -- to the down. A new question:
how many ways can n (right or down)moves be placed in n * 2 moves(Because others n will be placed by convention)
(Order is not important)? В этом случае можно использовать класическую формулу сочетания без повторения:
С = n!/(m!*(n-m)!). Формула решения выглядит: С = (n*2)!/(n!*n!)

Программа выводит количество путей прохождения от левого верхнего до правого нижнего.
"""
import math

n = int(input("Введите размер вашей квадратной сетки(одно число): "))
print(int(math.factorial(n*2)/(math.factorial(n) * math.factorial(n))))
