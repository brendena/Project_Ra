from selenium import webdriver 
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
        #self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Firefox()
        #i should close this thing
        #driver.close()
        '''
        print(driver.find_element_by_id("content").text) 

        '''
        '''
        try:    
            element = WebDriverWait(driver, 10).until(                       
            EC.presence_of_element_located((By.ID, "loadedButton"))) 
        finally:    
            print(driver.find_element_by_id("content").text)    
            driver.close()
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
        time.sleep(3)
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
        print(returnInfo)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #   if coundn't find anything return 0
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if(returnInfo["hoursSun"] == ''):
            return 0
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
    def getAddressPageInfo(self, url,address):
        self.driver.get(url)
        time.sleep(3)
        bet_fa = self.driver.find_element_by_id("input-0")
        bet_fa.clear()
        #05401
        bet_fa.send_keys("vermont")
        
        print(self.driver.find_element_by_xpath("//input[contains(@id,'input-0')]").get_attribute('value'))

        sectionTag = self.driver.find_element_by_tag_name("section")        
        inputField = sectionTag.find_element_by_tag_name('md-autocomplete-wrap')
        inputField.click()
        inputField.send_keys(Keys.ARROW_LEFT)
        inputField.send_keys(Keys.ARROW_LEFT)
        inputField.send_keys(Keys.RETURN)
        inputField.submit()
        sectionTag.find_element_by_tag_name("form").submit()
        
        time.sleep(1)
        #asdf.send_keys(Keys.RETURN)
        #bet_fa.send_keys(Keys.RETURN)
        #time.sleep(1)
        ##bet_fa.click()
        #bet_fa.click()
        #bet_fa.send_keys(Keys.ARROW_LEFT)
        #bet_fa.send_keys(Keys.RETURN)
        #bet_fa.send_keys("keysToSend")
        #time.sleep(10)
        #print(self.driver.find_element_by_tag_name('title').text)
        #print(self.driver.current_url)
        '''
        count = 0
        while True:
            count = count + 1
            if count > 40:
                print("timed out")
                print(self.driver.current_url)
                return 
            time.sleep(.5)
            try:
                self.driver.find_element_by_id("input-0")
            except:
                e = sys.exc_info()[0]
                print("error")
                print(e)
                return 
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