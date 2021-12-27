with open('text_3.txt', 'r', encoding='utf-8') as f:
    everybody = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Несчастные с зарплатой меньше 20 тысяч {[i[0] for i in everybody.items() if i[1] < 20000]}\n'
          f'Средняя зп = {round(sum(everybody.values()) / len(everybody), 2)}')