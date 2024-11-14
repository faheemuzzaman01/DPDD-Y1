import logging

def add(a, b):
    return a + b

def test_add():
    assert add(2, 52) == 5, ">:("

test_add()

logging.basicConfig(filename = "error.log")
level = logging.ERROR