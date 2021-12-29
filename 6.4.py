from random import choice
class Car:
    direction = ['left', 'right', 'back']
    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'This car: {n} is {c}.\nIs it a police car? {p}')
    def go(self):
        print(f'{self.name} rides')
    def stop(self):
        print(f'{self.name} stopped')
    def turn(self):
        print(f'{self.name} turn {choice(self.direction)}')
    def show_speed(self):
        return f'{self.name}s speed is {self.speed}'
class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed()
class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()
class SportCar(Car):
    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Too fast, bro!' if self.speed > 120 else super().show_speed()
class PoliceCar(Car):
    def __init__(self, n, c, s):
        super().__init__(n, c, s, p=True)
    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Ok! Just do your job! But be careful!' \
            if self.speed > 80 else super().show_speed()
town_car = TownCar('Honda Jazz', 'blue', 73)
work_car = WorkCar('CAT', 'yellow', 25)
sport_car = SportCar('Ferrari', 'red', 135)
police_car = PoliceCar("Donut's Car", "white", 94)
list_of_cars = [town_car, work_car, sport_car, police_car]
for i in list_of_cars:
    i.go
    print(i.show_speed())
    i.turn()
    i.stop()
    print()





