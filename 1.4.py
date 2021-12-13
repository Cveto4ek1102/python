your_num = int(input("Напишите любое число: "))
biggest = 0

while your_num > 0:
    num = your_num % 10
    if num > biggest:
        biggest = num
        if biggest == 9:
            break
    your_num = your_num // 10

print(f"Самая большая цифра в вашем числе это {biggest}")