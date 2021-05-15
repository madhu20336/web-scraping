import requests
import json
from bs4 import BeautifulSoup 
from pprint import pprint


def scrape_top_list():
    imdb_api = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
    imdb_url = requests.get(imdb_api)
    data = imdb_url.json
    soup = BeautifulSoup(imdb_url.text,"html.parser")
    div = soup.find("div",class_ = "lister")
    body = div.find("tbody",class_ = "lister-list")
    name = body.find_all("tr")
    serial_no = 0
    dict_1 = {}
    list_1 = []
    for tr in name:
        movie_name = tr.find("td",class_ = "titleColumn").a.get_text()
        # print(serial_no,".",movie_name)
        rating = tr.find("td",class_ = "ratingColumn imdbRating").strong.get_text()
        # print(rating)
        years = tr.find("td",class_ = "titleColumn").span.get_text()
        # print(years)
        link = tr.find("td",class_= "titleColumn").a['href']
        url = 'https://www.imdb.com' + str(link)
        # print(url)
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
            
        




# rank = soup.find("table",class_ = "chart full-width")
    # body_1 = rank.find("tbody",class_ = "lister-list")
    # name_1 = body_1.find_all("tr")