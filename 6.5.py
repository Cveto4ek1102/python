class Stationery:
    def __init__(self, title='картинки'):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки {self.title}')
class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')
class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')
stat = Stationery()
pen = Pen('черной гелевой')
pencil = Pencil('HB')
handle = Handle('разноцветным')
chancellery = [stat, pen, pencil, handle]
for c in chancellery:
    c.draw()



