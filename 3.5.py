def sum_num():
    s = 0
    while True:
        in_list = input("Напишите числа через пробел или 'q' чтобы выйти: ").split()
        for num in in_list:
            if num.lower() == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("Для выхода напишите 'q'")
        print(f"Сумма всех чисел = {s}")
print(sum_num())