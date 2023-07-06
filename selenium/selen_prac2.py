from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#config the chromedriver
driver = webdriver.Chrome()
driver.get("http://www.google.com")

#find an element by name



search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('OpenAI')
search_box.send_keys(Keys.RETURN)

# Find all elements with a specific tag name
search_results = driver.find_elements(By.TAG_NAME, 'h3')
for result in search_results:
    print(result.text)

time.sleep(5)

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(10)

# Scroll to the top of the page
driver.execute_script("window.scrollTo(0, 0);")

time.sleep(10)

# Close the browser
driver.quit()
