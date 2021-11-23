def s_sum(s_nums, stop):
    nums_list = s_nums.split(' ')
    sum_list = 0
    for i in nums_list:
        if i == stop:
            break
        sum_list += int(i)
    return sum_list


stop = 's'
stopped = False
ns = 0
while not stopped:
    nums_str = input("Введите числа раделяя их пробелом. Для остановки ввода используйте символ 's': ")
    ns += s_sum(nums_str, stop)
    stopped = stop in nums_str
    print(f'Сумма = {ns}')
