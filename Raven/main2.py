import pandas as pd

feedbackData = pd.DataFrame([
    {
        "Name":"raven",
        "Email":"s2264374@students.ncl-coll.ac.uk",
        "Feedback":"RAHHH!",
        "Age":17
    },
    {
        "Name":"azalea",
        "Email":"s2259223@students.ncl-coll.ac.uk",
        "Feedback":"Undertale is a 2015 2D role-playing video game created by American indie developer Toby Fox.",
        "Age":16
    },
    {
        "Name":"james",
        "Email":"s2304159@students.ncl-coll.ac.uk",
        "Feedback":"weezer.",
        "Age":16
    }
])

s = pd.Series([10, 20, "30", 50])
s2 = pd.Series([10, 20, 30, 50])
listData = [10, 20, "30", 50]

print(s)
print(s2)
print(listData)

print(feedbackData)