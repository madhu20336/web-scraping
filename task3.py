from task1 import scrape_top_list
import requests
import json
from bs4 import BeautifulSoup 
from pprint import pprint

list = scrape_top_list()
year = []
def group_by_decade():
    i = 0
    while i < len(list):
        year.append(list[i]["year"])
        i += 1
    year.sort()
    j = 0
    dict = {}
    while j < len(year):
        year_1 = (year[j]//10)*10
        k = 0
        list_1 = []
        while k < len(list):
            if list[k]["year"] >= year_1 and list[k]["year"] < (year_1 + 10):
                list_1.append(list[k])
            dict[year_1] = list_1
            k += 1
        j += 1
        with open(" decade.json","w") as saral_data3:
            json.dump(dict,saral_data3,indent=4)
group_by_decade()




