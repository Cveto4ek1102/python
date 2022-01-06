class Division(Exception):
    def __init__(self, res):
        self.res = res


def div():
    try:
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель (только не 0): '))
        if num_2 == 0:
            return Division("Ну попросили же не 0!")
        else:
            res = num_1 / num_2
            return res
    except ValueError:
        return "Введите число"
    except Division as err:
        return err


print(div())