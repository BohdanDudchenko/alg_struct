import re
from datetime import datetime, date
import time
from phonenumbers import geocoder
import phonenumbers


class BankAccount:
    def __init__(self, name, surname, year, gender, phone, bank_id):
        self.name = name
        self.surname = surname
        self.year = year
        self.gender = gender
        self.phone = phone
        self.bank_id = bank_id

        self.auth()

    def auth(self):
        self.year = (datetime.now() - datetime.strptime(self.year, '%d/%m/%Y')).days / 365.2425
        if int(self.year) >= 18:
            print('Вам доступен кредит на 1000$, делаем пересчёт на вашу валюту!')
            self.credit()
        else:
            print('Вам нет 18 лет и не можете получить доступ к нашим услугам')

    def credit(self):
        locations = {"380": [27, "₴"], "48": [3.9, "zł"], "1": [1, '$'], "49": [0.88, '€']}
        geo = re.search(': (.+?) ', str(phonenumbers.parse(self.phone, None))).groups()[0]
        coefficient = locations[geo][0]
        valuta = locations[geo][1]
        money = coefficient * 1000
        self.get_info(money, valuta)

    def get_info(self, money, valuta):
        print(f'{self.name} {self.surname}, вам доступен кредит {int(money)}{valuta}\n')


if __name__ == '__main__':
    person1 = BankAccount('Vitya', 'Leviy', '12/08/2003', 'male', '+48573451360', 2374283)
    person2 = BankAccount('Natasha', 'Britva', '12/08/1998', 'female', '+490984087694', 9823941)
    person3 = BankAccount('Misha', 'Poker', '12/02/2003', 'male', '+380678245673', 1231234)
    person4 = BankAccount('Kolya', 'Poker', '12/08/2005', 'male', '+380984087458', 2281337)


