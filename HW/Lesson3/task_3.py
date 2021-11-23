def my_func(n1, n2, n3):
    sn = n1 + n2 + n3
    return sn - min(n1, n2, n3)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
print(f'Сумма наименьших двух слогаемых - {my_func(a, b, c)}')
