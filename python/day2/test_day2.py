# pytest 

from .functions import add_numbers
def test_add_numbers(a,b):
    assert add_numbers(10,30) == 40
