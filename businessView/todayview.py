from common.desired_caps import appium_desired
from businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging,time


class Today(HomeView):

    today_share = (By.ID,'com.palm.test:id/iv_today_share')
    today_quote = (By.ID,'com.palm.test:id/tv_today_quote')

    today_tarot1 = (By.ID,'com.palm.test:id/iv_tarot1')
    today_tarot2 = (By.ID,'com.palm.test:id/iv_tarot2')
    today_tarot3 = (By.ID,'com.palm.test:id/iv_tarot3')

    today_close = (By.ID,'com.palm.test:id/iv_today_close')


    def today_page_enter(self):
        self.switch_navigation_today()
        logging.info('=======enter today page======')
        time.sleep(1)
        logging.info('=======check today page======')
        try:
            self.driver.find_element(*self.today_quote)
        except NoSuchElementException:
            print('can not find the today page')
            return False
        else:
            print('now in today page')
            return True



    def today_get_one_tarot(self):
        self.switch_navigation_today()
        logging.info('=======get one tarot======')
        logging.info('=======start swipe page=======')
        self.swipeDown()
        self.swipeDown()
        # self.driver.find_element_by_android_uiautomator(
        # 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().id("com.palm.test:id/iv_tarot1").instance(0));'
        # # ).click()
        logging.info('=====start get first tarot======')
        try:
            first_tarot = self.driver.find_element(*self.today_tarot1)
        except:
            print('can not find the first tarot')
            return False
        else:
            first_tarot.click()
        first_tarot_information = WebDriverWait(self.driver,10,1).until(
            EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_today_close')))
        self.getScreenShot('first tarot information')
        first_tarot_information.click()
        time.sleep(2)
        self.getScreenShot('get first tarot')
        return True

    def today_get_two_tarot(self):
        self.switch_navigation_today()
        logging.info('=======get first tarot======')
        logging.info('=======start swipe page=======')
        self.swipeDown()
        self.swipeDown()
        logging.info('=====start get first tarot======')
        try:
            first_tarot = self.driver.find_element(*self.today_tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first_tarot.click()
        first_tarot_information = WebDriverWait(self.driver, 10, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_today_close')))
        self.getScreenShot('first tarot information')
        first_tarot_information.click()
        time.sleep(2)
        self.getScreenShot('get first tarot')

        logging.info('=======get second tarot======')
        logging.info('=====start get second tarot======')
        try:
            second_tarot = self.driver.find_element(*self.today_tarot2)
        except NoSuchElementException:
            print('can not find the second tarot')
            return False
        else:
            second_tarot.click()
        second_tarot_information = WebDriverWait(self.driver,10,1).until(
            EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_today_close')))
        self.getScreenShot('second tarot information')
        second_tarot_information.click()
        time.sleep(2)
        self.getScreenShot('get second tarot')
        return True

    def today_get_three_tarot(self):
        self.switch_navigation_today()
        logging.info('=======get first tarot======')
        logging.info('=======start swipe page=======')
        self.swipeDown()
        self.swipeDown()
        logging.info('=====start get first tarot======')
        try:
            first_tarot = self.driver.find_element(*self.today_tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first_tarot.click()
        first_tarot_information = WebDriverWait(self.driver, 10, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_today_close')))
        self.getScreenShot('first tarot information')
        first_tarot_information.click()
        time.sleep(2)
        self.getScreenShot('get first tarot')

        logging.info('=======get second tarot======')
        logging.info('=====start get second tarot======')
        try:
            second_tarot = self.driver.find_element(*self.today_tarot2)
        except NoSuchElementException:
            print('can not find the second tarot')
            return False
        else:
            second_tarot.click()
        second_tarot_information = WebDriverWait(self.driver, 10, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_today_close')))
        self.getScreenShot('second tarot information')
        second_tarot_information.click()
        time.sleep(2)
        self.getScreenShot('get second tarot')

        logging.info('=======get third tarot======')
        logging.info('=====start get third tarot======')
        try:
            third_tarot = self.driver.find_element(*self.today_tarot3)
        except NoSuchElementException:
            print('can not find the third tarot')
            return False
        else:
            third_tarot.click()
        third_tarot_information = WebDriverWait(self.driver,10,1).until(
            EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_today_close')))
        self.getScreenShot('third tarot information')
        third_tarot_information.click()
        time.sleep(2)
        self.getScreenShot('get third tarot')
        return True

    def today_page_share(self):
        self.switch_navigation_today()
        logging.info('=======check share button======')
        try:
            share_button = self.driver.find_element(*self.today_share)
        except NoSuchElementException:
            print('can not find the share button')
            return False
        else:
            share_button.click()
            time.sleep(1)
            self.getScreenShot('share page')
            self.driver.keyevent(4)
            return True

if __name__ == '__main__':
    driver = appium_desired()
    l = Today(driver)
    # l.today_page_enter()
    # l.today_page_share()
    l.today_get_one_tarot()
    # l.today_get_two_tarot()
    # l.today_get_three_tarot()