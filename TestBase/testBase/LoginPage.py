from TestBase.testBase.BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LMOHomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser,baseurl="http://192.168.1.154:8989")

    locator_dictionary = {
        "userName":(By.ID,'isc_12'),
        "passWord":(By.ID,'isc_16'),
        "roleCombo":(By.ID,'isc_1F'),
        "usrRole": (By.ID, 'isc_PickListMenu_0_row_0'),
        "signin_button":(By.ID,'isc_1L')
    }
    def loginAdmin(self, username='admin', password='admin'):
        self.find_element(*self.locator_dictionary['userName']).send_keys(username)
        self.find_element(*self.locator_dictionary['passWord']).send_keys(password)
        self.find_element(*self.locator_dictionary['roleCombo']).click()
        self.find_element(*self.locator_dictionary['usrRole']).click()

    class LogOut(BasePage):
        def __init__(self, context):
            BasePage.__init__(self,context.browser,baseurl="http://192.168.1.154:8989")

        locator_dictionary = {
            "logOut":(By.XPATH,'//img[contains(@src,"images/logout.png")]')
        }