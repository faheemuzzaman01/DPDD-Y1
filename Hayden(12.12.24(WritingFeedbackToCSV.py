# import csv

# feedback_data = [
#     {
#         "name":"hayden",
#         "email":"21.hayden.scott@gmail.com",
#         "message":"Woah Cool Feedback"
#     },
#     {
#         "name":"tom",
#         "email":"21.tom.surname@gmail.com",
#         "message":"This is not cool feedback"
#     },
#     {
#         "name":input("What is your name? "),
#         "email":input("Please write down your email adress "),
#         "message":input("Do you have any comments? ")
#     },
# ]

# with open("Feedback.csv", "a",newline="") as file:
#     cols = ["name","email","message"]
#     writer = csv.DictWriter(file,cols)
#     writer.writeheader()
#     writer.writerows(feedback_data)


import pandas as pd
import numpy as np

# DF01 = pd.DataFrame({
#     "name":["hayden","tom","jerry"],
#     "email":["s2282047@students.ncl-coll.ac.uk","placeholder@gmail.com","nonexisting@outlook.com"],
#     "age":["16","17","999"],
#     "phone":["1234567890","8430562935","35427689534678"],
#     "country":["UK","USA","Jordan"]
# })

# s1 = pd.Series[10,20,30,40,50]
# s2 = pd.Series[5,15,25,35,45]
# added = s1 + s2
# print(added)

# week1 = pd.Series([2,5,7,3,9,5,10])
# week2 = pd.Series([2,5,7,3,9,5,10])
# week3 = pd.Series([2,5,7,3,9,5,10])
# week4 = pd.Series([2,5,7,3,9,5,10])
# result = week1 + week2 + week3 + week4
# print(sum(result))

# week01 = [1,2,3,4,5,6,7]
# week02 = [1,2,3,4,5,6,7]
# week03 = [1,2,3,4,5,6,7]
# week04 = [1,2,3,4,5,6,7]
# total = week01 +week02+week03+week04

# df = pd.read_csv("Files To Read\\programming.csv", header=None, names=['Customer ID'])
# print(df.head())

# df = pd.read_csv("Files To Read\\programming.csv")
# print(df.loc[0:2])

# df = pd.read_csv("Files To Read\\programming.csv")
# print(df.loc[0:2, ["Customer Id", "Last Name"]])

# df = pd.read_csv("Files To Read\\programming.csv")
# print(df.index)
# print(df.columns)
# print(df.values)


df = pd.read_csv("Files to Read\\manipulating.csv")
# print(df)
# print(df.columns)
# print(df.loc[2])

df1 = pd.read_csv("Files to Read\\manipulating_with_missing.csv")
dropped_df = df1.dropna()
print(dropped_df)
filled_df = df1.fillna(0)
print(filled_df)
print(df.isnull())