import csv

feedbackData = [
    {
        "Name":"raven",
        "Email":"s2264374@students.ncl-coll.ac.uk",
        "Feedback":"RAHHH!"
    },
    {
        "Name":"azalea",
        "Email":"s2259223@students.ncl-coll.ac.uk",
        "Feedback":"Undertale is a 2015 2D role-playing video game created by American indie developer Toby Fox."
    },
    {
        "Name":"james",
        "Email":"s2304159@students.ncl-coll.ac.uk",
        "Feedback":"weezer."
    }
]

with open("feedback.csv", "w", newline="") as file:
    cols = ["Name","Email","Feedback"]
    writer = csv.DictWriter(file,cols)
    writer.writeheader()
    writer.writerows(feedbackData)