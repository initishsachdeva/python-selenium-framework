from pageObjects.LoginPage import Login
from services.CustomLogger import BaseClass
from services.ReadConfigINIFile import ReadConfig


class TestLogin(BaseClass):
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_login(self):
        log = self.getLogger()
        loginPage = Login(self.driver)
        log.info("executing test login")
        loginPage.setUserName(self.username)
        loginPage.setPassword(self.password)
        loginPage.clickLogin()
