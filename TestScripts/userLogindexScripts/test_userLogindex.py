import unittest
from TestBase.EnvironmentSetup import EnvironmentSetup
from PageObjects.blmoPages.LMO_LogindexPage import Logindex
from PageObjects.locators.Locator import Locator
import pytest

class Scripts_userLogin(EnvironmentSetup):

    @pytest.mark.Smoke
    def test_userAdmin(self):
        driver = self.driver
        print('Administator user login testcase')
        login = Logindex(driver)
        try:
            login.getUsername('admin')
            login.getPassword('admin')
            login.getRoleAdministrator()
            login.getSignIn()
            driver.implicitly_wait(30)
            print('User login Successfully')
        except ValueError as e:
            print('Error is ',e)
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
