print('1е задание')

'''
1. Поработайте с переменными, создайте несколько,
 выведите на экран,
 запросите у пользователя несколько чисел и строк и сохраните в переменные,
 выведите на экран.
'''

# Создать несколько переменных и вывести на экран
a, b, c, d = 1, 2, 3, 4

print(a, b, c, d)

# Запросить несколько чисел

k_num = 4  # сколько чисел введет пользователь

numbers = []
for i in range(k_num):
    numbers.append(float(input(f'Введите {i} из {k_num} число: ')))  # в условии не уточнено, какие числа => float

k_str = 4  # сколько строк введет пользователь

strings = []
for i in range(k_str):
    strings.append(input(f'Введите {i} из {k_str} строку: '))

# Сохранить в переменные
num1, num2, num3, num4 = numbers[0], numbers[1], numbers[2], numbers[3]
str1, str2, str3, str4 = strings[0], strings[1], strings[2], strings[3]

# Вывести
print(num1, num2, num3, num4)
print(str1, str2, str3, str4)


print('2е задание')
'''
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''

seconds = int(input('Введите количество секунд: '))

h = seconds // (60 * 60)
m = (seconds - h * 60 * 60) // 60
s = seconds - h * 60 * 60 - m * 60


def format_time(x):
    return str(x) if x//10 != 0 else '0' + str(x)


hh = format_time(h)
mm = format_time(m)
ss = format_time(s)

print(f'{hh}:{mm}:{ss}')

print('3е задание')

'''
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''


def make_num(x):
    # в условии не уточнено, какие числа, поэтому:
    try:
        x = int(x)
    except ValueError:
        x = float(x)
    return x + int(str(x)*2) + int(str(x)*3)


n = input('Введите число: ')

print(make_num(n))

print('4е задание')

'''
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

# Задание гораздо проще решить без арифметических операций и while, например:
print('Более простой вариант решения: ')

n = input('Введите число: ')
print(max([int(x) for x in n]))

print('Решение согласно заданному условию: ')

n = int(input('Введите число: '))
max_n = 0
while n != 0:
    last_n = n % 10
    if max_n < last_n:
        max_n = last_n
    n = n // 10
print(max_n)

print('5е задание')

'''
5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма 
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. 
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

in_money, out_money = float(input('Введите выручку фирмы ')), float(input('Введите издержки фирмы '))

is_positive = in_money > out_money  # В контексте данного условия не указано, что равенство попадает в прибыль
# или что в убыток.

if is_positive:
    print('Прибыль')
elif in_money == out_money:
    print('В условии равенство не относится ни к прибыли ни к убыткам. ')
else:
    print('Убыток')

if is_positive:
    print(f'Рентабельность равна {(in_money-out_money)/in_money}')
    k_people = int(input('Введите количество сотрудников '))
    print(f'Прибыль фирмы в расчете на одного сотрудника равна {(in_money-out_money)/k_people}')

print('6е задание')

'''
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:

1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''

a, b = float(input('Введите результат за 1й день ')), float(input('Введите финальный результат '))
days = 1
while b > a:
    a = a + a * 0.1
    days += 1

# "выводить одно натуральное число — номер дня" противоречит формату ответа в примере. Поэтому 2 варианта вывода:
print('Обнаружено противоречие в примере ответа и в условии. ')
print('Вывод согласно условию: ')
print(days)
print('Вывод согласно примеру ответа: ')
print(f'на {days}-й день спортсмен достиг результата — не менее {b} км.')