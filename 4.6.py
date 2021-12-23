from itertools import count, cycle
my_count = count(3)
my_cycle = cycle("ABC")
for _ in range(8):
    print("(my_count, my_cycle) = ({},{})".format(next(my_count), next(my_cycle)))

