import pandas
import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets')

content = webpage.content

result = BeautifulSoup(content, 'html.parser')

products = result.find_all('div', {'class' : 'col-md-4 col-xl-4 col-lg-4'})

names = []
links = []
prices = []

for item in products:
    names.append(item.a.string)
    links.append('https://www.webscraper.io' + item.a['href'])
    prices.append(item.h4.string)


data = list(zip(names, links, prices))

d = pandas.DataFrame(data, columns=['Name', 'Link', 'Price'])

try:
    d.to_excel('./Products.xlsx')
except Exception as e:
    print('Something went wrong!!!/n' + e)
else:
    print('Web data successfully written.')
finally:
    print('Quitting the program, bye!!!')