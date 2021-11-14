a_list = list(input("Напишите что хотите: "))
i = 0

if a_list > 1:
    while i < (a_list.__len__() - 1):
        a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        i += 2

print(a_list)
