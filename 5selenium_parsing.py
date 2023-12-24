from selenium import webdriver
from selenium.webdriver.common.by import By


base_url = 'https://habr.com/ru/articles/'
driver = webdriver.Chrome()
driver.get(base_url)
h3_list = driver.find_elements(By.TAG_NAME, 'h3')
for i in range(5):
    a = h3_list[i].find_element(By.TAG_NAME, 'a')
    if a:
        print(a.get_attribute('href'))

