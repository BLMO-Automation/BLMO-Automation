# import os
#
# dpath = '/Resources/browserDriver/chromedriver.exe'
# print(os.getcwd())
# abs = os.path.abspath(__file__)
# print(os.path.dirname(abs))


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://google.com')
driver.implicitly_wait(30)
driver.close()
driver.quit()