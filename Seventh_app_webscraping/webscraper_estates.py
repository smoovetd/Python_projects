import requests
from bs4 import BeautifulSoup
import pandas

'''this is a test program to make web scrapper from cached real estate website for learning purposes. BeautifulSoup and request libraries will be used'''

base_url = 'http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/'
page_ext = 't=0&s='
html_ext = '.html'
properties = []

html_content = requests.get(base_url, headers = {'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64l rv:61.0) Gecko/20100101 Firefox/61.0'})

#print(html_content)
#print(str(html_content) == '<Response [200]>')
content = None
if str(html_content) != '<Response [200]>':
    print('ERROR - connection to: ' + base_url + ' did not worked!')
else:
    content = BeautifulSoup(html_content.text, 'html.parser')

#print(content.prettify())
#finding max pages s
page_nums = content.find_all('a',{'class':'Page'})
max_pages = int(page_nums[-1].text)
#print(max_pages)

for crnt_page in range(0, max_pages, 1):
    #print(crnt_page * 10)
    #print(base_url + page_ext + str(crnt_page * 10))
    crnt_page_html = requests.get(base_url + page_ext + str(crnt_page * 10) + html_ext, headers = {'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64l rv:61.0) Gecko/20100101 Firefox/61.0'})
    crnt_page_content = BeautifulSoup(crnt_page_html.text, 'html.parser')
#    print(crnt_content.prettify())

    all_props = crnt_page_content.find_all('div',{'class':'propertyRow'})

    for property in all_props:
        #print(property.find('h4').text)
        crnt_prop = {}
        try:
            crnt_prop['Price'] = property.find('h4',{'class':'propPrice'}).text.strip()
        except:
            crnt_prop['Price'] = None

        try:
            crnt_prop['Address'] = property.find_all('span',{'class':'propAddressCollapse'})[0].text.strip()
        except:
            crnt_prop['Address'] = None

        try:
            crnt_prop['Region'] = property.find_all('span',{'class':'propAddressCollapse'})[1].text.strip()
        except:
            crnt_prop['Region'] = None

        try:
            crnt_prop['Beds'] = property.find('span',{'class':'infoBed'}).text.strip()
        except:
            crnt_prop['Beds'] = None

        try:
            crnt_prop['Baths'] = property.find('span',{'class':'infoValueFullBath'}).text.strip()
        except:
            crnt_prop['Baths'] = None

        try:
            crnt_prop['Area_sqft' ] = property.find('span',{'class':'infoSqFt'}).text.strip()
        except:
            crnt_prop['Area_sqft'] = None

        all_groups = property.find_all('div', {'class':'columnGroup'})
        additional_info = []
        for group in all_groups:
            try:
                feature_group = group.find('span',{'class':'featureGroup'}).text
            except:
                feature_group = None

            try:
                feature_name = ''.join([item.text for item in group.find_all('span',{'class':'featureName'})])
            except:
                feature_name = None

            if feature_group != None and feature_name != None:
                additional_info.append(str(len(additional_info) + 1) + '. ' + feature_group + ': ' + ''.join(feature_name))

        crnt_prop['Additional_info'] = '\n'.join(additional_info)
        properties.append(crnt_prop)


df = pandas.DataFrame(properties)
df.to_csv('test_res.csv')
#print(properties)
#print(df)
