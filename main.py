'''
Docstring for main
starting in 16 feb 
'''
import emoji
import requests
from bs4 import BeautifulSoup
import tqdm
import time 
import re
from tqdm import tqdm

url = "https://wallex.ir/price/btc"         # i used from wallex website 
answer = input("you want bitcoin (y/n) ?")
if answer == "y" :
    while True :
        try :
            response = requests.get(url)
            soup = BeautifulSoup(response.text,"html.parser")
            text = soup.get_text()

            number = re.search(r"([0-9]{1,3}(?:,[0-9]{3})+)", text)
            if number :
                price = number.group(1)
                for i in tqdm(range(100)):
                    time.sleep(0.03)


                print(f'price of bitcoin : {price}')
                answer2 = input("show again ? (y/n)")
                if answer2 == "y":
                    pass
                else:
                    print("ok! have good day")
                    break
            else :
                print("i can not find any thing")
        except Exception as e :
            print(f'error : {e}')
        time.sleep(5)
else : 
    print("ok! have good day ")