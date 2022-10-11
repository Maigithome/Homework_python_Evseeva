# Задана натуральная степень k. Сформировать случайным образом список коэффициентов Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#  *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools

k = int(input("Введите степень k: "))

def get_coefficient(k):
    coefficient = [randint(0, 100) for i in range (k + 1)]
    while coefficient[0] == 0:
        coefficient[0] = randint(1, 100) 
    return coefficient

def get_polynomial(k, coefficient):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(coefficient, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


coefficient = get_coefficient(k)
polynom1 = get_polynomial(k, coefficient)
print(polynom1)

with open('Polynomial_1.txt', 'w') as data:
    data.write(polynom1)


# Второй многочлен для задачи:

k1 = randint(2, 5)

coefficient = get_coefficient(k1) 
polynom2 = get_polynomial(k1, coefficient)
print(polynom2)

with open('Polynomial_2.txt', 'w') as data:
    data.write(polynom2)

