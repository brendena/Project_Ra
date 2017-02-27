from bs4 import BeautifulSoup
from urllib import request 
import matplotlib.pyplot as plt 
from pylab import pie
from random import uniform 
#from Render import SoupJSRender
from Render import JSRender
import csv
import time
import pickle
import sys
import json

class ScrappingClass:
    def __init__(self):
        print("nothing yet")
        self.data = []
        self.JSRender = JSRender()
        self.cvsFile = "googleSunRoofData.csv"
        self.f = open(self.cvsFile, 'w')
        self.allData = []

        
  
    def searchURL(self, place,typeAddress="address"):
        #address = "15 Glendale Ave, Somerville, MA 02144, USA"
        #"112 Stanley St, Redwood City, CA 94062, USA"
        #url = "https://www.google.com/get/sunroof#a=15%20Glendale%20Ave,%20Somerville,%20MA%2002144,%20USA&b=150&f=lease&np=28&p=1&sh=1"
        '''
        hours
        so there a dive with class=_Ysh
        and there a span that holds all actuall numberPages

        number of possible feet solar panels
        It has the same structor as above.  
        a class with _Ysh and a span underneath it.

        '''
        if(typeAddress=="address"):
            url = "https://www.google.com/get/sunroof#a="
            print(url + place + "&p=1")
            return url + place + "&p=1" 
        elif(typeAddress=="place"):
            url = "https://www.google.com/get/sunroof/data-explorer/"
            #print(url + place + "&p=1")
            return url #url + place + "&p=1" 

        
                
    #second functions
    def getPagesInfo(self,place,typeAddress="address"):
        url= self.searchURL(place,typeAddress)
        print(typeAddress)
        if(typeAddress == "address"):
            #i can get the spans they just don't have any information in them
            self.JSRender.getAddressPageInfo(url)
            

        elif(typeAddress == "place"):
            print("hi")
            info = self.JSRender.getZipCodePageInfo(url)
            aList = []
            aList.append(info)
            aList.append(info)
            f = open('workfile.csv', 'w+')
            output = csv.writer(f)
            output = csv.writer(f)
            output.writerow(aList[0].keys())

            for row in aList:
                output.writerow(row.values())

    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        loop through a a lot of urls

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

    def loopThroughAllAddress(self, address):
        loop = [
            #{"address":"15 Glendale Ave, Somerville, MA 02144, USA", "typeAddress":"address"},            
        ]

        output = csv.writer(self.f)

        with open('listPlacesScrape.json') as data_file:
            data = json.load(data_file)
        for region in data:
            for zipCode in data[region]:
                self.getZipCodeInfo(region,zipCode["zipCode"],zipCode["url"])
            


        count = 0
        output = csv.writer(self.f)
        for i in self.allData:
            if(count == 0 ):
                header = i.keys()
                output.writerow(header)
                count = 1
            output.writerow(i.values())

        print("done")

    def getZipCodeInfo(self,town,zipCode,url):
        zipCodeInfo = self.JSRender.getZipCodePageInfo(url)
        #if(self.f.stat("file").st_size == 0):
        #    output.writerow(aList[0].keys())

        zipCodeInfo["town"] = town
        zipCodeInfo["zip_code"] = zipCode
        self.allData.append(zipCodeInfo)
        


            
        
            


    
    #load the saved data
    def loadState(self, state):
        return pickle.load( open( "./" + state + ".pickle", "rb" ) )
