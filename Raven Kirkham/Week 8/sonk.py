with open("sonk.jfif", "rb") as file:
    binary_data = file.read()
    print(binary_data)


with open("test.jfif", "wb") as file:
    file.write(binary_data)