from random import randint
with open('text_2.txt', mode='w+', encoding='utf-8') as numbers:
    numbers.write(' '.join([str(randint(1, 500)) for _ in range(25)]))
    numbers.seek(0)
    print(sum(map(int, numbers.readline().split())))