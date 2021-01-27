import requests
from bs4 import BeautifulSoup
import pandas

'''this is a test program to make web scrapper from cached real estate website for learning purposes. BeautifulSoup and request libraries will be used'''

base_url = 'http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/'
page_ext = 't=0&s='

html_content = requests.get(base_url, headers = {'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64l rv:61.0) Gecko/20100101 Firefox/61.0'})

#print(html_content)
#print(str(html_content) == '<Response [200]>')
content = None
if str(html_content) != '<Response [200]>':
    print('ERROR - connection to: ' + base_url + ' did not worked!')
else:
    content = BeautifulSoup(html_content.text, 'html.parser')

#print(content.prettify())
page_nums = content.find_all('a',{'class':'Page'})
max_pages = page_nums[-1].text
print(max_pages)
