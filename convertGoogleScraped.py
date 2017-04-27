import pandas as pd
import numpy as np
import re


def convertGoogleScraped(fileLocation):
    #original = pd.read_csv(fileLocation + ".csv",index_col=[0],usecols=["id","hoursSun","sqFtRoof","zipCode"])
    original = pd.read_csv(fileLocation + ".csv",usecols=["hoursSun","sqFtRoof"])
    idValues = pd.read_csv(fileLocation + ".csv",usecols=["id","zipCode"])

    #print(original.columns.to_series().groupby(original.dtypes).groups)

    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    / hoursSun roof are object not int
    / so you have to convert them
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    numbers = re.compile('\d+(?:\.\d+)?')
    #'''
    for i in range(0, len(original)):
        row = original.iloc[i]
        print(i)
        #print(row)
        hoursSun = int(''.join(numbers.findall(str(row["hoursSun"]) )))
        sqFtRoof = int(''.join(numbers.findall(str(row["sqFtRoof"]) )))
        original.iloc[i] = {#"id": row["id"],
                            "hoursSun": hoursSun,
                            "sqFtRoof": sqFtRoof,
                            }
    #'''
    original["sqFtRoof"].apply(pd.to_numeric)
    original["hoursSun"].apply(pd.to_numeric)
    print(original.columns.to_series().groupby(original.dtypes).groups)
    original.head()


    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    / get rid of null values
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    for i in original:
        original.loc[original[i].isin([0]), i] = np.nan

    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /  fill missing values
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    original["hoursSun"] = original["hoursSun"].interpolate(method='linear')
    original.sqFtRoof = original.sqFtRoof.interpolate(method='linear')

    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    / make sure all values are filled
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    print(original["sqFtRoof"].notnull().sum())
    print(original["hoursSun"].notnull().sum())
    print(len(original["hoursSun"]))

    original["id"] = idValues["id"]
    original.set_index(["id"])
    original.to_csv(fileLocation + "2.csv")