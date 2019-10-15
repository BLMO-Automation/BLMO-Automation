from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common import keys
import unittest
from time import sleep

class WebBrowesr():
    driver = webdriver.Chrome(executable_path='C:/Users/Ashok/PycharmProjects/Auto_framework/Resources/browserDriver/chromedriver.exe',desired_capabilities=None)
    driver.get('https://www.google.com/')
    sleep(5)
    driver.quit()


