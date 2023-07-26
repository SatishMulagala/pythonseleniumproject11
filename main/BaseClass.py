import logging
import pytest
@pytest.mark.usefixtures("setup")
class TestBaseClass:
    def get_logger(self):
        logs = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('..//..//Logs//logfile.log')
        format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(message)s")
        logs.setLevel(logging.DEBUG)
        fileHandler.setFormatter(format)
        logs.addHandler(fileHandler)
        return logs

    # def closeIframeOption(self,driver):
    #     driver.switch_to.default_content()

    def takescreenshot(self, driver):
        driver.save_screenshot("..//..//screenshot//result1.png")

    # def setup(request):
    #     global DRIVER
    #     DRIVER = webdriver.Chrome()
    #     print("DRIVER setUp: ", DRIVER)
