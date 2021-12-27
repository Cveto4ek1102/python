with open('text_3.txt', 'r', encoding='utf-8') as f:
    my_list = [f'{line}. {count.strip()} - {len(count.split())} слов'
              for line, count in enumerate(f, 1)]
    print(*my_list, f'Всего строк - {len(my_list)}', sep='\n')