from lxml import html
import requests
import time
import plotly.plotly as py
import pandas as pd

cities = {'houston':'texas',
          'albany':'new-york',
          'new-york':'new-york',
          'tampa':'florida',
          'seattle':'washington',
          'milwaukee':'wisconsin',
          'los-angeles':'california',
          'portland':'maine'
          }
#cities = {'new-york':'new-york'}

# 
def createURL(state,city):
    return "https://www.electricitylocal.com/states/" + state + "/" + city + "/"

# cleans rate string to only bet the number
def getMoney(string):
    #print('debug: converting string -> ',string)
    newString = string.replace('¢/kWh.','')
    return float(newString)

for city in cities:
    page_url = createURL(cities[city],city)
    page = requests.get(page_url)
    tree = html.fromstring(page.content)
    values = tree.xpath('//ul[@class="no2"]/li/strong/text()')
    rateCom, rateRes, rateInd = getMoney(values[0]), getMoney(values[3]), getMoney(values[6])
    avgRate = (rateCom + rateRes + rateInd) / 3
    print(city, " avg rate = ", format(avgRate, '.2f'),'¢/kWh')
    time.sleep(1)