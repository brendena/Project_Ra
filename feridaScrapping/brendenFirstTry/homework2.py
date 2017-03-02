# -*- coding: utf-8 -*-
from homework2Functions import MyFunctions
from PandaGraphingWrapper import PandasGraphingWrapper as PGW
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

'''
TODO
    I should definitly check the slack online
    

    I should probable delete all the data points that don't have enough information Row
    
    So i guess i'm going to have to do all the
    notebook stuff at home becuase it just not working
        makes the graphs and see how that works
    

    I think i have to make sure that sure i have a index for this to work.            

'''

'''

myFunctions.deleteColumn(["date_of_birth"])
myFunctions.printLenColumns()

myFunctions.convertUnknownToNull()


myFunctions.columnNotEnoughDataPoints()
myFunctions.deleteColumnsAllSame()
myFunctions.moveAFullDataPointToTop()
myFunctions.printLenColumns()

myFunctions.fillMissingData()

myFunctions.createOutputCSVFile()
#'''

pd.options.display.mpl_style = 'default'
'''
myFunctions = MyFunctions("test.csv", "test.csv")
a = myFunctions.getDataFrameColumn("baths").value_counts()
print(a)
print(a.index)
a.plot(kind="bar")
#a.hist()
#a.boxplot()
print(a.describe())



#dtypes to get data type
'''
myFunctions = MyFunctions("test.csv", "test.csv")
print()
data = myFunctions.DataSet
#print(data["creadit_rating"])
#print(data.groupby(["gender", "occupation"]).count())
#print(data.groupby(["gender"]).get_group("Male")["credit_rating"])
groupMale = data.groupby(["gender"]).get_group("Male")["credit_rating"]
groupFemale = data.groupby(["gender"]).get_group("Female")["credit_rating"]
all = pd.DataFrame({"male ":groupMale, 
                                  "female": groupFemale
                                })
#all.plot.box()')
#all.plot(kind='bar')
groupMale = data.groupby(["gender"]).get_group("Male")["baths"].value_counts()
groupFemale = data.groupby(["gender"]).get_group("Female")["baths"].value_counts()
print(groupMale)


all = pd.DataFrame({"male ":groupMale, 
                                  "female": groupFemale
                                })
                                
all.plot(kind="bar")
#asdf= data.groupby(["baths"]).count()
#print(groupFemale)
'''
#there a parse date attribute
#sales=pd.read_csv("sample-salesv2.csv",parse_dates=['date'])



#very cool you can copu the number of repeat instance
#by a certain attribute
#test = data.groupby("age").count()
#test["age"].clip_lower(40)
#print(test["age"])
#print(data.head())
print("end")


#print(data["bank_card_individual"] == "t")
'''
plt.show(block=True)
