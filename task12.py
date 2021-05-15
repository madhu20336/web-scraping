import requests
from task1 import scrape_top_list
import json
from pprint import pprint
from bs4 import BeautifulSoup

name1 = scrape_top_list()
def scrape_movie_cast():
    list_1 = []
    movie_number = int(input("Enter the movie number: "))
    cast_api = name1[movie_number]["url"]
    cast_url = requests.get(cast_api)
    soup = BeautifulSoup(cast_url.text,"html.parser")
    cast = soup.find("table","cast_list")
    td = cast.find_all("td",class_="")
    for i in td:
        my_dict = {}
        id = i.a["href"][6:15]
        artist = i.a.get_text().strip()
        my_dict["artist"] = artist
        my_dict["imbd_id"] = id
        list_1.append(my_dict)
        # print(list1)
    with open("artist_name.json","w") as saral:
        json.dump(list_1,saral,indent=4)
    return(list_1) 
scrape_movie_cast()