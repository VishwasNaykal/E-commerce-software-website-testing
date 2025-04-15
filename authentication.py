import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:/chromedriver-win64/chromedriver-win64"
driver = webdriver.Chrome()
url = "https://account.relianceretail.com/sign-up/?client_id=fdb646ea-e708-4725-a953-228fa1cb8355&return_ui_url=www.jiomart.com/customer/account/login?msite=yes"
driver.get(url)
driver.refresh()

try:
    # Wait for the phonenumber field to be present
    phonenumber = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'phoneNumber'))
    )
    time.sleep(2)
    phonenumber.send_keys(' ')

    # Wait for the Proceed button to be present and clickable
    Proceed = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Continue")]'))
    )
    time.sleep(2)
    Proceed.click()

    

    time.sleep(10)

finally:
    driver.quit()
