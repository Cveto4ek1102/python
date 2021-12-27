with open('text_1.txt', 'x', encoding='utf-8') as f:
    while True:
        line = input('Напишите построчные данные или пустую строку для окончания: ')
        if not line:
            break
        print(line, file=f)