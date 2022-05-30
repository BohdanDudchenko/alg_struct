import re
from main import Generator, Person
import ephem


def test_person():
    p = Person('some', 'example', '10/10/1990', 'male', "48493939449", 2342312312)
    assert p.name == 'some'
    assert p.surname == 'example'
    assert p.gender == 'male'
    assert re.search('(.+?) ', str(ephem.Date(p.year))).groups()[0] == '1900/2/1'


def test_person_full():
    p = Person('some', 'example', '10/10/2000', 'female', "48493939449", 2342312312)
    assert p.name == 'some'
    assert p.surname == 'example'
    assert p.gender == 'female'
    assert re.search('(.+?) ', str(ephem.Date(p.year))).groups()[0] == '1900/1/22'


def test_person_getinfo():
    p = Person('some', 'example', '10/10/1990', 'female', "48493939449", 2342312312)
    assert isinstance(p.get_info(123123, "valuta"), str)


def test_gen_1000_type():
    g = Generator()
    plist = g.generate_1000()
    assert isinstance(plist, list)
    assert isinstance(plist[0], Person)
    assert len(plist) == 1000


def test_gen_10_000_type():
    g = Generator()
    plist = g.generate_10000()
    assert isinstance(plist, list)
    assert isinstance(plist[0], Person)
    assert len(plist) == 10000