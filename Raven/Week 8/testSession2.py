import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)

def add(a, b):
    return a + b

def testAddition():
    try:
        assert add(2, 4) == 5, "Should be 5"    
    except:
        logging.ERROR("The Error for Logs")
        print("The Error for User")

testAddition()
