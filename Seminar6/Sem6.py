# 1) Вычислить число π c заданной точностью d
# Пример:при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

# print('Программа выведет число π с определенной точностью.')
# user_number = input('Формат ввода: 0.001 -> покажет 3 цифры после запятой.\nВведите значение: ')
# size = abs(len(user_number) - user_number.find('.') - 1)
# pi = 0
# for i in range(size):
#     pi += (1 / 16 ** i) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6)))

# print(str(pi)[:len(user_number)])

# 36.	Не решили! Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

lst = list(map(int, input("Введите числа через пробел:\n").split()))
for j in range(len(lst)-1):
    new_lst = [lst[j]]
    for i in range(len(lst)):
        if lst[i]>new_lst[-1]: #and lst[i+1]<lst[i+2]:
            new_lst.append(lst[i])
            print(new_lst)
        

# Дан список чисел. Создать список, в который
# попадают числа, описываемые возрастающую
# последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3]
# или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя
nums = [1, 5, 2, 3, 4, 6, 1, 7]

list01 = [1, 5, 2, 3, 4, 6, 1, 7]
list01 = list(map(int, list01))

#k = 0
for i in range(len(list01)):
    list02 = []
    list02.append(min(list01))
    for j in range(i, len(list01)):
        if list02[-1] < list01[j]:
            #k += 1
            list02.append(list01[j])
    print(list02)


# 36. Дан список чисел. Создать список, в который попадают числа,
# описываемые возрастающую последовательность.
# *Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.*
# ***Порядок элементов менять нельзя***

nums = [3, 1, 2, 3, 4, 6, 1, 7]

# Первый вариант

def get_up2(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups
    
print(get_up2(nums))

# Второй вариант

def get_up(nums):
    ups = []
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
            ups.append(nums[i])
    return ups

print(get_up(nums))

# 41.	Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. 
# приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
#  .	Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;

st = input()
for el in ['+', '-', '*', '/']:
    st = st.replace(el, f' {el} ')
st_list = st.split()

for i in range(len(st_list)-1):
    if st_list[i] == '*':
        result = int(st_list[i-1]) * int(st_list[i+1])
        st_list[i] = result
        st_list[i-1] = None
        st_list[i+1] = None
st_list = [el for el in st_list if el != None] #'это часть кода


# крестики-нолики

field = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

def print_field(field):
    for el in field:
        print(el)

def fill_num_in_field(field, n):
    for el in field:
        for i in range(len(el)):
            if el[i] == n:
                el[i] = 'x'

print_field(field)

a = int(input('Введите цифру, куда хотите поставить крестик: '))
fill_num_in_field(field, a)
print_field(field)


