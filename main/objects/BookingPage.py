from selenium.webdriver.common.by import By
class BookingPage:
    driver = ''
    def __init__(self, driver):
        self.driver = driver
    fromButton = (By.ID, "fromCity")
    fromInput = (By.XPATH, "//input[@placeholder='From']")
    fromCity = (By.XPATH, "//div[@class='calc60']//p[contains(text(),'Pune')]")
    toButton = (By.ID, "toCity")
    toInput = (By.XPATH, "//input[@placeholder='To']")
    toCity = (By.XPATH, "//div[@class='calc60']//p[contains(text(),'Chandigarh')]")
    nextBtn = (By.CLASS_NAME, "DayPicker-NavButton--next")
    datesChoices = (By.XPATH, "//div[@class='dateInnerCell']")
    #calendarDates = (By.XPATH, "//div[@class='DayPicker-Months']//div[@class='DayPicker-Day']")
    classTravel= (By.XPATH, "//span[@class='lbl_input appendBottom5']")
    adultTkts= (By.XPATH,"//div[@class='travellers gbTravellers']//li[text()='2']")
    childTkts= (By.XPATH, "//div[@class='makeFlex column childCounter']//li[text()='1']")
    applyTkts=(By.XPATH, "//button[text()='APPLY']")
    searchFlight=(By.XPATH,"//a[text()='Search']")
    adPopup=(By.XPATH, "//button[text()='OKAY, GOT IT!']")
    def fromButtonOption(self):
        return self.driver.find_element(*BookingPage.fromButton)
    def fromInputOption(self):
        return self.driver.find_element(*BookingPage.fromInput)
    def fromCityOption(self):
        return self.driver.find_element(*BookingPage.fromCity)
    def toButtonOption(self):
        return self.driver.find_element(*BookingPage.toButton)
    def toInputOption(self):
        return self.driver.find_element(*BookingPage.toInput)
    def toCityOption(self):
        return self.driver.find_element(*BookingPage.toCity)
    def dateChoicesOption(self):
        return self.driver.find_elements(*BookingPage.datesChoices)
    def nextBtnOption(self):
        return self.driver.find_element(*BookingPage.nextBtn)
    def classTravelOption(self):
        return self.driver.find_element(*BookingPage.classTravel)
    def adultTktsOption(self):
        return self.driver.find_element(*BookingPage.adultTkts)
    def childTktsOption(self):
        return self.driver.find_element(*BookingPage.childTkts)
    def applyTktsOption(self):
        return self.driver.find_element(*BookingPage.applyTkts)
    def searchFlightOption(self):
        return self.driver.find_element(*BookingPage.searchFlight)
    def adPopupOption(self):
        return self.driver.find_element(*BookingPage.adPopup)










    # def calendarDateOption(self,dates1):
    #     return self.driver.find_elements(*BookingPage.calendarDates)
    #
    # def bookingDateOption(self, calendarDates):
    #     for bkdDate in calendarDates:
    #         if bkdDate.get_attribute('aria-label') == self.sel_date:
    #             bkdDate.click()
    #             break
    #         return bkdDate

    # cal_dates = driver.find_elements(by=By.XPATH, value="//div[@class='DayPicker-Months']//div[@class='DayPicker-Day']")
    #  print(bkd_dates)
    # sel_Date = input('Please enter the date, format should be Day Mon Date Year(Ex.Sun Jan 23 2023):')
    # time.sleep(8)
    # for bkdDate in cal_dates:
    #     if bkdDate.get_attribute('aria-label') == sel_Date:
    #         bkdDate.click()
    #         break
    # time.sleep(3)
    # driver.find_element(by=By.XPATH, value="//span[@class='lbl_input appendBottom5']").click()
    # time.sleep(2)
    # driver.find_element(by=By.XPATH, value="//div[@class='travellers gbTravellers']//li[text()='2']").click()
    # time.sleep(2)
    # driver.find_element(by=By.XPATH, value="//div[@class='makeFlex column childCounter']//li[text()='1']").click()
    # time.sleep(2)
    # driver.find_element(by=By.XPATH, value="//button[text()='APPLY']").click()
    # time.sleep(2)
    # driver.find_element(by=By.XPATH, value="//a[text()='Search']").click()
    # time.sleep(10)
    # driver.find_element(by=By.XPATH, value="//button[text()='OKAY, GOT IT!']").click()
    # time.sleep(2)
