import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # begin=3, end=10: evens 4+6+8+10 = 28
    content = open('result1.txt').read()
    print(content)
    regex_test([r'28'], content)

@pytest.mark.T2
def test_main_2():
    # begin=-5, end=-2: evens -4+(-2) = -6
    content = open('result2.txt').read()
    print(content)
    regex_test([r'-6'], content)

@pytest.mark.T3
def test_main_3():
    # begin=1, end=1: no evens, sum = 0
    content = open('result3.txt').read()
    print(content)
    regex_test([r'\b0\b'], content)

@pytest.mark.T4
def test_main_4():
    # begin=2, end=12: evens 2+4+6+8+10+12 = 42
    content = open('result4.txt').read()
    print(content)
    regex_test([r'42'], content)
