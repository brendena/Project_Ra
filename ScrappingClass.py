from bs4 import BeautifulSoup
from urllib import request 
import matplotlib.pyplot as plt 
from pylab import pie
from random import uniform 
#from Render import SoupJSRender
from Render import JSRender
import time
import pickle
import sys

class ScrappingClass:
    def __init__(self):
        print("nothing yet")
        self.data = []
        self.JSRender = JSRender()

        
  
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
            self.JSRender.getAddressPageInfo(url,place)
        


    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        loop through a a lot of urls

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

    def loopThroughAllAddress(self, address):
        loop = [
            {"address":"05401", "typeAddress":"place"}
            #{"address":"15 Glendale  USA", "typeAddress":"address"},
            #{"address":"15 Glendale Ave, Somerville, MA 02144, USA", "typeAddress":"address"},
            #{"address":"15 Glendale Ave, Somerville, MA 02144, USA", "typeAddress":"address"},
            #{"address":"15 Glendale Ave, Somerville, MA 02144, USA", "typeAddress":"address"},
            #
            
        ]
        for i in loop:
            self.getPagesInfo(i["address"], i["typeAddress"])
        


            
        
            


    
    #load the saved data
    def loadState(self, state):
        return pickle.load( open( "./" + state + ".pickle", "rb" ) )