from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")



driver = webdriver.Chrome(options=options)

# Open Google Meet link
meet_link = "https://meet.google.com/agn-zezh-cub" # create the link right on the time when writting the scriptpi
driver.get(meet_link)

time.sleep(5)

# Wait for the "Join" button to be clickable
join_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Join')]"))
)

time.sleep(10) # wait before clicking on join button
# Click the "Join" button
join_button.click()

# Close the browser
driver.quit()

'''
it click on the join button but aboard the call 
saying "you can't join the call" it's happen because of 
authentication issue
when i searched found that i have to provide valid e-mail address to join.
'''