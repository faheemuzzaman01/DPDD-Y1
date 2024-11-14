def process(text):
    print(text)

try:
    with open("Andrew More Image.jpg", "rb") as file:
        while chunk := file.read(1024):
            process(chunk)
except FileNotFoundError:
    print("File not found!")
