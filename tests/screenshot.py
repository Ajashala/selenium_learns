import os
import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from support.common import get_element
from support.common import type_element
from support.common import click_element


@pytest.fixture(scope='module')
def driver():
        chrome_driver_path = r"./drivers/chromedriver"
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()

def test_url(driver):
    driver.get("https://np.chimpvine.com/login/index.php")
    assert 'ChimpVine: Log in to the site' == driver.title

def test_login(driver):
    #driver.find_element(By.ID, "login_username").send_keys("")
    # driver.find_element(By.ID, "login_password").send_keys("")
    # driver.find_element(By.ID, "login-submit").click()
    type_element(driver,(By.ID,"login_username"),"pramod")
    type_element(driver, (By.ID, "login_password"), "Pramod12!@")
    click_element(driver, (By.ID,"login-submit"))

    time.sleep(5)
    assert 'https://np.chimpvine.com/' == driver.current_url

def test_screenshot(driver):
    driver.save_screenshot("sc.png")
    time.sleep(5)