class Error:
    def __init__(self):
        self.my_list = []

    def my_num(self):

        while True:
            try:
                val = int(input('Введите число: '))
                self.my_list.append(val)
                print(f'Ваш список: - {self.my_list} \n ')
            except:
                print(f"Вводите только числа!")
                exit = input(f'Продолжаем? Нажмите Enter. Для выхода введите "q" ')

                if exit == 'q' or exit == 'Q':
                    return f'Ну и ладно. До свидания.'
                else:
                    print(try_except.my_num())
                    break


try_except = Error()
print(try_except.my_num())