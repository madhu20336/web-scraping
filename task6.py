from task5 import top_movie_list 
import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup


list_1 = top_movie_list 
Language = []
my_dict = {}
def analyse_movies_language():
    for a in list_1:
        for b in a["language"]:
            Language.append(b)
        for c in Language:
            if c not in my_dict:
                my_dict[c] = 1
            else:
                my_dict[c] = 1 + 1
    with open("movie_language.json","w") as lang_uage:
        json.dump(my_dict,lang_uage,indent=4)
    return (my_dict)
analyse_movies_language()   
