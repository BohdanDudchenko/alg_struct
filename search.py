import math
import random

from Structures import DynamiqueArray, Generator
from main import Person

class StepSearch(DynamiqueArray):
    def __init__(self):
        super(DynamiqueArray, self).__init__()

    def find_cl(self, value: Person) -> [int, None]:
        step = math.floor(math.sqrt(self.length))
        k1 = 0
        k2 = step
        while True:
            if k1 >= self.length:
                return None
            print(value)
            print(self.array)
            if value < self.array[0]:
                return None
            elif value == self.array[0]:
                return k2
            if value == self.array[k2]:
                return k2
            elif value < self.array[k2]:
                a = k2
                while a != k1:
                    a -= 1
                    if value == self.array[a]:
                        return a
            k1 += step
            if self.array[k2 + step] is None:
                k2 = self.length - 1
            else:
                k2 += step

    def find_by_val(self, value: object) -> [list, None]:
        list_of_keys = []
        if value in ["Samuel", "Jack", "Joseph", "Harry", "Alfie", "Jacob", "Thomas"]:
            for key in range(self.length):
                if value == self.array[key].name:
                    list_of_keys.append(key)
        if value in ["Alana", "Alex", "Cynthia", "Scarlett", "Emma", "Jenna", "Gabriel"]:
            for key in range(self.length):
                if value == self.array[key].name:
                    list_of_keys.append(key)
        if value in ["Smith", "Brown", "Young", "Lewis", "Davis", "Harris", "Walker"]:
            for key in range(self.length):
                if value == self.array[key].surname:
                    list_of_keys.append(key)
        if value in ['male', 'female']:
            for key in range(self.length):
                if value == self.array[key].gender:
                    list_of_keys.append(key)
        if list_of_keys == []:
            return None
        else:
            return list_of_keys


g = Generator()
f1 = StepSearch()
print("Testing find class")
f1.add(g.generate_single())
f1.add(g.generate_single())
f1.add(g.generate_single())
f1.add(g.generate_single())
f1.add(g.generate_single())
f1.add(g.generate_single())
print("Creating list of correct and incorrect values")
sm_l = []
for key in range(f1.length):
    sm_l.append(f1.array[key])
for el in range(6):
    sm_l.append(g.generate_single())
print("10 attempts of finding in array some random elements from the list")
n = 1
print(sm_l)
while n <= 10:
    print(f1.find_cl(random.choice(sm_l)))
    n += 1
print("Testing find attribute")
f1.add(g.generate_single())
f1.add(g.generate_single())
f1.add(g.generate_single())
print("Creating list of all values of attributes")
attr_l = [["Samuel", "Jack", "Joseph", "Harry", "Alfie", "Jacob", "Thomas", "Alana", "Alex", "Cynthia", "Scarlett", "Emma", "Jenna", "Gabriel"], ["Smith", "Brown", "Young", "Lewis", "Davis", "Harris", "Walker"], ['male', 'female']]
for attr in range(6):
    a = random.choice(attr_l[attr])
    print(f"{a} --- {f1.find_by_val(a)}")
