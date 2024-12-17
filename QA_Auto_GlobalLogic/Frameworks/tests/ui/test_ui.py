import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import By
import time

@pytest.mark.ui
def test_check_incorrect_username():
  
  driver = webdriver.Chrome(
    service=Service(r"PATH" + "chromedriver")
    )





  login_elem = driver.find_element(By.ID, "login field")
  driver.get("https://github.com/login")

  login_elem.send_keys("sergiibutenko@mistakeinemail.com")
  

  pass_elem = driver.find_element(By.ID, "password")


  pass_elem.send_keys("wrong password")


  btn_elem = driver.find_element(By.NAME, "commit")


  btn_elem.click()
  time.sleep(3)
  driver.close()


