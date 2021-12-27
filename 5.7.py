import json
from json import dump
with open('text_7.txt', 'r', encoding='utf-8') as read_file:
    with open('text_77.json', 'w', encoding='utf-8') as write_file:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in read_file}
        result = [profit, {'average_profit': round(sum([int(f) for f in profit.values() if int(f) > 0]) /
                                                   len([int(f) for f in profit.values() if int(f) > 0]))}]
        json.dump(result, write_file, ensure_ascii=False, indent=4)