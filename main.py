from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.mangaupdates.com/series.html?perpage=100').text

soup = BeautifulSoup(html_text, 'lxml')
manga = soup.find('div', class_ = 'col-12 col-lg-6 p-3 text')
genre = manga.find('div', class_ = 'textsmall').text
print(genre)