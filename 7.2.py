from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption

class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        if size < 38:
            print('Размерный ряд с 38 до 58. Расчет для 38')
            self.__size = 38
        elif size > 58:
            print('Размерный ряд с 38 до 58. Расчет для 58')
            self.__size = 58
        else:
            self.__size = size
    @property
    def consumption(self):
        return self.__size / 6.5 + 0.5

class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.__height = height
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if height < 150:
            print('Рост от 150 до 210. Расчет для 150')
            self.__height = 150
        elif height > 210:
            print('Рост от 150 до 210. Расчет для 210')
        else:
            self.__height = height
    @property
    def consumption(self):
        return 2 * (self.__height / 100) + 0.3

coat = Coat(int(input('Укажите размер пальто: ')))
print(f'Для размера {coat.size} потребуется {coat.consumption:.2f} метров ткани')
costume = Costume(int(input('Укажите свой рост в сантиметрах для расчета ткани на костюм: ')))
print(f'Для роста {costume.height} потребуется {costume.consumption:.2f} метров ткани')
print(f'Всего потребуется {coat + costume:.2f} метров ткани')
