from common.desired_caps import appium_desired
from businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging

class MePage(HomeView):

    me_name = (By.ID,"com.palm.test:id/me_name")
    me_constellation = (By.ID,"com.palm.test:id/me_constellation")
    me_birthday = (By.ID,"com.palm.test:id/me_date")
    done = (By.ID, 'com.palm.test:id/tv_titlebar_text')
    edit = (By.ID, 'com.palm.test:id/me_edit_btn')

    me_et_name = (By.ID, 'com.palm.test:id/me_et_name')
    me_et_birthday = (By.ID, 'com.palm.test:id/me_et_birthday')
    me_et_male = (By.ID, 'com.palm.test:id/me_tv_male')
    me_et_female = (By.ID, 'com.palm.test:id/me_tv_female')


    def information_edit_enter(self):
        '''个人信息修改'''
        logging.info('==========edit enter==========')
        try:
            edit = self.driver.find_element(*self.edit)
        except NoSuchElementException:
            print('can not find the edit')
            return False
        else:
            edit.click()
            return True

    def information_done(self):
        logging.info('========personal information finished=========')
        try:
            Done = self.driver.find_element(*self.done)
        except NoSuchElementException:
            print('can not find the Done or can not click')
            return False
        else:
            assert Done.is_enabled() == True
            Done.click()
            return True

