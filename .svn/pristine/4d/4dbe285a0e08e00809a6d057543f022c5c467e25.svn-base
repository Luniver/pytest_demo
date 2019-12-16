from common.desired_caps import appium_desired
from common.common_fun import Commom
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By


class Loginview(Commom):
    nextBtn = (By.ID,'com.palm.test:id/tv_app_next')
    username = (By.ID,'com.palm.test:id/et1')
    birthday_selectBtn = (By.ID,'com.palm.test:id/et2')
    Constellation = (By.ID,'com.palm.test:id/et3')
    maleBtn = (By.ID,'com.palm.test:id/tv_appinfo_male')
    femaleBtn = (By.ID,'com.palm.test:id/tv_appinfo_female')

    # years = (By.ID,'android:id/date_picker_header_year')
    # next_month = (By.ID,'android:id/next')
    # prev_month = (By.ID,'android:id/prev')
    # sure = (By.ID,'android:id/button1')
    # cancel = (By.ID,'android:id/button2')
    # year2018 = (By.XPATH,'//*[@text="2018"]')
    # day22 = (By.XPATH,'//*[@text="22"]')
    #
    def username_input(self,username):
        '''填写用户名'''
        logging.info('========input username========')
        try:
            usernametext = self.driver.find_element(*self.username)
        except NoSuchElementException:
            print('can not find username input')
            return False
        else:
            usernametext.clear()
            usernametext.send_keys(username)
            return True
    #
    # def birthday_select(self):
    #     '''选择生日，星座'''
    #     logging.info('========select birthday=======')
    #     #点击输入生日
    #     try:
    #         birthday_select = self.driver.find_element(*self.birthday_selectBtn)
    #     except NoSuchElementException:
    #         print('can not find birthday_select input')
    #         return False
    #     else:
    #         birthday_select.click()
    #
    #
    #     logging.info('========click years to choose=======')
    #     #点击选择年份
    #     try:
    #         years = self.driver.find_element(*self.years)
    #     except NoSuchElementException:
    #         print('can not find the years choose')
    #         return False
    #     else:
    #         years.click()
    #
    #     logging.info('========choose years========')
    #     #选择年份
    #     try:
    #         yearchoose = self.driver.find_element(*self.year2018)
    #     except NoSuchElementException:
    #         print('can not find the year2018')
    #         return False
    #     else:
    #         yearchoose.click()
    #
    #     logging.info('========select month========')
    #     #选择上一个月
    #     try:
    #         prev_month = self.driver.find_element(*self.prev_month)
    #     except NoSuchElementException:
    #         print('can not find the prev_month')
    #         return False
    #     else:
    #         prev_month.click()
    #
    #     logging.info('========select day========')
    #     #选这日期
    #     try:
    #         day = self.driver.find_element(*self.day22)
    #     except NoSuchElementException:
    #         print('can not find the day22')
    #         return False
    #     else:
    #         day.click()
    #
    #     logging.info('=======sure click=========')
    #     #确认点击
    #     try:
    #         sureBtn = self.driver.find_element(*self.sure)
    #     except NoSuchElementException:
    #         print('can not find the sureBtn')
    #         return False
    #     else:
    #         sureBtn.click()
    #         logging.info('========auto select Constellation======')
    #         return True
    #
    # def male_select(self):
    #     '''男性选择'''
    #     logging.info('========sexual set male===========')
    #     try:
    #         maleBtn = self.driver.find_element(*self.maleBtn)
    #     except NoSuchElementException:
    #         print('no maleBtn to choose')
    #         return False
    #     else:
    #         maleBtn.click()
    #         return True
    #
    # def female_select(self):
    #     '''女性选择'''
    #     logging.info('========sexual set female==========')
    #     try:
    #         femaleBtn = self.driver.find_element(*self.femaleBtn)
    #     except NoSuchElementException:
    #         print('no femaleBtn to choose')
    #         return False
    #     else:
    #         femaleBtn.click()
    #         return True

    def next_button(self):
        '''下一个按钮'''
        logging.info('========next_button click===========')
        try:
            nextBtn= self.driver.find_element(*self.nextBtn)
        except NoSuchElementException:
            print('can not find the next button')
            return False
        else:
            nextBtn.click()
            return True

if __name__ == '__main__':
    driver = appium_desired()
    l = Loginview(driver)
    l.username_input('lichenyu')
    l.birthday_select()
    l.male_select()
    l.getScreenShot('loginpage')
    l.next_button()
    l.allow_event()
    l.back_event()
    l.close_event()





