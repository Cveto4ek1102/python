def my_func(x, y):
    try:
        result = x ** y
    except TypeError:
        return "Нужно действительное положительное число x и целое отрицательное число y"
    return result
print(my_func(8, -3))