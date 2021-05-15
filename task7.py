from task5 import top_movie_list 
import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

list_1 = top_movie_list 
director = []
my_dict = {}
def analyse_movies_director():
    for i in list_1:
        for j in i["director"]:
            director.append(j)
        for k in director:
            if k not in my_dict:
                my_dict[k] = 1
            else:
                my_dict[k] = 1 + 1
    with open("movie_director.json","w") as director_name:
        json.dump(my_dict,director_name,indent=4)
    return (my_dict)
analyse_movies_director()   