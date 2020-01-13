from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PageObjects.locators import Locator

import logging
import time
import pytest
import allure

class Logindex(object):

    def __init__(self,driver):
        self.driver = driver

        self.username = driver.find_element(By.XPATH, Locator.username)
        self.password = driver.find_element(By.XPATH, Locator.password)
        self.roleCombo = driver.find_element(By.XPATH, Locator.roleCombo)
        self.roleAdmin = driver.find_element(By.XPATH, Locator.roleAdmin)
        self.sigin = driver.find_element(By.XPATH, Locator.sigin)

    def getUsername(self,username):
        self.username.clear()
        self.username.send_keys(username)

    def getPassword(self, password):
        self.password.clear()
        self.password.send_keys(password)

    def getSignIn(self):
        self.signIn.click()

    def getRoleAdministrator(self):
        self.roleCombo.click()
        self.roleAdmin.click()

