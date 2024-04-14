from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def center_parser():

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.bcc.kz/personal/cards/ironcard/')
    
    card_title7 = driver.find_element(By.XPATH, '//*[@id="product-cards-6"]/div[1]').text
    card_title7 = re.search(r'#(\w+)', card_title7).group(1)
    card_cash7 = driver.find_element(By.XPATH, '//*[@id="product-cards-3"]/div/div/div/div/div/div[3]/div[1]').text
    card_cash7 = re.search(r'\d+', card_cash7).group()
    
    data1 = (card_title7, card_cash7)
    driver.quit()

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.bcc.kz/personal/cards/pension-card/')
    card_title8 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[1]/p').text
    card_cash8 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]').text
    card_cash8 = re.search(r'\d+', card_cash8).group()

    card_title9 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[1]/p').text
    card_cash9 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]').text
    card_cash9 = re.search(r'\d+', card_cash9).group()

    driver.quit()
    data2 = [(card_title8, card_cash8), (card_title9, card_cash9), data1]
    return data2