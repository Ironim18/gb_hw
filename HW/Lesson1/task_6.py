a = float(input("Укажите начальную дистанцию: "))
b = float(input("Укажите желаемую дистанцию: "))
day = 1

while a < b:
    a *= 1.1
    day += 1

print(f"На {day}-й день спортсмен достиг результата — не менее {b} км.")