#
#http://pythonhow.com/data-analysis-with-python-pandas
#complete document
#http://pandas.pydata.org/pandas-docs/stable/10min.html
import pandas as pd
from baseDataframe import BaseDataFrame
import numpy as np
import random

'''------------------------------------------------------
MyFunctions
    Hold all the functions to 
    fill in the missing data points
    
------------------------------------------------------'''

class MyFunctions(BaseDataFrame):
    def __init__(self, input, output):
        BaseDataFrame.__init__(self, input, output)
        #BaseDataFrame.__init__(self, "test.csv", "test.csv")
        print("created class")
        
        
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /   for each type of data it will
    /   fill in the missing data.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def fillMissingData(self):
        #'''
        for i in self.DataSet:
            Type = self.getType(i)[0]
            if(Type is str):
                self.getFrequencyEachSection(i)
            elif(Type is "date"):
                #for ever x in DataSet[i="dateValue"] convert it to a int
                self.DataSet[i] = self.DataSet[i].apply(lambda x: self.convertStringDateToInt(x))
                #fill in data mean
                self.DataSet[i] = self.DataSet[i].interpolate(method='linear')
                self.fillNanWithSum(i)
                #convert it back to a string
                self.DataSet[i] = self.DataSet[i].apply(lambda x: self.convertIntDateToString(x))
            else:
                self.DataSet[i] = self.DataSet[i].interpolate(method='linear')
                self.fillNanWithSum(i)
                self.DataSet[i] = self.DataSet[i].round(decimals=0)
        #'''

    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        get a dictionary of number that need 
        to be filled pased on the ratio of filled 
        data
        
        Ex. - returnData 
            data = [a:50, c:20: h:100]
            
        To keep the same ratio you need to fill
        in the data with 50 a's and 20 c's and
        100 h's.

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
    
    def numberOfNullsToFill(self, column):
        #get a dataframe of the counts of a column
        countOfCategories = self.DataSet[column].value_counts()
        #get a list of the labels
        listCategories = list(countOfCategories.index)
        #get the number of validPoints from column
        numberOfValidPoints = self.getNumberOfAnswers(column)
        #get number Null values from column
        numberOfNulls = self.getNumberOfNulls(column)
        #inputLists is a dictionary of frequency per item in listCategories
        inputList ={}
        for i in range(0,len(countOfCategories)):
            # (numberInSpecificCategorie / numberOfValidPoints) = ratio * nulls = numberOfNullsToFill
            inputList[listCategories[i]] = float(countOfCategories[i]) / float(numberOfValidPoints) * numberOfNulls
        
        return inputList
    
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /   fill in Nan for catigorical Data.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def getFrequencyEachSection(self, column):
        #**************************************************************
        # -----------------How-Works-----------------------------------
        # it creates a .isNull() array and where the values are true
        # fill it with a catigorical data point.  If false it get a 
        # np.NaN value.  When you do a fill na it will replace all
        
        #**************************************************************
        
        inputList = self.numberOfNullsToFill(column)
        nullTestArray = self.DataSet[column].isnull()
        
        for i in range(0,len(nullTestArray)):
            if(nullTestArray[i] == True):
                if(nullTestArray[i] == True):
                    fillInType = ""
                    
                    #first try a random approach
                    increment = 0
                    rand = random.randrange(0, 1)

                    for categorie in inputList:
                        fillInType = categorie
                        break
                        increment = increment + inputList[categorie]
                        if(rand < increment):
                            if(inputList[categorie] >0):
                                fillInType = categorie
                                print(categorie)
                                inputList[categorie] = inputList[categorie] - 1
                            break
                            
                    #if random fails then just find first input
                    if(fillInType == ""):
                        for categorie in inputList:
                            if(inputList[categorie] > 0):
                                fillInType = categorie
                                inputList[categorie] = inputList[categorie] - 1
                                break  

                    nullTestArray[i] = fillInType            
            else:
                nullTestArray[i] = np.NaN
                
        self.DataSet[column].fillna((nullTestArray), inplace=True)
        
        #**************************************************************
        # technically works but it seemed really slow
        # i think it has to do with the loc function
        '''
        index = 0
        for value in self.DataSet["construction_type"]:
            if(nullTestArray[index] == True):
                fillInType = "ASDF"
                #for categorie in inputList:
                ##    if(inputList[categorie] > 0):
                 #       fillInType = categorie
                 #       inputList[categorie] = inputList[categorie] - 1    
                self.DataSet.loc[index, "construction_type"] = fillInType
            index = index + 1
        #'''
        #**************************************************************
        
        
        
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /   file the data with sum and return None
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def fillNanWithSum(self, column):
        self.DataSet[column].fillna((self.DataSet[column].mean()), inplace=True)
    
    
    
    
    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        converts categorical into int so you 
        can interpolate over them.
    
        Idea for this function was found here.
        http://stackoverflow.com/questions/11975203/better-rounding-in-pythons-numpy-around-rounding-numpy-arrays    
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
    
    
    def interpolateOverCategoricalData(self,column):
        #turn catigorical data to int's
        array, label = column.factorize()
        #turn all the -1 into np.nanimport sys
        array = pd.Series(array).replace(-1, np.nan)
        #interpilates the data
        array = array.interpolate()
        #round possible float to ints and turn into categorical data
        array = array.round(decimals=0).astype('category')
        #add back the labels and then turns it back into string
        array = array.cat.rename_categories(label).astype('str')
        
        return array
    

        
