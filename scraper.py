import requests
from bs4 import BeautifulSoup 

url = input("Provide a URL to begin scraping: ")

response = requests.get(url) 

soup = BeautifulSoup(response.content, 'html.parser')

for link in soup.find_all('a'): 
    print(link.get_text(), link.get('href'))

