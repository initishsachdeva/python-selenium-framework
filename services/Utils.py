import pytest
import allure
from allure_commons.types import AttachmentType


class Utils:

    def __init__(self, driver):
        self.driver = driver

    def takeScreenshot(self, name):
        try:
            self.driver.save_screenshot(".\\screenshots\\" + name + ".png")
        except Exception as e:
            pytest.fail("unable to save the screenshot", e)

    def takeAllureScreenshot(self, screenshotname):
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotname,
                          attachment_type=AttachmentType.PNG)
        except Exception as e:
            pytest.fail("unable to save the screenshot", e)
