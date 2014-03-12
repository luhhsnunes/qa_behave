from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def my_browser():
  driver = webdriver.Firefox()
  return driver
