'''/////////////////////////////////////////////////////////////////
|   tutoral for Geocoder 
|   http://chrisalbon.com/python/geocoding_and_reverse_geocoding.html
|   get offline zipcodes 
|   http://pythonhosted.org/uszipcode/#by-coordinate
/////////////////////////////////////////////////////////////////'''
from pygeocoder import Geocoder
from pygeocoder import GeocoderError
from random import uniform
import random 
from Render import JSRender
import pandas as pd
from uszipcode import ZipcodeSearchEngine
import time

import pickle
import json
import csv
import os.path
import sys
from pathlib import Path


class ScrappingClassAddress:
    def __init__(self):
        print("nothing yet")
        self.data = []
        self.JSRender = JSRender()
        self.dataFolder = "ferida"
        self.listFerida = json.loads(open(self.dataFolder + "/listFerida.json" ).read())['listFeridaFiles']
        self.ListPlacesCanScrape = json.loads(open("listPlacesScrape.json").read())
        self.search = ZipcodeSearchEngine()
        self.GoogleTimeLog = 0;
        self.keys = ["AIzaSyACVu-9cEH1KkHdnImX7SyZl--7wipuRP4",
                     "AIzaSyDGVCEUtFSRp7WZ6UgmzWfBeOAF3iiw_hc",
                     "AIzaSyAvQMM_9jGdFq7u2nBcNu5jxIXE4HUfa_A",
                     "AIzaSyCkea01k1qu4r9rGVzbkh29MMKGSt6mBgE",
                     "AIzaSyDt8KzzEJk4UDrBXS8kHwhQREhfoWFNdWA"]
        
  
    def searchURL(self, address):
        #address = "15 Glendale Ave, Somerville, MA 02144, USA"
        #"112 Stanley St, Redwood City, CA 94062, USA"
        #url = "https://www.google.com/get/sunroof#a=15%20Glendale%20Ave,%20Somerville,%20MA%2002144,%20USA&b=150&f=lease&np=28&p=1&sh=1"

        url = "https://www.google.com/get/sunroof#a="
        #print(url + str(address) + "&p=1")
        return url + str(address) + "&p=1" 
        
                


    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        loop through a a lot of urls

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

    def loopThroughAllAddress(self):

        for fileName in self.listFerida:
            print("./" + self.dataFolder + "/" + fileName)                      #speeds up things a lot and uses less memory
            baseFile = "./" + self.dataFolder + "/" + fileName
            df = pd.read_csv(baseFile + ".csv", usecols=['id','latitude','longitude'])

            
            #if file exists - add
            if(Path(baseFile + "Updated.csv").is_file()):
                tmp = pd.read_csv(baseFile + "Updated.csv")
                startingPoint = tmp["id"].count()
                self.csvFile = open(baseFile+ "Updated.csv",'a')
                self.output = csv.writer(self.csvFile)
                
            #if file doesn't - start fresh
            else:
                self.csvFile = open(baseFile+ "Updated.csv",'w+')
                self.output = csv.writer(self.csvFile)
                self.output.writerow(["id","hoursSun","sqFtRoof"])
                startingPoint = 0

            zipCodes = []
            for i in range(0,len(self.ListPlacesCanScrape[fileName])):
                zipCodes.append(int(self.ListPlacesCanScrape[fileName][i]["zipCode"]))

            print("totalNumber ",df["id"].count())

            count = df["id"].count()
            
            for i in range(startingPoint,count): #range(0,200): 
                print(i," / ", count)
                self.loopLogic(df.iloc[i],zipCodes)
                                    #there something wrong with the iloc
                                    #it doesn't look right when you take the lat and longtidue out
                


    def loopLogic(self,datapoint,zipCodes):
        lat = datapoint['latitude']
        lng = datapoint['longitude']
        ID = datapoint['id']
        
        offlineCheck = self.offlineZipCodeCheck(lat,lng,zipCodes)
        
        if(offlineCheck != 0 ):
            
            address = self.googleGetZipCode(lat,lng,zipCodes)

            if(address != 0):
                self.getZipCodeData(address,ID)
            else:
                self.output.writerow([ID, 0, 0])
        else:
            self.output.writerow([ID, 0, 0])

        self.csvFile.flush()
        

    def getZipCodeData(self,address,ID):
        url = self.searchURL(address)
        data = self.JSRender.getAddressPageInfo(url)
        data["id"] = ID
        self.output.writerow([data["id"], data["hoursSun"], data["sqFtRoof"]])

        
    def googleGetZipCode(self,latitude, longitude,zipCodes):
        count = 0
        if(time.time() - self.GoogleTimeLog   < .5):
            time.sleep(1)
        self.GoogleTimeLog = time.time()
        while(True):
            try:
                address = Geocoder(random.choice(self.keys)).reverse_geocode(latitude, longitude)
                break 
            except GeocoderError as GeoError:
                print(GeoError)
                count = count + 1
                time.sleep(10)
                if(count > 3):
                    sys.exit()

        if(address.postal_code is not None and 
            int(address.postal_code) in zipCodes):

            return address 
        else:
            return 0
    def offlineZipCodeCheck(self,latitude, longitude,zipCodes):
        zipCode = self.search.by_coordinate(latitude, longitude, radius=2,returns=2)
        if(len(zipCode) == 0):
            return 2
        else:
            zP = zipCode[0]["Zipcode"]
            if(int(zP) in zipCodes):
                return 1
            else:
                return 0
        