class GetInfo:
    def __init__(self):
        print("nothing yet")
        self.data = []
        self.largestSize = 0
        self.averagePerState = {}
        #,"IN" ,"OR"
        #tried lower case letter
        #didn't seem to work
        self.listState = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IA","KS","KY",
                          "LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND",
                          "OH","OK","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
        
  
        
    #constructs the url
    def searchURL(self, intiger, state):
        return  ("https://projects.propublica.org/docdollars/query?commit=Search&page=" +
                str(intiger) + 
                "&query=&state=" +
                state +
                "&utf8=%E2%9C%93")
                
    #get the information of a specific state and a specific page
    def getPagesInfo(self, intiger, state):
        url= self.searchURL(intiger,state)
        soup = self.getSoup(url)
        table = soup.find("table", {"class": "sorty"}).find("tbody")

        dictionaryOfStates = {}
        for row in table.findAll('tr'):
            colmn = row.findAll('td')
            name = colmn[0].find("a").get_text().replace("  ", "").replace("\n","")
            job = colmn[0].get_text().replace(name, "").replace("  ", "").replace("\n","")
            #removes the vermont part
            town = colmn[1].find("p").get_text().split(',')[0].replace("  ", "").replace("\n","")
            income = colmn[2].string.replace(",","").replace("$","").replace("  ", "").replace("\n","")
            
            if 'M' in income:
                income = income.replace("M","")
                income = int(income) * 1000000
            
            elif 'K' in income: 
                income = income.replace("K","")
                income = int(income) * 1000
            else:
                income = int(income)
            
            self.data.append({
                'name': name,
                'job': job,
                'town':  town,
                'income': income
            })
            #print(name)
            #print(job)
            #print(town)
            #print(income)

    #loop through all the data of a specific state
    def loopThroughAllState(self, state):
        largestValue = self.getNumberOfPages(state)
        
        print(largestValue)
        print('\n')
        
        for i in range(int(largestValue)):
            #if there a error its going to going
            try:
                self.getPagesInfo(i, state)
            except:
                print("error")
            print(i)
            time.sleep(uniform(2,10))
            
        print("pickling " + state + ".pickle")
        pickleData = {
            'data':self.data,
            'numberPages':largestValue,
            'size': len(self.data)
        }
        
        pickle.dump(pickleData, open(state + ".pickle", "wb+"))
        self.data = []
    
    def getNumberOfPages(self,state):
        url=self.searchURL(1,state)
        page = request.urlopen(url)
        soup = BeautifulSoup(page.read(), "lxml")
        table = soup.find("nav", {"class": "pagination"})
        largestValue = 0

        for row in table.findAll("span"):
            if(row['class'][0] == 'next'):
                break
            largestValue = row.get_text()
            
        return largestValue

    def getNumberPeoplePerState(self):
        for state in self.listState:
            print(state)
                                                                    #25 per page
            self.averagePerState[state] = (int(self.getNumberOfPages(state)) *25)
            time.sleep(uniform(1,4))
            
        
            

    #Get the page information
    def getSoup(self, url):
        #http://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
        try:
            page = request.urlopen(url)
        except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop\
            print("exception time out try again")
            time.sleep(30)
            page = request.urlopen(url)
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            print("bad URL")
            print(url)
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            print (e)
            sys.exit(1)
        soup = BeautifulSoup(page.read(), "lxml")
        return soup
    
    #load the saved data
    def loadState(self, state):
        return pickle.load( open( "./" + state + ".pickle", "rb" ) )