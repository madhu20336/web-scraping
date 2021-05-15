from task1 import scrape_top_list
import requests
import json
from bs4 import BeautifulSoup 
from pprint import pprint

movies_name = scrape_top_list()

year_1 = []
year_2 = []

def group_by_year ():
    i = 0
    while i < len(movies_name):
        year = movies_name[i]["year"]
        year_1.append(year)
        i = i + 1
    j = 0
    while j < len(year_1):
        if year_1[j] not in year_2:
            year_2.append(year_1[j])
        j = j + 1
    k = 0
    while k < len(year_2):
        l = 0
        while l < len(year_2):
          if year_2[k] < year_2[l]:
            a = year_2[k]
            year_2[k] = year_2[l]
            year_2[l] = a
          l = l + 1
        k = k + 1 
    my_dict = {}
    a = 0
    while a < len(year_2):
        list1 = []
        b = 0
        while b < len(movies_name):
            if year_2[a] == movies_name[b]["year"]:
                if movies_name[b] not in list1:
                    list1.append(movies_name[b])
            b = b + 1
        my_dict[year_2[a]] = list1 
        a = a + 1
    with open ("movies.json","w") as sara_data2:
        json.dump(my_dict,sara_data2,indent = 4)
    return(my_dict)
group_by_year()

