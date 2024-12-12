import pandas as pd
import numpy as np
# list1=[1,2,3,4,5]
# list2=[1,2,3,4,5]
# running=True
# i=0
# while running:
#     try:
#         print(list1[i] + list2[i])
#     except IndexError:
#         running=False
#     i+=1

# df=pd.read_csv(r"D:\vscode work\Programming\customers-100.csv", header=None, names=["Customer Id"])
# print(df)



df=pd.read_csv(r"D:\vscode work\Programming\file_csv.csv")
print(df)
print(df["name"].values)
print(df.loc[0:1])
