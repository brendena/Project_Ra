'''/////////////////////////////////////////////////////////////////
|   tutoral for Geocoder 
|   http://chrisalbon.com/python/geocoding_and_reverse_geocoding.html
/////////////////////////////////////////////////////////////////'''
from pygeocoder import Geocoder
from random import uniform 
from Render import JSRender
import pandas as pd
import pickle
import json
import csv

class ScrappingClassAddress:
    def __init__(self):
        print("nothing yet")
        self.data = []
        self.JSRender = JSRender()
        self.dataFolder = "ferida"
        self.listFerida = json.loads(open(self.dataFolder + "/listFerida.json" ).read())['listFeridaFiles']

        
  
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
            
            count = 0
            for i in range(5):
                address = Geocoder.reverse_geocode(df['latitude'][i], df['longitude'][i])
                url = self.searchURL(address)
                data = self.JSRender.getAddressPageInfo(url)
                data["id"] = df['id'][i]
                if(count == 0 ):
                    header = data.keys()
                    output.writerow(header)
                    count = 1
                
                output.writerow(data.values())
        

