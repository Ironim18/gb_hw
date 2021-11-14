products = []
num = 1
stop = ''

print('Введите информацию о товарах.')

while stop != 'q':
    name = input('Название: ')
    price = input('Цена: ')
    amount = input('Количество: ')
    units = input('Еденица измерения: ')
    products.append((num, {'name': name, 'price': price, 'amount': amount, 'units': units}))
    num += 1
    stop = input('Для выхода из системы ввода напишите "q": ')

# Не смог сделать самостоятельно.
