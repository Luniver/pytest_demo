from common.desired_caps import appium_desired
from common.common_fun import Commom
import logging,time
from selenium.webdriver.common.by import By

class HomeView(Commom):

    item_image = (By.ID,'com.palm.test:id/rl_bg')
    navigation_home = (By.ID,'com.palm.test:id/ll_tab_home')
    navigation_today = (By.ID,'com.palm.test:id/ll_tab_today')
    navigation_me = (By.ID,'com.palm.test:id/ll_tab_me')
    closeBtn = (By.ID, 'com.palm.test:id/iv_payment_close')

    def switch_navigation_home(self):
        '''切换至首页'''
        logging.info('========APP enter=======')
        self.first_close_event()
        self.driver.find_element(*self.navigation_home).click()
        logging.info('=======switch_home======')
        time.sleep(2)
        # self.getScreenShot('home_page')
        return True

    def switch_navigation_today(self):
        '''切换至今日'''
        logging.info('========APP enter=======')
        self.first_close_event()
        self.driver.find_element(*self.navigation_today).click()
        logging.info('=======switch_today======')
        time.sleep(2)
        # self.getScreenShot('today_page')
        return True

    def switch_navigation_me(self):
        '''切换到我的'''
        logging.info('========APP enter=======')
        self.first_close_event()
        self.driver.find_element(*self.navigation_me).click()
        logging.info('======switch_me======')
        time.sleep(2)
        # self.getScreenShot('me_page')
        return True

    def switch_palm(self):
        '''切换到手相功能页'''
        logging.info('=======APP enter======')
        self.first_close_event()
        self.driver.find_elements(*self.item_image)[1].click()
        logging.info('=====switch_palm======')
        time.sleep(2)
        # self.getScreenShot('palm_home')
        return True

    def switch_Constellation(self):
        '''切换到星座功能页'''
        logging.info('========APP enter=======')
        self.first_close_event()
        self.driver.find_elements(*self.item_image)[2].click()
        logging.info('======swicth_constellation======')
        time.sleep(2)
        self.getScreenShot('constellation_home')
        return True

    def switch_tarot(self):
        '''切换到塔罗牌功能页'''
        logging.info('========APP enter=======')
        self.first_close_event()
        self.driver.find_elements(*self.item_image)[3].click()
        logging.info('======switch tarot=====')
        time.sleep(2)
        # self.getScreenShot('tarot_home')
        return True

    def switch_face(self):
        '''切换到变老功能页'''
        logging.info('========APP enter=======')
        self.first_close_event()
        self.driver.find_elements(*self.item_image)[0].click()
        logging.info('======switch face======')
        time.sleep(2)
        # self.getScreenShot('face_home')
        return True

    def switch_psychological_test(self):
        '''切换至心理测试功能页'''
        logging.info('========APP enter=======')
        self.first_close_event()
        self.driver.find_elements(*self.item_image)[4].click()
        logging.info('======switch psychological_test=======')
        time.sleep(2)
        # self.getScreenShot('psychological_test page')
        return True



if __name__ == '__main__':
    driver = appium_desired()
    l = HomeView(driver)
    # l.switch_navigation_home()
    # l.switch_navigation_today()
    # l.switch_navigation_me()
    l.switch_palm()
    # l.switch_Constellation()
    # l.switch_tarot()
    # l.switch_face()
    # l.switch_psychological_test()






