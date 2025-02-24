from bs4 import BeautifulSoup
import requests

url = requests.get('https://newsroom.cisco.com/c/services/i/servlets/newsroom/rssfeed.json')
print (url)

soup = BeautifulSoup(url.content, 'lxml')
items = soup.find_all('item')
for item in items:
    title = item.title.text
    description_soup = BeautifulSoup(item.description.text, 'html.parser')
    br_texts = [br.next_sibling for br in description_soup.find_all('br') if br.next_sibling]
    description = ' '.join([str(text) for text in br_texts])
    description = description.split(' <b>')[0]
    a_texts = [a['href'] for a in description_soup.find_all('a', href=True)]
    link = ' '.join(a_texts)
    print(f"{title}\n{description}\n{link}\n")