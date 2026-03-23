# Practical No: 10
# Lab Assignment-1:
# Create a Panda Dataframe script by reading a file "books.csv". The "books.csv" contains information regarding the books such as title, name of author, edition, publication year and publishing house, price. Create an application to perform the following operations:
# a) Print the complete report of books in a Tabular form.
# b) Print the list of available books of a given author
# c) Print the list of available books of a given publishing house
# d) Print the Titles of cheapest & costliest book available
# e) Print the list by sorting based on the year of publication

import pandas as pd

df = pd.read_csv("books.csv")

print(df)

author = input("Enter author: ")
print(df[df["author"] == author])

pub = input("Enter publisher: ")
print(df[df["publishing_house"] == pub])

print(df[df["price"] == df["price"].min()]["title"])
print(df[df["price"] == df["price"].max()]["title"])

print(df.sort_values("publication_year"))





# Practical No: 10
# Lab Assignment-2:
# Create a table showing information about 5 states such as:
# a) Name of the state
# b) Area
# c) Population
# Generate the following reports:
# a) Print the complete information of states
# b) Print the name of the State having largest Area
# c) Print the name of State having largest population
# d) Create a mechanism to calculate the population density of States
# e) Determine the name of State with highest population density

import pandas as pd

data = {
    "state": ["A", "B", "C", "D", "E"],
    "area": [1000, 2000, 1500, 1800, 1200],
    "population": [50000, 80000, 60000, 90000, 70000]
}

df = pd.DataFrame(data)

print(df)

print(df.loc[df["area"].idxmax()]["state"])

print(df.loc[df["population"].idxmax()]["state"])

df["density"] = df["population"] / df["area"]

print(df)

print(df.loc[df["density"].idxmax()]["state"])