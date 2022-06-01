from datetime import datetime
import random


class Person:
    def __init__(self, name: str, surname: str, year: str, gender: str, phone: str, bank_id: int):
        self.name: str = name
        self.surname: str = surname
        self.year: str = year
        self.gender: str = gender
        self.phone: str = phone
        self.bank_id: int = bank_id

        self.auth()

    def auth(self):
        self.year = (datetime.now() - datetime.strptime(self.year, '%d/%m/%Y')).days / 365.2425
        if int(self.year) >= 18:
            print('Вам доступен кредит на 1000$, делаем пересчёт на вашу валюту!')
            self.credit()
        else:
            print('Вам нет 18 лет и не можете получить доступ к нашим услугам')

    def credit(self):
        locations = {"48": [3.9, "zł"], "49": [0.88, '€']}
        geo = self.phone[:2]

        coefficient: float = locations[geo][0]
        valuta: str = locations[geo][1]
        money = coefficient * 1000
        info: str = self.get_info(money, valuta)
        print(info)

    def get_info(self, money: float, valuta: str) -> str:
        return f'{self.name} {self.surname}, вам доступен кредит {int(money)}{valuta}\n'

    def __repr__(self):
        return f'Person({self.name}, {self.gender})'


class Generator:
    def __init__(self):

        self.names: dict = {
            0: ["Samuel", "Jack", "Joseph", "Harry", "Alfie", "Jacob", "Thomas"],
            1: ["Alana", "Alex", "Cynthia", "Scarlett", "Emma", "Jenna", "Gabriel"]
        }
        self.surnames: list = ["Smith", "Brown", "Young", "Lewis", "Davis", "Harris", "Walker"]
        self.genders: list = ['male', 'female']
        self.generator()

    def generate_single(self):
        gen: int = random.randint(0, 1)
        return gen

    def generate_phone(self):
        phone = ""
        location: dict = {"48": ["55", "32", "85"], "49": ["5237", "7166"]}
        country = random.choice(list(location))
        city: str = f"{random.choice(location[country])}"
        phone += f"{country}{city}"
        while len(phone) < 10:
            phone += str(random.randint(0, 9))
        return phone

    def generator(self):
        gender: str = self.genders[self.generate_single()]
        name: str = random.choice(self.names[self.generate_single()])
        surname: str = random.choice(self.surnames)
        while True:
            try:
                self.year: str = f"{random.randint(1, 30)}/{random.randint(1, 12)}/{random.randint(1900, 2022)}"
                check = (datetime.now() - datetime.strptime(self.year, '%d/%m/%Y')).days / 365.2425
                break
            except ValueError:
                continue
        phone = self.generate_phone()
        id = random.randint(9999, 20000000)
        return Person(name, surname, self.year, gender, phone, id)

    def generate_1000(self) -> list:
        plist = list()
        for i in range(1000):
            plist.append(self.generator())
        return plist

    def generate_10000(self) -> list:
        plist = list()
        [plist.append(self.generator()) for i in range(10000)]
        return plist


if __name__ == '__main__':
    g = Generator()
    g.generate_1000()
    g.generate_10000()


