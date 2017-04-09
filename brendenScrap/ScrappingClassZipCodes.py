from random import uniform 
#from Render import SoupJSRender
from Render import JSRender
import csv
import pickle
import json

class ScrappingClassZipCode:
    def __init__(self):
        print("nothing yet")
        self.data = []
        self.JSRender = JSRender()
        self.cvsFile = "googleSunRoofData.csv"
        self.f = open(self.cvsFile, 'w')
        self.allData = []


    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        loop through a a lot of urls

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

    def loopThroughAllAddress(self):

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
        zipCodeInfo["town"] = town
        zipCodeInfo["zip_code"] = zipCode
        self.allData.append(zipCodeInfo)
        


            
        
            
