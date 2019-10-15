'''
Created on 14-Oct-2019

@author: Ashok
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

import logging
import time
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class UserManagement_BLMO(unittest.TestCase):
    global logger

    logging.basicConfig(filename="audit.log", format='%(asctime)s %(message)s', filemode='w')  # Create and configure logger
    logger = logging.getLogger()  # Creating an object
    logger.setLevel(logging.DEBUG)

    @classmethod
    def setUpClass(cls):
        logging.info('Opening a browser')
        cls.driver = webdriver.Chrome(
            executable_path='C:/Users/Ashok/PycharmProjects/Auto_framework/Resources/browserDriver/chromedriver.exe',
            desired_capabilities=DesiredCapabilities.CHROME.clear())
        cls.driver.maximize_window()

    def setUp(self):
        logging.info('LMO Application url is lunched')
        self.driver.get('http://192.168.1.154:8989')

    def tearDown(self):
        # logout functions
        time.sleep(5)
        lStrip = self.driver.find_element_by_xpath('//*[@class="toolStrip"]')
        imgLogout = self.driver.find_element_by_xpath('//img[contains(@src,"images/logout.png")]')
        toolStrip = ActionChains(self.driver)
        toolStrip.move_to_element(lStrip).perform()
        toolStrip.click(imgLogout).perform()

    def test_001_createUser(self):
        self.userlogin()
        self.roleAdministrator()
        self.stackSecurity()
        self.createUser()

    def test_002_createProfile(self):
        self.userlogin()
        self.roleAdministrator()
        self.stackSecurity()
        self.createProfile()

    @classmethod
    def tearDownClass(cls):
        logging.info('Closing a browser')
        cls.driver.close()
        cls.driver.quit()

    def userlogin(self):
        self.driver.find_element_by_id('isc_12').send_keys('admin')
        self.driver.find_element_by_id('isc_16').send_keys('admin')

    def roleAdministrator(self):
        self.driver.find_element_by_id('isc_1F').click()
        self.driver.find_element_by_id('isc_PickListMenu_0_row_0').click()
        self.driver.find_element_by_id('isc_1L').click()

    def stackBandwidthManagement(self):
        time.sleep(5)
        sStack = self.driver.find_element_by_xpath('//*[@class="sectionStack"]')
        bm = self.driver.find_element_by_xpath(
            '//*[@class="imgSectionHeaderTitleclosed"]//*[text()="Bandwidth Management"]')
        stack = ActionChains(self.driver)
        stack.move_to_element(sStack).perform()
        stack.click(bm).perform()

    def stackSecurity(self):
        time.sleep(5)
        sStack = self.driver.find_element_by_xpath('//*[@class="sectionStack"]')
        bm = self.driver.find_element_by_xpath('//*[@class="imgSectionHeaderTitleclosed"]//*[text()="Security"]')
        stack = ActionChains(self.driver)
        stack.move_to_element(sStack).perform()
        stack.click(bm).perform()

    def stackSystemConfiguration(self):
        time.sleep(5)
        sStack = self.driver.find_element_by_xpath('//*[@class="sectionStack"]')
        bm = self.driver.find_element_by_xpath(
            '//*[@class="imgSectionHeaderTitleclosed"]//*[text()="System Configuration"]')
        stack = ActionChains(self.driver)
        stack.move_to_element(sStack).perform()
        stack.click(bm).perform()

    def createUser(self):
        logging.info('user created scripts has started')
        self.driver.find_element_by_xpath('//*[contains(text(),"Users") and @class="treeCell"]').click()
        #
        time.sleep(3)
        sidePanel = self.driver.find_element_by_xpath('//*[@class="listTable"]')
        Auser = self.driver.find_element_by_xpath('//*[contains(text(),"Users") and @class="treeCell"]')
        userPanel = ActionChains(self.driver)
        userPanel.move_to_element(sidePanel).perform()
        userPanel.context_click(Auser).perform()

        self.driver.find_element_by_xpath('//*[@class="menuBorder"]//*[text()="Add User"]').click()
        time.sleep(3)
        self.driver.find_element_by_name('UserName').send_keys('AutoTestUser')
        self.driver.find_element_by_name('FirstName').send_keys('Automation')
        self.driver.find_element_by_name('Password').send_keys('Admin@123')
        self.driver.find_element_by_name('LastName').send_keys('tester')
        self.driver.find_element_by_name('confirmPassword').send_keys('Admin@123')

        self.driver.find_element_by_xpath('//*[@class="selectItemText" and contains(@id,"isc_7")]').click()
        self.driver.find_element_by_id('isc_PickListMenu_0_row_0').click()

        #         self.driver.find_element_by_xpath('//*[@class="toolStripButton"]//*[text()="Add"]').click()
        #         time.sleep(3)
        #         self.driver.find_element_by_xpath('//*[@class="selectItemText" and contains(@id,"isc_BL")]').click()
        #         self.driver.find_element_by_id('isc_PickListMenu_0_row_0').click()
        #
        self.driver.find_element_by_xpath('//*[@class="toolStripButton"]').click()
        time.sleep(5)
        Umsg = self.driver.find_element_by_xpath('//*[@class="windowBackground"]//*[text()="Users added successfully"]')
        UokBtn = self.driver.find_element_by_xpath('//*[@class="windowBackground"]//*[text()="OK"]')

        Cuser = ActionChains(self.driver)
        Cuser.move_to_element(Umsg).perform()
        Cuser.click(UokBtn).perform()
        logging.info('User created successfully')

    def createProfile(self):
        logging.info('profile created scripts has started')
        self.driver.find_element_by_id('isc_44').click()  # Security click function
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[contains(text(),"Profiles") and @class="treeCell"]').click()
        time.sleep(3)

        sidePanel = self.driver.find_element_by_xpath('//*[@class="listTable"]')
        prfl = self.driver.find_element_by_xpath('//*[contains(text(),"Profiles") and @class="treeCell"]')
        uProfile = ActionChains(self.driver)
        uProfile.move_to_element(sidePanel).perform()
        uProfile.context_click(prfl).perform()
        self.driver.find_element_by_xpath('//*[@class="menuBorder"]//*[text()="Add Profile"]').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('//span[contains(@id,"extra_icon_3")]').click()
        self.driver.find_element_by_xpath('//span[contains(@id,"extra_icon_4")]').click()
        self.driver.find_element_by_xpath('//span[contains(@id,"extra_icon_5")]').click()
        self.driver.find_element_by_xpath('//span[contains(@id,"extra_icon_6")]').click()

        time.sleep(5)
        self.driver.find_element_by_name('ProfileName').send_keys('AutoTestProfile')
        self.driver.find_element_by_xpath('//div[@class="selectItemText"]').click()

        self.driver.find_element_by_id('isc_PickListMenu_0_row_0').click()
        self.driver.find_element_by_name('ProfileDescription').send_keys('Automation')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()