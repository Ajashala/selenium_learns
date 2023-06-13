import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"./drivers/chromedriver")
driver.get("https://np.chimpvine.com/login/index.php")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.ID,"login_username").send_keys("pramod")
driver.find_element(By.ID,"login_password").send_keys("Pramod12!@")
driver.find_element(By.ID,"login-submit").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div/nav/ul[1]/ul/li[4]/div").click()

dropdownbox =driver.find_elements(by=By.TAG_NAME,value="a")
i =0
while i < len(dropdownbox):
    if(dropdownbox[i].text=="Log out"):
        dropdownbox[i].click()
        time.sleep(4)
    i =i +1
time.sleep(4)