def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ZeroDivisionError:
        return "Только не ноль!"
    except ValueError:
        return "Надо число"
    return round(div_num, 2)
print(div(input("Напишите число: "), input("И еще число: ")))