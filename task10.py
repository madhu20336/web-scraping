from task1 import scrape_top_list
import requests
import json
from bs4 import BeautifulSoup 
from pprint import pprint

def analyse_language_and_directors(name):
    name_1 = name[:250]
    List = []
    for name_2 in name_1:
        detail_mov = {}
        director = []
        language = []
        movie_api = name_2["url"]
        movie_url = requests.get(movie_api)
        soup = BeautifulSoup(movie_url.text,"html.parser")
        director_name = soup.find("div",class_ = "credit_summary_item").a.get_text()
        director.append(director_name)
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
        detail_mov["director"] = director
        detail_mov["language"] = language
        List.append(detail_mov.copy())
        with open ("get_movie_list_details.json","w") as movie:
            json.dump(List,movie,indent=4)
    return List
top_movie_list = analyse_language_and_directors(scrape_top_list())

