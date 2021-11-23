n = input("Имя: ")
s = input("Фамилия: ")
y = input("Год рождения: ")
c = input("Город проживания: ")
e = input("E-mail: ")
p = input("Телефон: ")


def info_card(n, s, y, c, e, p):
    return f'{n} {s} {y} {c} {e} {p}'


print(info_card(n, s, y, c, e, p))
