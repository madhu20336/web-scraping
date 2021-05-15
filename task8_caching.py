import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
import os


def scrape_top_list ():
    if os.path.isfile("caching/" + "scrap.json"):
        with open ("caching/" + "scrap.json","r") as saral_data:
            movie_data = json.load(saral_data)
        return movie_data
    else:
        IMDB_api = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
        IMDB_url = requests.get(IMDB_api)
        data = IMDB_url.json
        soup = BeautifulSoup(IMDB_url.text,"html.parser")
        dict_1 = {}
        list_1 = []
        div = soup.find("div",class_ = "lister")
        body = div.find("tbody",class_ = "lister-list")
        name = body.find_all("tr")
        serial_no = 0
        for tr in name:
            movie_name = tr.find("td",class_ = "titleColumn").a.get_text()
            rating = tr.find("td",class_ = "ratingColumn imdbRating").strong.get_text()
            years = tr.find("td",class_ = "titleColumn").span.get_text()
            link = tr.find("td",class_= "titleColumn").a['href']
            url = 'https://www.imdb.com' + str(link)
            serial_no += 1
            
            dict_1["name"] = movie_name
            dict_1["year"] = int(years[1:5])
            dict_1["rating"] = rating
            dict_1["position"] = int(serial_no)
            dict_1["url"] = url
            list_1.append(dict_1.copy())
            with open("saral.json","w") as saral:
                data = json.dump(list_1,saral,indent=4)
    return(list_1)
scrape_top_list()