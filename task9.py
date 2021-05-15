from task1 import scrape_top_list
import requests
import json
from bs4 import BeautifulSoup 
from pprint import pprint
import random
import time 

list = scrape_top_list()
serial_no = 1
def movie_details():
    global time
    global serial_no
    time_limit = random.randint(1,3)
    imdb_api = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
    # time.sleep(time_limit)
    imdb_url = requests.get(imdb_api)
    data = imdb_url.json
    soup = BeautifulSoup(imdb_url.text,"html.parser")
    dict_1 = {}
    
    div = soup.find("div",class_ = "lister")
    body = div.find("tbody",class_ = "lister-list")
    name = body.find_all("tr")
    for tr in name:
        list_1 = []
        director = []
        language = []
        genre = []
        movie_name = tr.find("td",class_ = "titleColumn").a.get_text()
        rating = tr.find("td",class_ = "ratingColumn imdbRating").strong.get_text()
        years = tr.find("td",class_ = "titleColumn").span.get_text()
        link = tr.find("td",class_= "titleColumn").a['href']
        url = 'https://www.imdb.com' + str(link)
        serial_no += 1
        # time.sleep(time_limit)
        movie_url = requests.get(url)
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
        list1 = []
        api_cast = url
        url_cast = requests.get(api_cast)
        soup = BeautifulSoup(url_cast.text,"html.parser")
        table = soup.find("table","cast_list")
        td = table.find_all("td",class_="")
        for i in td:
            my_dict = {}
            id = i.a["href"][6:15]
            artist = i.a.get_text().strip()
            my_dict["artist"] = artist
            my_dict["imbd_id"] = id
            list1.append(my_dict)
        dict_1["movie_name"] = movie_name
        dict_1["year"] = int(years[1:5])
        dict_1["rating"] = rating
        dict_1["position"] = int(serial_no)
        dict_1["url"] = url
        dict_1["director"] = director
        dict_1["country"] = "India"
        dict_1["poster_url"] = movie_poster
        dict_1["language"] = language
        dict_1["movie_bio"] = movie_bio
        dict_1["runtime"] = runtime_of_movie
        dict_1["movie_genre"] = genre
        dict_1["cast"] = list1
        list_1.append(dict_1)
        link = link[7:16]
        print(link)

        with open ("movie/" + link + ".json","w") as Data:
            json.dump(list_1,Data,indent=4)
    return(list_1)
movie_details()