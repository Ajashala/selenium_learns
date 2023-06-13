# exception_handling using search button
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"./drivers/chromedriver")
driver.get("https://np.chimpvine.com/login/index.php")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.ID, "login_username").send_keys("pramod")
driver.find_element(By.ID, "login_password").send_keys("Pramod12!@")
driver.find_element(By.ID, "login-submit").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/nav/ul[2]/li/div/a").click()
time.sleep(3)
try:
    driver.find_element(By.ID, "searchform_search").send_keys("nonexistent")
    driver.find_element(By.ID, "searchform_button").click()
    element = driver.find_element(By.ID, "non-existent")
    # This line will be executed if the element is found
    print("Element found:", element.text)
    time.sleep(3)

except NoSuchElementException:
    # Handle the exception when the element is not found
    print("Element not found")
    time.sleep(3)

finally:
    # Close the browser window
    driver.quit()

time.sleep(5)
