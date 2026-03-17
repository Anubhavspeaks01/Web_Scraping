from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service = s)

driver.get('https://www.google.com')
# time.sleep(2)

# fetch the search input box using xpath
user_input = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')

user_input.send_keys('Campusx')
# time.sleep(1)

user_input.send_keys(Keys.ENTER)
# time.sleep(2)

# fetch titles
results = driver.find_elements(by=By.XPATH, value='//h3')

for r in results:
    print(r.text)

# time.sleep(10)

driver.quit()