import requests
from bs4 import BeautifulSoup
#TO DO
#user input - done
#write results in file - done
#try except - done
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
            file.write(url+'\n')
            for i in range(len(links)):
                file.write(f'{links[i]}\n')
        file.close()

    except Exception as e:
        print(f'Something went wrong: {e}')
    return 1


url = input('Enter your url (e.g. https://www.youtube.com/):\n')
nested_links = list(set(get_links(url))) #get rid of doubles

print(f'Total of the links found: {len(nested_links)}')
print('Putting the links in file...')
put_links_in_file(links=nested_links, url=url)




