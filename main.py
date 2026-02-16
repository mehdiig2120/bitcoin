'''
Docstring for main
starting in 16 feb 
'''
import emoji
import requests
from bs4 import BeautifulSoup
import tqdm
import time 
import lxml

result = requests.get("https://bitarz.net/prices/")    #get information from wallex website 
soup = BeautifulSoup(result.text,"html.parser")
print(soup)

