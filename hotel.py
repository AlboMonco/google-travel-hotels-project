from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import os
import time
import pandas as pd


def get_hotels_from_excel():
    path = os.path.join(os.getcwd(), "hotels.xlsx")
    return pd.read_excel(path, engine="openpyxl")["hoteis"].to_list()


def hotel(hotels:list):
    serv = Service(os.path.join("C:\\","Users","HP","Code","geckodriver.exe"))
    firefox = webdriver.Firefox(service=serv)
    hotel_prices = []

    for hotel in hotels:
        firefox.get("https://www.google.com/travel/")
        xpath_search_button = '//*[@id="oA4zhb"]'
        firefox.find_element(By.XPATH, xpath_search_button).send_keys(hotel)
        xpath_press_search_button = "/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div/div[1]/div[1]/div[2]/c-wiz/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/ul/li/div/div/div/div[2]/div"
        
        time.sleep(1)

        firefox.find_element(By.XPATH, xpath_press_search_button).click()

        time.sleep(3)
        
        xpath_price = "/html/body/c-wiz[2]/div/div[2]/div[2]/span[1]/c-wiz/c-wiz/div/div/div/div/c-wiz[1]/div/section[1]/div[1]/div[2]/c-wiz/div[1]/div/div/span[2]"
        price = firefox.find_element(By.XPATH, xpath_price).text
        
        hotel_prices.append({"hotel_name": hotel, "price": price})

    firefox.close()

    return hotel_prices


def put_prices_to_excel(prices):
    return pd.DataFrame.from_dict(prices).to_excel("prices.xlsx", index=False)


    
if __name__ == "__main__":
    put_prices_to_excel(hotel(get_hotels_from_excel()))
