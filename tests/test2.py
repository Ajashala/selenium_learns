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
    if os.environ.get("IS_LOCAL") is True:
        chrome_driver_path = r"./drivers/chromedriver"
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)

    else:
        api_key=os.environ.get("API_KEY")    #74cac9f0e66fb727f12500df

        api_secret_key =os.environ.get("API_SECRET_KEY") #ad81b4cf2b407852b881529d7492ec8832f72415c2757811ea4249795aadcf919c06c188
        base ='a.blazemeter.com'

        desired_capabilities ={
            'browserName': 'chrome',
            'blazemeter.reportname':'Demo report'
        }
        blazegrid_url ="https://{api_key}:{api_secret_key}@{base}/api/v4/grid/wd/hub".format(api_key=api_key,
                                                                                              api_secret_key=api_secret_key,
                                                                                              base=base
                                                                                              )
        print(blazegrid_url)
        driver = webdriver.Remote(command_executor=blazegrid_url,
                                  desired_capabilities=desired_capabilities)
    yield driver
    driver.quit()

# @pytest.mark.usefixtures("driver")
# @pytest.fixture(scope = "function",autouse=True)
# def blazemeter_report(request,driver):
#     args= {
#         'testCaseName': 'Test case name demo',
#         'testSuiteName': 'Test Suit name demo'
#
#     }
#     driver.execute_script("/*FlOW_MARKER test-case-start */",args)
#     yield driver
#     if request.node.session.testfailed>0:
#         status ="failed"
#     else:
#         status ="passed"
#
#     args ={
#         'status' :status,
#         'message': 'Test demo has {status}'.format(status=status)
#     }
#     driver.execute_script("/*FlOW_MARKER test-case-stop */", args)

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

def test_trial(driver):
    get_element(driver,(By.CSS_SELECTOR, '#inst1009 > div > section > div > div > div > div > div.owl-stage-outer > div > div > div > div > a')).click()
    assert 'pricing' in driver.current_url

# API key id 74cac9f0e66fb727f12500df
# API secret key ad81b4cf2b407852b881529d7492ec8832f72415c2757811ea4249795aadcf919c06c188