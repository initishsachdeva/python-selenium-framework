import pytest

from pageObjects.LoginPage import Login
from services.CustomLogger import BaseClass
from services.ReadConfigINIFile import ReadConfig
from services.Utils import Utils


@pytest.mark.Login
class TestLogin(BaseClass):
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # Verify the user is able to login and navigate to default landing page with correct username and password
    def test_login001(self):
        log = self.getLogger()
        loginPage = Login(self.driver)
        log.info("******** test_login001 execution started ********")
        loginPage.enterUserName(self.username)
        loginPage.enterPassword(self.password)
        loginPage.clickLogin()
        assert "Accounts Overview" == loginPage.landingPage()
        loginPage.clickLogOut()
        log.info("******** test_login001 execution completed ********")

    # Verify the user is not able to log in with the incorrect username and password
    def test_login002(self):
        log = self.getLogger()
        loginPage = Login(self.driver)
        utils = Utils(self)
        log.info("******** test_login002 execution started ********")
        loginPage.enterUserName("bravo")
        loginPage.enterPassword("bravo1234")
        loginPage.clickLogin()
        assert "Error!" == loginPage.landingPage()
        log.info("******** test_login002 execution completed ********")
