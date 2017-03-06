from selenium import webdriver 
import selenium 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import sys
import time
'''
    install 

        https://gist.github.com/julionc/7476620

    use node to phantomjs

        http://stackoverflow.com/questions/36770303/phantomjs-with-selenium-unable-to-load-atom-find-element

    if you want to use firefox or chrome 
    you habe to download the drivers for them

        http://selenium-python.readthedocs.io/installation.html

'''
'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
TODO
    should probable log all the things that didn't work 


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
class JSRender:
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        #self.driver = webdriver.Firefox()
        #i should close this thing
        #driver.close()
        '''
        print(driver.find_element_by_id("content").text) 

        '''


    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        get the info from a singler page on sunroof.

        returns: 
            {
                hoursSun:
                sqFtRoof
            }
        returns: bad getAddress 
            return 0

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
    def getAddressPageInfo(self, url):
        self.driver.get(url)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #   wait 3 seconds to allow the page 
        #   to render and gather its content
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        count = 0
        sleepTime = .2
        while(True):
            if(count < 20):
                text = self.driver.find_element(By.XPATH, '//li[@class="_Vsh"]//div[@class="_Ysh"]//span').text
                if(text != ""):
                    break

                time.sleep(sleepTime)
                count = count + 1
                
            else:
                print("there was a error")
                break


        results = self.driver.page_source
        soup = BeautifulSoup(results, "lxml")
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #   both hoursSun and sqFtRoof have parent
        #   li with class _Vsh and the number is 
        #   in a span tag.
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        info = soup.findAll("li", {"class": "_Vsh"})
        returnInfo = {
            "hoursSun": info[0].find("span").get_text(),
            "sqFtRoof": info[1].find("span").get_text()
        }
        #print(returnInfo)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #   if coundn't find anything return 0
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if(returnInfo["hoursSun"] == ''):
            return {
                "hoursSun": "0",
                "sqFtRoof": "0" 
            }
        else:
            return returnInfo

    '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        
        
        
        
        Resources:

        How to click in selenium

            http://stackoverflow.com/questions/21350605/python-selenium-click-on-button

        How to input values for inputs tags

            http://stackoverflow.com/questions/28346240/selenium-not-setting-input-field-value

        good example of selenium    

            http://www.marinamele.com/selenium-tutorial-web-scraping-with-selenium-and-python

        large example of selenium

            http://thiagomarzagao.com/2013/11/12/webscraping-with-selenium-part-1/

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
    def getZipCodePageInfo(self, url):
        self.driver.get(url)
        time.sleep(3)
        allData = self.driver.execute_script("return placeDetailsResponseJspb")
        roofTopData = allData[2]
        print(len(roofTopData))
        print(url)
        results = {
            "threshold_viable_sunroof": self.checkExists(roofTopData[0]),
            "roof_viable_total": self.checkExists(roofTopData[1]),
            "roof_solar_viable": self.checkExists(roofTopData[2]),
            "roof_space_total": self.checkExists(roofTopData[3]),
            "roof_space_median": self.checkExists(roofTopData[4]),

            "roof_total_est_flat_roofs": self.checkExists(roofTopData[5][4]),
            "roof_total_est_s_facing": self.checkExists(roofTopData[5][1]),
            "roof_total_est_w_facing": self.checkExists(roofTopData[5][3]),
            "roof_total_est_e_facing": self.checkExists(roofTopData[5][2]),
            "roof_total_est_n_facing": self.checkExists(roofTopData[5][0]),

            "roof_capacity_median": self.checkExists(roofTopData[6]),

            "total_yearl_energy_est_flat_roof": self.checkExists(roofTopData[7][4]),
            "total_yearl_energy_est_flat_roof": self.checkExists(roofTopData[7][1]),
            "total_yearl_energy_est_flat_roof": self.checkExists(roofTopData[7][3]),
            "total_yearl_energy_est_flat_roof": self.checkExists(roofTopData[7][2]),
            "total_yearl_energy_est_flat_roof": self.checkExists(roofTopData[7][0]),


            "roof_energy_median": self.checkExists(roofTopData[8]),
            "potential_co2_saved_all_solar": self.checkExists(roofTopData[9]),
            "potential_car_taken_off_rode_all_solar": self.checkExists(roofTopData[10]),
            "potential_tree_planet_all_solar": self.checkExists(roofTopData[11]),

            "0_to_5_roof_top_capacity_distribution":0,
            "5_to_10_roof_top_capacity_distribution":0,
            "10_to_15_roof_top_capacity_distribution":0,
            "15_to_20_roof_top_capacity_distribution":0,
            "20_to_25_roof_top_capacity_distribution":0,
            "25_to_30_roof_top_capacity_distribution":0,
            "30_to_35_roof_top_capacity_distribution":0,
            "35_to_40_roof_top_capacity_distribution":0,
            "40_to_45_roof_top_capacity_distribution":0,
            "45_to_50_roof_top_capacity_distribution":0,


            "50_to_100_roof_top_capacity_distribution":0,
            "100_to_150_roof_top_capacity_distribution":0,
            "150_to_200_roof_top_capacity_distribution":0,
            "200_to_250_roof_top_capacity_distribution":0,
            "250_to_300_roof_top_capacity_distribution":0,
            "300_to_350_roof_top_capacity_distribution":0,
            "350_to_400_roof_top_capacity_distribution":0,
            "400_to_450_roof_top_capacity_distribution":0,
            "450_to_500_roof_top_capacity_distribution":0,
            "500_to_550_roof_top_capacity_distribution":0,
            "550_to_600_roof_top_capacity_distribution":0,
            "600_to_650_roof_top_capacity_distribution":0,
            "650_to_700_roof_top_capacity_distribution":0,
            "700_to_750_roof_top_capacity_distribution":0,
            "750_to_800_roof_top_capacity_distribution":0,
            "800_to_850_roof_top_capacity_distribution":0,
            "850_to_900_roof_top_capacity_distribution":0,
            "900_to_950_roof_top_capacity_distribution":0,
            "950_to_1000_roof_top_capacity_distribution":0
        }
        #'''
        '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        / load the last graph and all its data
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
        
        #print(len(roofTopData[13]))
        #print(url)
        #'''
        index = 0
        for roof in roofTopData[14]:
            results[str(roof[0]) + "_to_" + str(roof[1]) +"_roof_top_capacity_distribution"] = self.checkExists(roof[2])
            index = index + 1
        index = 0
        for roof in roofTopData[15]:
            results[str(roof[0]) + "_to_" + str(roof[1]) +"_roof_top_capacity_distribution"] = self.checkExists(roof[2])
            index = index + 1
        #'''
        return results

    def checkExists(self,value):
        if(value):
            return value
        else:
            return 0
        #if(value == '' or value == None or value == ""):
        #    return 0
        #else:
        #    return value




'''
        soup = BeautifulSoup(results, "lxml")
        mainContent = soup.find("div",  {"class":"place-card-content"})
        print(mainContent)
        print("\n\n")
        columns = mainContent.find("div",{"class":"place-metrics-columns"}).findAll("div", {"class":"place-metrics-column"})
        print(columns[0].get_text())
        listItems = ["roofs_percent_viable",  "roof_total_number",  "roof_total_space",  "roof_total_capacity", 
                            "roof_total_electricity", "roof_median_space",  "roof_median_capacity",  "roof_meidan_electricity"]
        dict = {}
        count = 0
        for column in columns:
            for cell in column.findAll("div", {"class": "place-metrics-cell-value"}):
                dict[listItems[count]] = cell.get_text()
                count = count + 1
        '''
'''
getting a list of address
do it by zip code   
http://www.melissadata.com/lookups/zipstreet.asp


verify address in bulk
http://www.melissadata.com/lookups/batchaddresscheck.asp

all the data
http://www.melissadata.com/lookups/index.htm


'''
