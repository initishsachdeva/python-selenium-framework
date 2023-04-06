from selenium.webdriver.common.by import By


class Login:
    usernameInput = (By.XPATH, "//*[@class='login']/input[1]")
    passwordInput = (By.XPATH, "//*[@class='login']/input[@type='password']")
    logInBtn = (By.XPATH, "//*[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(*Login.usernameInput).clear()
        self.driver.find_element(*Login.usernameInput).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*Login.usernameInput).clear()
        self.driver.find_element(*Login.passwordInput).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*Login.logInBtn).click()
