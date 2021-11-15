def int_func(w):
    word = w[0].upper() + w[1:]
    return word


string = input("Введите слово или слова маленькими латинскими буквами: ")
for word in string.split(' '):
    print(f'{int_func(word)}', end=' ')
