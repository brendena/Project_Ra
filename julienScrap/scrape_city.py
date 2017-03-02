from lxml import html
import requests
import time
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

avg_rates, com_rates, res_rates, ind_rates = [], [], [], []
cities = {'houston':'texas',
          'albany':'new-york',
          'new-york':'new-york',
          'tampa':'florida',
          'seattle':'washington',
          'milwaukee':'wisconsin',
          'los-angeles':'california',
          'portland':'maine'
          }
          
# creates custom url using city and state strings
def createURL(state,city):
    return "https://www.electricitylocal.com/states/" + state + "/" + city + "/"

# cleans rate string to only bet the number
def getMoney(string):
    #print('debug: converting string -> ',string)
    newString = string.replace('¢/kWh.','')
    return float(newString)

# scrapes data from page and stores in arrays
def scrapePage(url):
    page = requests.get(page_url)
    tree = html.fromstring(page.content)
    values = tree.xpath('//ul[@class="no2"]/li/strong/text()')
    rateCom, rateRes, rateInd = getMoney(values[0]), getMoney(values[3]), getMoney(values[6])
    avgRate = (rateCom + rateRes + rateInd) / 3
    com_rates.append(format(rateCom, '.2f'))
    res_rates.append(format(rateRes, '.2f'))
    ind_rates.append(format(rateInd, '.2f'))
    avg_rates.append(format(avgRate, '.2f'))

# Create table of data
def createTable():
    table_data = []
    table_data.append(['City', 'Commercial Rate', 'Residential Rate', 'Industrial Rate' , 'Average Rate'])
    index = 0
    for city in cities:
        city_state = city.capitalize() + ', ' + cities[city].capitalize()
        city_state.replace('-', ' ')
        table_data.append([city_state, 
                           str(com_rates[index] + ' ¢/kWh'), 
                           str(res_rates[index] + ' ¢/kWh'), 
                           str(ind_rates[index] + ' ¢/kWh'), 
                           str(avg_rates[index] + ' ¢/kWh')
                          ])
        index += 1
    
    # Init a figure
    colorscale = [[0, '#8B5600'],[.5, '#FFEB60'],[1, '#ffffff']]
    figure = FF.create_table(table_data, colorscale=colorscale)
    figure.layout.width=1000
    #figure.layout.update({'title': 'Electricity rates in ¢/kWh'})
    
    # Make text size larger
    for i in range(len(figure.layout.annotations)):
        figure.layout.annotations[i].font.size = 16
    
    py.iplot(figure, filename='electricity-table-rates')

def createGraph():
    city_names = []
    for city in cities:
        name = city.capitalize() + ', ' + cities[city].capitalize()
        name = name.replace('-', ' ')
        city_names.append(name)
    
    trace1 = go.Bar(
                    x = city_names,
                    y = com_rates,
                    name = 'Com Rates'
    )
    trace2 = go.Bar(
                    x = city_names,
                    y = res_rates,
                    name = 'Res Rates'
    )
    trace3 = go.Bar(
                    x = city_names,
                    y = ind_rates,
                    name = 'Ind Rates'
    )
    trace4 = go.Bar(
                    x = city_names,
                    y = avg_rates,
                    name = 'Avg Rates'
    )
    
    data = [trace1, trace2, trace3, trace4]
    layout = go.Layout(
                       barmode = 'group'
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename = 'electricity-bar-rates')
    
########################## MAIN CODE BELOW ##########################
    
for city in cities:
    page_url = createURL(cities[city],city)
    scrapePage(page_url)
    time.sleep(1)
createTable()
createGraph()
