import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging

class TestBase(unittest.TestCase):
    global driver
    global logger

    logging.basicConfig(filename="audit.log", format='%(asctime)s %(message)s', filemode='w')  # Create and configure logger
    logger = logging.getLogger()  # Creating an object
    logger.setLevel(logging.DEBUG)

    driver = webdriver.Chrome(executable_path='C:/Users/Ashok/PycharmProjects/Auto_framework/Resources/browserDriver/chromedriver.exe',
            desired_capabilities=DesiredCapabilities.CHROME.clear())

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        cls.driver.maximize_window()

    def setUp(self):
        logging.info('LMO Application url is lunched')
        self.driver.get('http://192.168.1.154:8989')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
