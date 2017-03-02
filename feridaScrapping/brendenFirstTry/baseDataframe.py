import pandas as pd
import numpy as np
import datetime 
import time
import re

'''------------------------------------------------------
BaseDataFrame
    Holds all the data and all 
    the function needed to 
    remove all the junk  data.
    
    Removes
        -columns with no unique data
        -column that don't have enought data
    
    HelperFunction
        -For printing out basic length of data
        -deleting list of rows
        -reading in cvs file
        -converting time to int
    
------------------------------------------------------'''
class BaseDataFrame():
    
    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    inputFile - a csv file full of data
    outPutFile - a cvs file name
    DataSet - the dataset that 
                    you will be cleaning up
    startingDate - the date that all date will
                    be converting around.
    
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
    def __init__(self,inputFile,outputFile):
        print("created class")
        self.inputFile = inputFile
        self.outPutFile = outputFile
        self.DataSet = self.readInputCSVFILE() # .iloc[0:100,0:40]
        self.startingDate = datetime.datetime(1900, 1, 1)
        
        
        
    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        moves a data point that is almost
        fully complete to the top.  This is 
        helpfull becuase scipi's interpolate
        function only starts when it first
        see a variable.
        
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
    
    def moveAFullDataPointToTop(self):
        fullData = self.DataSet.isnull()
        print('going through')
        for index, row in fullData.iterrows():
            if((row.sum()/len(self.DataSet.columns)) < 0.1):
                '''-------Debug---------
                print("\n sum " + str(row.sum()))
                print(row.sum()/len(self.DataSet))
                print(index)
                print(row)
                #'''
                self.DataSet.iloc[[0,index],:] = self.DataSet.iloc[[index,1],:].values
                break
    
    
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /  Delete all columns that don't have 
    / more the "minimumPercent"
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def columnNotEnoughDataPoints(self):
        minimumPercent = 10
        notEnoughData = []
        numberOfPeopleBelowPercent = self.numberOfPeoplePercent(minimumPercent)
        for i in self.DataSet:
            #sum the True (1) values from a frame that been converted to not null.
            numberPeopleNotNull = self.DataSet[i].notnull().sum()
            if(numberPeopleNotNull <= numberOfPeopleBelowPercent):
                notEnoughData.append(i)
                
        self.deleteColumn(notEnoughData)
    
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /  converts Unknown values to np.nan
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def convertUnknownToNull(self):
        #should remove case senstivity .lower() or something
        unknowns = ["UNKNOWN"]
        for i in self.DataSet:
            #print(self.DataSet[i].isin(unknowns).sum())
            self.DataSet.loc[self.DataSet[i].isin(unknowns), i] = np.nan
                             
                             
    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        So this looks for the first value that's
        not null and then compares that 
        value to everthing in the array.  If
        the data repeat more then "limitingDiverity",
        then you delete it.

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
    
    
    def deleteColumnsAllSame(self):
        limitingDiverity = .99
        noDiversity = []        
        for i in self.DataSet:
            valueType, value = self.getType(i)
            numberOfAnswer = self.getNumberOfAnswers(i);
            if type(value) is np.float64:
                #print("its a int")
                value = "nothing"
            else:
                numberOfRepeating = self.DataSet[i].str.contains(value).sum()
                #(numberOfRepeating / numberOfAnswer) but the value between
                # 0 - 1 so then you can compare it against a percentage.
                if(numberOfRepeating / numberOfAnswer > limitingDiverity):
                    noDiversity.append(i)
                    
        self.deleteColumn(noDiversity)
    
    
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /   return the type and instance 
    /   of the first none null values
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    
    def getType(self,column):
        data = self.DataSet[column].notnull()
        value = np.NAN;
        for j in range(0,len(self.DataSet[column])):
            if(data[j]):
                value = self.DataSet[column][j]
                break;
        valueType = type(value) 
        if(type(value) is str):
            if(re.match('(\d{4})[/.-](\d{2})[/.-](\d{2})$', value) != None):
                valueType = "date"
            
        return valueType, value
    
    
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /   return a int of the number columns 
    /   that had not null values.   
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    
    def getNumberOfAnswers(self,column):
        return self.DataSet[column].notnull().sum()
    
    def getNumberOfNulls(self,column):
        return self.DataSet[column].isnull().sum()
    
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /    convert date to int by taking 
    /    date and subtracting it by 
    /    startingDate.  So its going to 
    /    return number of days from 
    /    startingDate
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    
    def convertStringDateToInt(self,date):
        if(date is not np.NaN):
            return np.intc((datetime.datetime.strptime(date, "%Y-%m-%d") - self.startingDate).days)
        else:
            return np.NaN
    def convertIntDateToString(self,days):
        currentDate = self.startingDate + datetime.timedelta(days=days)
        return str(currentDate.year)+ "-" + str(currentDate.month) + "-" + str(currentDate.day)
    
        #**********************************************
        # future idea
        #    if you need to output things like 10/4/95
        #    print(str(currrentDate.year)[-2:])
        #**********************************************
    
    def getDataFrameColumn(self, column):
        return self.DataSet[column]
    
    def deleteColumn(self, items):
        for i in items:
            del self.DataSet[i]
            
    def getNumberDataPoints(self):
        return len(self.DataSet)
                
    def createOutputCSVFile(self):
        self.DataSet.to_csv('test.csv')
        
    def readInputCSVFILE(self):
        return pd.read_csv(self.inputFile)
    
    def printLenColumns(self):
        print(len(self.DataSet.columns))
        
    def printLenData(self):
        print(self.getNumberDataPoints())
    
    def printColumns(self):
        print(self.DataSet.columns)
    
    def numberOfPeoplePercent(self, number):
        return len(self.DataSet) * (number/100)
