import re
from selenium import webdriver
from selenium.webdriver.common.by import By


def halyk_parser():

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.get('https://halykbank.kz/cards')

    card_title3 = driver.find_element(By.CLASS_NAME, "product-cards-caraousel-item-title").text
    card_cash3 = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div/section[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div').text
    card_cash3 = re.search(r'\d+', card_cash3).group()
    

    card_title4 = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div/section[1]/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[1]').text
    card_cash4 = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div/section[1]/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/div').text
    card_cash4 = re.search(r'\d+', card_cash4).group()

    data = [(card_title3, card_cash3), (card_title4, card_cash4)]
    return data