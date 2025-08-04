import requests
from bs4 import BeautifulSoup
#TO DO
#user input
#write results in file
url = '' #e.g. https://www.youtube.com/shorts/
domain = '' #e.g. https://www.youtube.com
website = requests.get(url) #get the content
website_text = website.text #content in unicode

soup_obj = BeautifulSoup(website_text) # creating Beautifulsoup object

links = []

for link in soup_obj.find_all('a'):
    full_url = domain + str(link)
    if requests.request('GET', full_url) == 200 or requests.request('GET', link) == 200 or requests.request('GET', domain + str(link)) == 200:
        links.append(link.get('href'))

links.sort()
links = set(links)

for link in links:
    print(link)

print('total quantity:', len(links))