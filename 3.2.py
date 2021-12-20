def your_inf(**kwargs):
    return " ".join(kwargs.values())
print(your_inf(name = input("Ваше имя: "), surname = input("Ваша фамилия: "),
               year = input("Год рождения: "), city = input("Город проживания: "),
               email = input("Email: "), phone = input("Номер телефона: ")))