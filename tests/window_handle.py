import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"./drivers/chromedriver")
driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
#driver.find_element(By.ID ,"newTabBtn").click()
#time.sleep(5)
#print(driver.current_window_handle)

#handles = driver.window_handles

# for handle in handles:
#     driver.switch_to.window(handle)
#     print(driver.title)
#     print(driver.current_window_handle)
#     print(driver.current_url)
#     if driver.title == "Window Handles Practice - H Y R Tutorials":
#         driver.close()
#         time.sleep(4)

driver.find_element(By.ID ,"newWindowBtn").click()
time.sleep(5)


print(driver.current_window_handle)
print(driver.title)

handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    print(driver.current_window_handle)

    if driver.title =="Window Handles Practice - H Y R Tutorials":
        driver.close()
        time.sleep(4)