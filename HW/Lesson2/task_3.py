winter, spring, summer, autumn = "зима", "весна", "лето", "осень"
seasons_dict = {1: winter, 2: winter, 3: spring, 4: spring, 5: spring, 6: summer, 7: summer, 8: summer, 9: autumn, 10: autumn, 11: autumn, 12: winter}

month = int(input("Укажите номер месяца: "))

print(f"Этот месяц относится к сезону - {seasons_dict[month]}")

seasons_list = [winter, winter, spring, spring, spring, summer, summer, summer, autumn, autumn, autumn, winter]

print(f"Этот месяц относится к сезону - {seasons_list[month - 1]}")
