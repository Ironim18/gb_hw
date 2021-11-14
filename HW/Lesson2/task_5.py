rating = [7, 5, 5, 4, 2, 2, 1]

number = int(input("Введите число: "))
x, i = 0, 0
while i < rating.__len__():
    if number > rating[i]:
        rating.insert(i, number)
        x += 1
        break
    i += 1

if x == 0:
    rating.append(number)

print(rating)
