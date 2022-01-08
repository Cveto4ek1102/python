class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель устройства': self.name, 'Цена за 1 шт': self.price, 'Количество': self.quantity}
        self.my_list = []

    def income(self):
        try:
            name = input(f'Введите наименование: ')
            price = int(input(f'Введите цену за 1 шт: '))
            quantity = int(input(f'Введите количество: '))
            item = {'Модель устройства': name, 'Цена за 1 шт': price, 'Количество': quantity}
            self.my_list.append(item)
            print(f'{self.my_list}\n')
        except ValueError:
            print('Недопустимое значение!')

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'Продолжаем? ')
        if q == 'Q' or q == 'q':
            return f'Выход'
        else:
            return OfficeEquipment.income(self)


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


p = Printer('Canon', 5300, 26)
s = Scanner('Epson', 9990, 8)
x = Xerox('HP', 14499, 19)
p.income()
s.income()
x.income()
