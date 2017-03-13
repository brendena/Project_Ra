import pandas as pd

data = pd.read_csv( "./ferida/Albany.csv")


print("Albany")
print(data['state'].value_counts())

data.groupby(["state"]).get_group("NY").to_csv("NY_Albany.csv")

data.groupby(["state"]).get_group("GA").to_csv("GA_Albany.csv")

data.groupby(["state"]).get_group("OR").to_csv("OR_Albany.csv")

data.groupby(["state"]).get_group("CA").to_csv("CA_Albany.csv")


data = pd.read_csv( "./ferida/TampaHouses.csv")

print("\n\n tamps houses")
print(data['state'].value_counts())


data.groupby(["state"]).get_group("FL").to_csv("FL_Tampa.csv")

            