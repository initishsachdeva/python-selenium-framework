import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class Login:
    usernameInput = (By.XPATH, "//*[@class='login']/input[1]")
    passwordInput = (By.XPATH, "//*[@class='login']/input[@type='password']")
    logInBtn = (By.XPATH, "//*[@type='submit']")
    logOut = (By.XPATH, "//*[text()='Log Out']")
    landingPageTitle = (By.XPATH, "//*[@class='title']")

    def __init__(self, driver):
        self.driver = driver

    def enterUserName(self, username):
        try:
            self.driver.find_element(*Login.usernameInput).clear()
            self.driver.find_element(*Login.usernameInput).send_keys(username)
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name=self.enterUserName.__name__,
                          attachment_type=AttachmentType.PNG)
            pytest.fail("unable to enter username in the given field", e)

    def enterPassword(self, password):
        try:
            self.driver.find_element(*Login.passwordInput).clear()
            self.driver.find_element(*Login.passwordInput).send_keys(password)
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name=self.enterPassword.__name__,
                          attachment_type=AttachmentType.PNG)
            pytest.fail("unable to enter password in the given field", e)

    def clickLogin(self):
        try:
            self.driver.find_element(*Login.logInBtn).click()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name=self.clickLogin.__name__,
                          attachment_type=AttachmentType.PNG)
            pytest.fail("unable to click on login button", e)

    def landingPage(self):
        try:
            title = self.driver.find_element(*Login.landingPageTitle).text
            return title
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name=self.landingPage.__name__,
                          attachment_type=AttachmentType.PNG)
            pytest.fail("unable to get the title of landing page", e)

    def clickLogOut(self):
        try:
            self.driver.find_element(*Login.logOut).click()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name=self.clickLogOut.__name__,
                          attachment_type=AttachmentType.PNG)
            pytest.fail("unable to click on logout button", e)

    def login(self, username, password):
        try:
            self.enterUserName(username)
            self.enterPassword(password)
            self.clickLogin()
        except Exception as e:
            pytest.fail("unable to login into the application", e)
