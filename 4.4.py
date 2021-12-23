from random import randint
my_list = [randint(1, 44) for _ in range(14)]
numbers = [num for num in my_list if my_list.count(num) == 1]
print(numbers)