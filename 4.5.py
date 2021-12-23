from _functools import reduce
def my_list(num_1, num_2):
    return num_1 * num_2
numbers = [num for num in range(100, 1001, 2)]
print(f"Result\n{numbers}\nmultiplication of numbers\n{reduce(my_list, numbers)}")