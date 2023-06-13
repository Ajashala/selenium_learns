from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.relative_locator import RelativeLocator

driver = webdriver.Chrome(executable_path=r"./drivers/chromedriver")
driver.get("https://np.chimpvine.com/login/")

driver.find_element(By.ID,"login-username").send_keys("pramod")
password =driver.find_element(By.ID,"login-password").send_keys("Pramod12!@")

#driver.find_element(RelativeLocator.with(By.TAG_NAME("submit")).below(password)).click()