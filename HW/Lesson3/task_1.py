x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))


def func(a, b):
    if y != 0:
        return a / b
    else:
        return "Нельзя делить на ноль."


print(func(x, y))
