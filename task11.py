# from task1 import scrape_top_list
# import requests
# import json
# from bs4 import BeautifulSoup 
# from pprint import pprint

# list_1 = scrape_top_list()
# def get_movie_details(name):
#     name_1 = name[:250]
#     for name_2 in name_1:
#         detail_mov = {}
#         genre = []
#         movie_api = name_2["url"]
#         movie_url = requests.get(movie_api)
#         soup = BeautifulSoup(movie_url.text,"html.parser")
#         time = soup.find("div",class_="subtext")
#         runtime = time.find("time").get_text().strip()
#         movie_genre = time.find_all("a")
#         movie_genre.pop()
#         for i in list_1:
#             for j in i[movie_genre]:
#                 genre.append(j)
#                 for k in genre:
#                     if k not in detail_mov:
#                         detail_mov[k] = 1
#                     else:
#                         detail_mov[k] = 1 + 1
#                         detail_mov["movie_genre"] = genre
#                         List.append(detail_mov.copy())
#         with open ("movie_genre.json","w") as movie:
#             json.dump(List,movie,indent=4)
#     return List
# get_movie_details(scrape_top_list())


from task5 import top_movie_list 
import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

list_1 = top_movie_list 
genre = []
my_dict = {}
def analyse_movies_genre():
    # name_1 = name[:250]
    for i in list_1:
        for j in i["movie_genre"]:
            genre.append(j)
        for k in genre:
            if k not in my_dict:
                my_dict[k] = 1
            else:
                my_dict[k] = 1 + 1
                # print(my_dict)
    with open("movie_genre.json","w") as director_name:
        json.dump(my_dict,director_name,indent=4)
    return (my_dict)
analyse_movies_genre()   