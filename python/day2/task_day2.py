#task1
# Calculator.py

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b 

print(add(7,8))
print(sub(4,5))
print(mul(9,8))
print(div(3,3))

# Calculator Test

import add
def test_add(a,b):
    assert add(3,4) == 7
def test_sub(a,b):
    assert sub(4,3) == 1
def test_mul(a,b):
    assert mul(5,5) == 25
def test_div(a,b):
    assert div(10,5) == 2
