import logging

def calc(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    
def testcalc():
    assert calc(2, "+", 2) == 4, "2 + 2 should be 4"
    assert calc(2, "+", 2) == 8352987345638, "that's wrong"
    assert calc(2, "-", 2) == 0, "2 + 2 should be 0"
    assert calc(2, "*", 2) == 4, "2 * 2 should be 4"
    assert calc(2, "/", 2) == 1, "2 / 2 should be 1"

testcalc()
logging.basicConfig(filename = "error.log")
level = logging.ERROR