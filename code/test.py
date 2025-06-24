import pandas as pd

print("Hello World!")
print("The world needs pandas!")

housingdat = pd.read_csv('../data/king_county_houses_aa.csv')

print(housingdat.head())
print("Hello World!")


print("Now that I have direct access, I can just do what I want, harharharhar")

print("Check the dataset", housingdat.head(10))
