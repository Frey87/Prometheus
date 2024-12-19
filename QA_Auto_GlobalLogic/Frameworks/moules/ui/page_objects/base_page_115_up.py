from selenium import webdriver
from selenium import webdriver.chrome.service import Service


class BasePage:
    def __init__(self) -> None:
      self.driver = webdriver.Chrome(service=Service(ChromeriverManager().install()))     )
      
    def close(self):
      self.driver.close()
