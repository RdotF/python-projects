import requests
from bs4 import BeautifulSoup
#TO DO
#filter links - done
#check url - done
def get_links(url):
    links = []
    try:

        website = requests.get(url)
        website_text = website.text
        soup = BeautifulSoup(website_text, features="lxml")

        for link in soup.find_all('a'):
            links.append(link.get('href'))
        links.sort()

    except Exception as e:
        print(f'Something went wrong: {e}')
    return links
def put_links_in_file(links, url):
    try:
        with open('nestedLinks.txt', 'w') as file:
            file.write('ROOTLINK: ' + url+'\n')
            for i in range(len(links)):
                file.write(f'{links[i]}\n')
        file.close()

    except Exception as e:
        print(f'Something went wrong: {e}')
    return 1
def filter_nested_links(links):
    filtered_links = []
    if isinstance(links, list):
        for i in links:
            if '/' in i and len(i) > 1:
                filtered_links.append(i)
        return filtered_links
    else:
        print('wrong parameter got into filtered_nested_links function. Should be a list')



def check_url(url):
    if 'http://' not in url and 'https://' not in url or len(url) <= 8:
        url = 0 #false
    elif not(url[-1] == '/'):
        return url+'/'
    if url == 0:
        print('Wrong link.')
        print('Example of valid link: https://www.youtube.com/')
        print('Exiting the program')
        exit()
    else:
        return url


url = input('Enter your url (e.g. https://www.youtube.com/):\n')
url = check_url(url)

nested_links = list(set(get_links(url))) #get rid of doubles
filtered_links = filter_nested_links(nested_links)
print(f'Total unique links found: {len(filtered_links)}')
print('Putting the links in file...')
if put_links_in_file(links=filtered_links, url=url):
    print('The links were put in the file without an issue.')



