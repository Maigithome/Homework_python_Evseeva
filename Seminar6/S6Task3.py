# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

import re
import itertools


file1 = 'Polynomial_1.txt'
file2 = 'Polynomial_2.txt'
file_sum = 'Sum_polynomials.txt'

# Получение данных из файла

def read_polinom(file):
    with open(str(file), 'r') as data:
        polinom = data.read()
    return polinom

# Получение списка кортежей каждого (<коэффициент>, <степень>)

def convert_pol(polinom):
    polinom = polinom.replace('= 0', '')
    polinom = re.sub("[*|^| ]", " ", polinom).split('+')
    polinom = [char.split(' ') for char in polinom]
    polinom = [[x for x in list if x] for list in polinom]
    for i in polinom:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    polinom = [tuple(int(x) for x in j if x != 'x') for j in polinom]
    return polinom

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

def fold_pols(polinom1, polinom2):   
    x = [0] * (max(polinom1[0][1], polinom2[0][1] + 1))
    for i in polinom1 + polinom2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

# Составление итогового многочлена

def get_sum_pol(polinom):
    var = ['*x^'] * len(polinom)
    coefs = [x[0] for x in polinom]
    degrees = [x[1] for x in polinom]
    new_polinom = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_polinom:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_polinom = list(itertools.chain(*new_polinom))
    new_polinom[-1] = ' = 0'
    return "".join(map(str, new_polinom))

def write_to_file(file, polinom):
    with open(file, 'w') as data:
        data.write(polinom)

polinom1 = read_polinom(file1)
polinom2 = read_polinom(file2)
polinom_1 = convert_pol(polinom1)
polinom_2 = convert_pol(polinom2)

polinom_sum = get_sum_pol(fold_pols(polinom_1, polinom_2))
write_to_file(file_sum, polinom_sum)

print(polinom1)
print(polinom2)
print(polinom_sum)