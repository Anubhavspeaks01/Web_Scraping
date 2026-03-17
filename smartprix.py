import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup   # 👈 new

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.smartprix.com/mobiles')
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[5]/div[2]/label[2]/input').click()
time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')

while True:
    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
        time.sleep(2)
    except:
        break

    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == old_height:
        break

    old_height = new_height

# 👉 formatting part
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

with open('smartprix.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())   # 👈 formatted output

driver.quit()