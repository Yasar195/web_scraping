from selenium import webdriver
from bs4 import BeautifulSoup
import requests

item = input('Enter the item you want to search: ')
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('./chromedriver', options=options)

driver.get('https://amazon.in')

driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').send_keys(item)
driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()

search_results = driver.find_elements_by_class_name('sg-col-inner')

for item in search_results:
    source = item.get_attribute('innerHTML')
    soup = BeautifulSoup(source, 'lxml')
    data = soup.find('span', attrs={'class': 'a-text-normal'})
    symbol = soup.find('span', attrs={'class': 'a-price-symbol'})
    price = soup.find('span', attrs={'class': 'a-price-whole'})
    if data and symbol and price:
        print(f'{data.string}: {symbol.string} {price.string}')
