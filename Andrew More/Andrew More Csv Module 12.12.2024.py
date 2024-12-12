import csv

data = [
    {
        "name":"Andrew",
        "email":"Andrew@gmail.com",
        "message":"Hola!"
    },
    {
        "name":"Andrew2",
        "email":"Andrew2@gmail.com",
        "message":"Bonjour!"
    }
]

with open("feedback.csv","w",newline='') as f:
    cols = ['name', 'email', 'message']
    writer = csv.DictWriter(f,cols)
    writer.writeheader()
    writer.writerows(data)