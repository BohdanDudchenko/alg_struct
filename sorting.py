import random

from main import Generator
from Structures import DynamiqueArray


class Sorter(DynamiqueArray):

    def __init__(self):
        super(DynamiqueArray, self).__init__()

    def sort(self) -> bool:
        if self.length in range(2):
            return False
        a = self.array
        k = 0
        b = 1
        l = self.length - 1
        while True:
            i = k
            j = b
            while a[j]:
                x = a[i]
                a[i] = a[j]
                a[j] = x
                i -= 1
                j -= 1
                if i == -1 or j == 0:
                    break
            k += 1
            b += 1
            if b > l:
                break
        return True

    def sort_by(self, value: str) -> bool:
        i = 0
        j = 1
        a = self.array

        if self.length in range(2):
            return False
        try:
            getattr(a[0], value)
        except AttributeError:
            return False

        while True:
            b = j
            pos = j
            min = a[b]
            while True:
                b += 1
                if b > self.length - 1:
                    break
                if getattr(min, value) > getattr(a[b], value):
                    min = a[b]
                    pos = b
            if getattr(a[i], value) > getattr(min, value):
                a[pos] = a[i]
                a[i] = min
            else:
                pass
            i += 1
            j += 1
            if j > self.length - 1:
                break
        return  True

g = Generator()
s1 = Sorter()
s2 = Sorter()

print("Testing .sort()")
s1.add(g.generate_single())
s1.add(g.generate_single())
s1.add(g.generate_single())
s1.add(g.generate_single())
s1.add(g.generate_single())
s1.add(g.generate_single())
s1.add(g.generate_single())
for pos in range(s1.length):
    print(f"{pos} ===> {s1.array[pos]}")
print("\nSorting...\n")
s1.sort()
for pos in range(s1.length):
    print(f"{pos} ===> {s1.array[pos]}")

print("\nTesting .sort_by(value)")
s2.add(g.generate_single())
s2.add(g.generate_single())
s2.add(g.generate_single())
s2.add(g.generate_single())
s2.add(g.generate_single())
s2.add(g.generate_single())
s2.add(g.generate_single())
for pos in range(s2.length):
    print(f"{pos} ===> {s2.array[pos]}")
print("Creating list of some attributes and random choice from list")
attr = ['name', 'gender']
value = random.choice(attr)
print(f"Sorting by... {value}")
s2.sort_by(value)
for pos in range(s2.length):
    print(f"{pos} ===> {s2.array[pos]}")
