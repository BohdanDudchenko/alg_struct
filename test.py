from main import Generator
from sorting import Sorter
from Structures import List


def test_sort_list_1000_type():
    g = Generator()
    l = List()
    sm_l = g.generate_1000()
    for el in sm_l:
        l.add(el)
    try:
        l.sort()
    except TypeError:
        pass


def test_sort_own_alg_1000_type():
    g = Generator()
    s = Sorter()
    sm_l = g.generate_1000()
    for el in sm_l:
        s.add(el)
    try:
        s.sort()
    except TypeError:
        pass


def test_sort_list_10000_type():
    g = Generator()
    l = List()
    sm_l = g.generate_10000()
    for el in sm_l:
        l.add(el)
    try:
        l.sort()
    except TypeError:
        pass


def test_sort_own_alg_10000_type():
    g = Generator()
    s = Sorter()
    sm_l = g.generate_10000()
    for el in sm_l:
        s.add(el)
    try:
        s.sort()
    except TypeError:
        pass
