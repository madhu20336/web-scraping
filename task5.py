from task1 import scrape_top_list
import requests
import json
from bs4 import BeautifulSoup 
from pprint import pprint

def get_movie_details(name):
    name_1 = name[:10]
    List = []
    for name_2 in name_1:
        detail_mov = {}
        director = []
        language = []
        genre = []
        movie_name = name_2["name"]
        movie_api = name_2["url"]
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
            # return run
            for j in run:
                if "Language:" in j:
                    lan = i.find_all("a")
                    for lang_uage in lan:
                        movie_language = lang_uage.get_text()
                        language.append(movie_language)
                        # print(language)

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
        # print(genre_1)
        detail_mov["movie_name"] = name_2["name"]
        detail_mov["director"] = director
        detail_mov["country"] = "India"
        detail_mov["poster_url"] = movie_poster
        detail_mov["language"] = language
        detail_mov["movie_bio"] = movie_bio
        detail_mov["runtime"] = runtime_of_movie
        detail_mov["movie_genre"] = genre
        List.append(detail_mov.copy())
        with open ("10_movie_details.json","w") as movie:
            json.dump(List,movie,indent=4)
    return List

top_movie_list = get_movie_details(scrape_top_list())

