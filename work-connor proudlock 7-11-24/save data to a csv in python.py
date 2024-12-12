import csv

data=[
    {"name":"connor",
     "email":"connordasigma@agartha.com",
     "message":"alreet hew"
    }
]

with open(r"D:\vscode work\Programming\csv save data\data.csv", "w", newline="") as csvfile:
    columns=["name","email","message"]
    write=csv.DictWriter(csvfile, columns)
    write.writeheader()
    write.writerows(data)