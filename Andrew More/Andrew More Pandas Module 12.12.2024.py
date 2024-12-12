import pandas as pd

# DF01 = pd.DataFrame({
# 	"name": ["firstname", "secondname", "thridname"],
# 	"age":[1,2,3],
# 	"email":["gmail","outlook","yahoo"],
#     "message":["Wow this is cool!", "I HATE THIS", "Nah"],
#     "gender":["M","F","U"],
#     "phone number":["0","519","3357"]
# })

# print(DF01)

# series01 = pd.Series([10, 20, 30, 50])
# series02 = pd.Series([1,2,3,5])
# seriesmerge = series01 + series02
# print(seriesmerge)

df = pd.read_csv("customers-100.csv", header=None, names=['Customer Id'])

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85, 90, 95]
}
df = pd.DataFrame(data)
print(df.loc[0])
print(df.loc[0:1,["name","Score"]])