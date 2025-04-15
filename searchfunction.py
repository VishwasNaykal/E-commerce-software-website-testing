import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Set up Chrome driver
os.environ['PATH'] += r"C:/chromedriver-win64/chromedriver-win64"
driver = webdriver.Chrome()

try:
    # Open the URL
    url = "https://www.jiomart.com/"
    driver.get(url)
    driver.maximize_window()
    driver.refresh()

    # Wait for the size selection element to be clickable
    Search = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'autocomplete-0-input'))
    )
    time.sleep(2)
    Search.send_keys('Maaza mango drink')
    Search.send_keys(Keys.RETURN)

    # Wait for the cart operation to complete (adjust this time based on page behavior)
    time.sleep(10)

finally:
    # Close the browser session
    driver.quit()