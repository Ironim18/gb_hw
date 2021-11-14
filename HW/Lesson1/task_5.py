

income = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))

if income > costs:
    print(f"Прибыль фирмы составила: {income - costs}")
    print(f"Рентабельность выручки: {(income - costs) / income}")
    men = int(input("Укажите кол-во сотрудников: "))
    print(f"Прибыль на сотрудника составила: {(income - costs) / men}")

else:
    print(f"Убыток фирмы сотавил: {costs - income}")
