'''/////////////////////////////////////////////////////////////////
|   tutoral for Geocoder 
|   http://chrisalbon.com/python/geocoding_and_reverse_geocoding.html
|   get offline zipcodes 
|   http://pythonhosted.org/uszipcode/#by-coordinate
/////////////////////////////////////////////////////////////////'''
from pygeocoder import Geocoder
from random import uniform 
from Render import JSRender
import pandas as pd
from uszipcode import ZipcodeSearchEngine
import pickle
import json
import csv
import os.path


class ScrappingClassAddress:
    def __init__(self):
        print("nothing yet")
        self.data = []
        self.JSRender = JSRender()
        self.dataFolder = "ferida"
        self.listFerida = json.loads(open(self.dataFolder + "/listFerida.json" ).read())['listFeridaFiles']
        self.ListPlacesCanScrape = json.loads(open("listPlacesScrape.json").read())
        self.search = ZipcodeSearchEngine()
        
  
    def searchURL(self, address):
        #address = "15 Glendale Ave, Somerville, MA 02144, USA"
        #"112 Stanley St, Redwood City, CA 94062, USA"
        #url = "https://www.google.com/get/sunroof#a=15%20Glendale%20Ave,%20Somerville,%20MA%2002144,%20USA&b=150&f=lease&np=28&p=1&sh=1"

        url = "https://www.google.com/get/sunroof#a="
        print(url + str(address) + "&p=1")
        return url + str(address) + "&p=1" 
        
                


    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        loop through a a lot of urls

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

    def loopThroughAllAddress(self):

        for fileName in self.listFerida:
            print("./" + self.dataFolder + "/" + fileName)
            df = pd.read_csv("./" + self.dataFolder + "/" + fileName + ".csv")
            output = csv.writer(open("./" + self.dataFolder + "/" + fileName + "Updated.csv",'w'))
            zipCodes = []
            for i in range(0,len(self.ListPlacesCanScrape[fileName])):
                zipCodes.append(int(self.ListPlacesCanScrape[fileName][i]["zipCode"]))

            print("totalNumber ",df["id"].count())

            for i in range(0,5): #range(df["id"].count()): 
                self.loopLogic(output,df.iloc[[i]],zipCodes)
                                    #there something wrong with the iloc
                                    #it doesn't look right when you take the lat and longtidue out
                


    def loopLogic(self,output,datapoint,zipCodes):
        lat = datapoint['latitude']
        lng = datapoint['longitude']
        ID = datapoint['id']
        print(lat)
        print(lng)
        
        #offlineCheck = self.offlineZipCodeCheck(lat,lng,zipCodes)
        '''
        if(offlineCheck != 0 ):
            address = self.googleGetZipCode(lat,lng,zipCodes)
            if(address != 0):
                self.getZipCodeData(output,address,ID)
        else:
            output.writerow()
        '''

    def getZipCodeData(self,output,address,ID):
        url = self.searchURL(address)
        data = self.JSRender.getAddressPageInfo(url)
        data["id"] = ID
        #if(count == 0 ):
        #    header = data.keys()
        #    output.writerow(header)
        #    count = 1
        
        output.writerow(data.values())
    def googleGetZipCode(self,latitude, longitude,zipCodes):
        address = Geocoder.reverse_geocode(latitude, longitude)
        print(address.postal_code)
        if(int(address.postal_code) in zipCodes):
            return 0
        else:
            return address
    def offlineZipCodeCheck(self,latitude, longitude,zipCodes):
        zipCode = self.search.by_coordinate(latitude, longitude, radius=2,returns=2)
        '''
        if(len(zipCode) == 0):
            return 2
        else:
            zP = zipCode[0]["Zipcode"]
            if(int(zP) in zipCodes):
                return 1
            else:
                return 0
        '''