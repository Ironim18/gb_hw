

time = int(input("Введите время в секундах: "))

sec = time % 60
minute = (time // 60) % 60
hour = time // 3600

print(f"Время в формате чч:мм:сс; {hour:02}:{minute:02}:{sec:02}")
