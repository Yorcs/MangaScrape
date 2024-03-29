from bs4 import BeautifulSoup
import requests
import time

def find_manga():
    html_text = requests.get('https://www.mangaupdates.com/series.html?perpage=100').text

    # Accepting user input to exclude genre
    print('Insert genre you would want to be excluded')
    exclude_genre = input('>').lower()
    special_characters = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    # # Scraping all of the available manga
    soup = BeautifulSoup(html_text, 'lxml')
    mangas = soup.find_all('div', class_ = 'col-12 col-lg-6 p-3 text')

    # # Looping to scrape data and f.writeing the result
    for index, manga in enumerate(mangas):
        manga_subinfo = manga.find('div', class_ = 'col text p-1 pl-3')
        year_published_and_rating = manga_subinfo.findAll('div', class_ = 'text')[2].text
        year_published = '%.4s' % year_published_and_rating
        
        # To limit the search
        if(int(year_published) > 2000):
            genre = manga.find('div', class_ = 'textsmall').text
            genre_split = genre.split(", ")
            genre_split_lowercase = map(str.lower, genre_split)

            manga_name = manga_subinfo.find('a', attrs={"alt" : "Series Info"}).text
            more_info = manga.div.div.a['href']

            # Checking in case there are multiple inputs from the user
            if any(c in special_characters for c in exclude_genre):
                multiple_genre = exclude_genre.strip().split(', ')

                # Checking if the user input matches the genre scraped from the website
                if not any(individual_exclude_genre in multiple_genre for individual_exclude_genre in genre_split_lowercase):
                    with open(f'posts/{index}.txt', 'w', encoding="utf-8") as f:
                        f.write(f"Manga Name: {manga_name.strip()} \n")
                        f.write(f"Genre: {genre.strip()} \n")
                        f.write(f"Year Published: {year_published.strip()} \n")
                        f.write(f"More Info: {more_info} \n")
                    print(f'File saved: {index}')

            else:
                if exclude_genre not in genre_split_lowercase:
                    with open(f'posts/{index}.txt', 'w', encoding="utf-8") as f:
                        f.write(f"Manga Name: {manga_name.strip()} \n")
                        f.write(f"Genre: {genre.strip()} \n")
                        f.write(f"Year Published: {year_published.strip()} \n")
                        f.write(f"More Info: {more_info} \n")
                    print(f'File saved: {index}')

# Run Code every 10 minutes
if __name__ =='__main__':
    while True:
        find_manga()
        time_wait = 10
        print(f'Waiting time: {time_wait} minutes')
        time.sleep(time_wait * 60)