proceed = float(input("Укажите свою выручку: "))
costs = float(input("Укажите свои издержки: "))
profit = proceed - costs
if profit > 0:
    print(f"Вы большой мододец! Заработали {profit} денюшек!")
    print(f"Ваша рентабельность {100 * profit / proceed:.1f}%")
    staff = int(input("Сколько у вас сотрудников? "))
    print(f"На каждого получается по {profit / staff} денюшек")
elif profit < 0:
    print(f"У вас пока убытки {-profit} денюшек. Ну вы это, не унывайте!")
else:
    print("Пока работаете в ноль. Поднажмите!")