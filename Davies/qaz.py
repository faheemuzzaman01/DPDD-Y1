def input_data():
    name = input("Enter your name: ")
    return name
def process_data(name):
    return name.upper()
def output_data(name):
    print("Hello, " + name + "!")
name = input_data()
name = process_data(name)
output_data(name)
