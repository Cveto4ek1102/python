class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        my_date = []

        for i in date.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2022:
                    return f'{day, month, year} - right date'
                else:
                    return f'{year} - wrong year'
            else:
                return f'{month} - wrong month'
        else:
            return f'{day} - wrong day'


print(Data.extract('21 - 7 - 2018'))
print(Data.valid(30, 12, 2021))
print(Data.valid(12, 18, 2021))
print(Data.valid(9, 1, 2022))
