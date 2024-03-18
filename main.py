from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.mangaupdates.com/series.html?perpage=100').text

soup = BeautifulSoup(html_text, 'lxml')
manga = soup.find('div', class_ = 'col-12 col-lg-6 p-3 text')
mangaSubInfo = manga.find('div', class_ = 'col text p-1 pl-3')

genre = manga.find('div', class_ = 'textsmall').text
mangaName = mangaSubInfo.find('a', attrs={"alt" : "Series Info"}).text
yearPublished = mangaSubInfo.findAll('div', class_ = 'text')[2].text
print(genre)
print(mangaName)
print(yearPublished)