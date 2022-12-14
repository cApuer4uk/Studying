from math import *
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (- b + d ** 0.5) / (2 * a)
    x2 = (- b - d ** 0.5) / (2 * a)
    answer = [x1, x2]
    answer.sort()
    for x in answer:
        print(x)
elif d == 0:
    x = - b / (2 * a)
    print(x)
else:
    print('Нет корней')