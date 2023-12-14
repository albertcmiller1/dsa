import pytest 
from example import sum 

def test_sum():
    assert sum(1, 2) == 3

def test_sum_output_type():
    assert type(sum(1, 2)) is int

@pytest.mark.parametrize('num1, num2, expected', [(3,5,8)])
def test_sum_2(num1, num2, expected):
    assert sum(num1, num2) == expected
