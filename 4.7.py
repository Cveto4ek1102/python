def fact(number):
    fact_num = 1
    for n in range(number + 1):
        yield f'{n}! = {fact_num}'
        fact_num *= n + 1
for el in fact(int(input("Enter your number: "))):
    print(el)