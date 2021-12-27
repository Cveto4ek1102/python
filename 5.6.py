my_list = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        les, num = line.split(':')
        les_sum = sum(map(int, ''.join([i for i in num if i == ' ' or '9' >= i >= '0']).split()))
        my_list[les] = les_sum
    print(f'{my_list}')