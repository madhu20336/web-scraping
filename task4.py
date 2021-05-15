from task1 import scrape_top_list
import requests
import json
from bs4 import BeautifulSoup 
from pprint import pprint

detail_mov = {}
director = []
language = []
genre = []

def scrape_movie_details (list):
    movie_number = int(input("Enter the any movie number: "))
    movie_name = list[movie_number-1]["name"]
    movie_api = list[movie_number-1]["url"]
    movie_url = requests.get(movie_api)
    soup = BeautifulSoup(movie_url.text,"html.parser")
    director_name = soup.find("div",class_ = "credit_summary_item").a.get_text()
    director.append(director_name)
    movies_poster = soup.find("div",class_="poster").a['href']
    movie_poster = "https://www.imdb.com/" + movies_poster
    bio = soup.find("div",class_="plot_summary")
    movie_bio = bio.find("div",class_="summary_text").get_text().strip()
    detail = soup.find("div",attrs={"class":"article","id":"titleDetails" })
    div1 = detail.find_all("div")
    for i in div1:
        run = i.find_all("h4")
        for j in run:
            if "Language:" in j:
                lan = i.find_all("a")
                for lang_uage in lan:
                    movie_language = lang_uage.get_text()
                    language.append(movie_language)
    time = soup.find("div",class_="subtext")
    runtime = time.find("time").get_text().strip()
    hour_to_min = (int(runtime[0])) * 60
    i = 0
    mins = ""
    a = runtime[3:]
    while i < len(a) :
        if a[i] == "m":
            break
        mins = mins + a[i]
        i = i + 1
    runtime_of_movie = hour_to_min + int(mins)
    movie_genre = time.find_all("a")
    movie_genre.pop()
    for i in movie_genre:
        genre_1 = i.get_text()
        genre.append(genre_1)
    detail_mov["movie_name"] = list[movie_number-1]["name"]
    detail_mov["director"] = director
    detail_mov["country"] = "India"
    detail_mov["poster_url"] = movie_poster
    detail_mov["language"] = language
    detail_mov["movie_bio"] = movie_bio
    detail_mov["runtime"] = runtime_of_movie
    detail_mov["movie_genre"] = genre
    with open ("movie_details.json","w") as movie_number:
        json.dump(detail_mov,movie_number,indent=4)
    return(detail_mov)
scrape_movie_details (scrape_top_list())

   