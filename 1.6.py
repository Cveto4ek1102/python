while True:
    days = 1
    first_day = float(input("Километров в первый день: "))
    goal = float(input("Цель: "))
    if first_day <= 0 or goal <= 0:
        print("Движение - это жизнь! Количество километров должно быть больше ноля")
    else:
        while first_day < goal:
            first_day *= 1.1
            days += 1
        print(f"Для достижения цели спортсмену потребуется {days} дней")
        break