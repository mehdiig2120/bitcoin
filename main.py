'''
Docstring for main
starting in 16 feb 
'''
import emoji
from selenium import webdriver
from bs4 import BeautifulSoup
import tqdm
import time 

driver = webdriver.Chrome()
driver.get("https://wallex.ir/price/btc")    #get information from wallex website 

from tqdm import tqdm
for i in tqdm(range(100)):
    time.sleep(0.1)

soup = BeautifulSoup(driver.page_source,"html.parser")
print(soup.prettify())
driver.quit()
print(soup)

