import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




class EnvironmentSetup(unittest.TestCase):
    # global logger
    #
    # logging.basicConfig(filename="../Logs/linkmanager.log",format='%(asctime)s %(message)s', filemode='w')  # Create and configure logger
    # logger = logging.getLogger()  # Creating an object
    # logger.setLevel(logging.DEBUG)

    @classmethod
    def setUpClass(cls):
        driver_path = '../Resources/browserDriver/chromedriver.exe'
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(10)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Environment has Initialized')
        print('Automation Started at', str(datetime.now()))

        url = 'http://192.168.1.154:8989'
        print(' Url open into browser')
        cls.driver.get(url)
        cls.driver.set_page_load_timeout(20)
        sleep(10)

    @classmethod
    def tearDownClass(cls):
        if (cls.driver != None):
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Environment has Destroyed')
            print('Automation Started at', str(datetime.now()))
            cls.driver.close()
            cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
