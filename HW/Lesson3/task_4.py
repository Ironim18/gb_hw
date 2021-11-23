def my_func(x, y):
    if x < 0:
        return 'Х должен быть больше нуля.'
    if y > 0:
        return 'Y должен быть больше нуля.'
    # Первый вариант
    # return x ** y
    # Второй вариант
    z = 1
    for i in range(y * -1):
        z *= x
    return 1 / z


x = float(input("Введите положительное чило (х): "))
y = int(input("Введите целое отрицательное (y): "))
print(my_func(x, y))
