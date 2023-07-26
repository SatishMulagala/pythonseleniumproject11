import pytest
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from main.BaseClass import TestBaseClass
from main.objects.BookingPage import BookingPage
from main.objects.LoginPage import LoginPage
from main.utilities.DBConnectionFile import DBConnectionFile


@pytest.mark.usefixtures("setup")
class TestBooking(TestBaseClass):

    def test_booking(self):
        logs = self.get_logger()
        try:
            logs.debug('Browser Launched New one')
            db = DBConnectionFile()
            data = db.dbconnect()
            # path = Service("C:\\Users\\Satish\\Downloads")
            # driver = webdriver.Chrome(service=path)
            # driver.get("https://www.makemytrip.com/")
            logs.debug('Website opened')
            time.sleep(15)
            frameList = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
            self.driver.switch_to.frame(frameList[3])
            time.sleep(2)
            self.driver.execute_script("document.elementFromPoint(0,0).click()")
            time.sleep(2)
            # driver.implicitly_wait(10)
            # driver.maximize_window()
            # login = LoginPage(self.driver)
            # # login.adFrameOption().click()
            # login.usernameInputOption().send_keys(data[2])
            # login.continueBtnOption().click()
            # #otp = input()
            # login.otpInputOption().send_keys(data[3])
            # self.driver.implicitly_wait(30)
            # logs.debug('OTP entered')
            # login.loginBtnOption().click()
            self.driver.execute_script("document.elementFromPoint(0,0).click()")
            bookObj = BookingPage(self.driver)
            bookObj.fromButtonOption().click()
            bookObj.fromInputOption().send_keys(data[0])
            bookObj.fromCityOption().click()
            logs.debug('From city selected')
            bookObj.toButtonOption().click()
            bookObj.toInputOption().send_keys(data[1])
            bookObj.toCityOption().click()
            logs.debug('To city selected')
            bookObj.nextBtnOption().click()
            time.sleep(3)
            dates = bookObj.dateChoicesOption()
            for d in dates:
                e = d.find_element(By.TAG_NAME, value="p")
                if e.text == '15':
                    e.click()
                    break
            logs.debug('Dates got selected')
            bookObj.classTravelOption().click()
            bookObj.adultTktsOption().click()
            bookObj.childTktsOption().click()
            logs.debug('Passengers selected')
            bookObj.applyTktsOption().click()
            bookObj.searchFlightOption().click()
            bookObj.adPopupOption().click()
            self.takescreenshot(self.driver)
            logs.debug('Successful booking')
        except Exception as ex:
            logs.error("Exception occurred", ex)
            self.takescreenshot(self.driver)










        # bookObj.calendarDateOption()
        # time.sleep(2)
        # sel_Date = input('Please enter the date, format should be Day Mon Date Year(Ex.Sun Jan 23 2023):')
        # bookObj.bookingDateOption(sel_Date)
        # time.sleep(5)

        # driver.find_element(By.XPATH,value="//input[@placeholder='From']").send_keys("Pune")
        # time.sleep(3)
        # driver.find_elements(By.CLASS_NAME, value="calc60")[0].click()
        # time.sleep(3)
        # driver.find_element(By.XPATH, value="//span[text()='To']").click()
        # time.sleep(3)
        # driver.find_element(By.XPATH, value="//input[@placeholder='To']").send_keys("Chandigarh")
        # time.sleep(3)
        # driver.find_elements(By.CLASS_NAME, value="calc60")[0].click()


# class TestBooking(TestBaseClass):
#     def test_getlogs(self):
#         path = Service("C:\\Users\\Satish\\Downloads")
#         driver = webdriver.Chrome(service=path)
#         driver.get("https://www.makemytrip.com/")
#         logs = self.get_logger()
#         logs.debug('Browser Launched')
#         time.sleep(5)


'''class TestBooking(TestBaseClass):
    def get_logger(self):
        logs = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(message)s")
        logs.setLevel(logging.DEBUG)
        fileHandler.setFormatter(format)
        logs.addHandler(fileHandler)
        return logs'''
