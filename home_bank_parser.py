import re
from selenium import webdriver
from selenium.webdriver.common.by import By

def home_parser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.get('https://home.kz/debit-cards')

    card_title = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[1]/div[1]/p[1]').text
    card_cash = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/p[2]').text
    card_cash = re.search(r'\d+', card_cash).group()
    card_title1 = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[2]/div[1]/p[1]').text
    card_cash1 = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/p[2]').text
    card_cash1 = re.search(r'\d+', card_cash1).group()
    card_title2 = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[3]/div[1]/p[1]').text
    card_cash2 = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div[2]/div[3]/div[1]/div[1]/div[1]/p[2]').text
    card_cash2 = re.search(r'\d+', card_cash2).group()
    
    data = [(card_title, card_cash),(card_title1, card_cash1), (card_title2, card_cash2)]
    return data
