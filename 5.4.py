trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text_4rus.txt', 'w', encoding='utf-8') as ru_file:
    with open('text_4.txt', encoding='utf-8') as en_file:
        ru_file.writelines([line.replace(line.split()[0], trans.get(line.split()[0])) for line in en_file])