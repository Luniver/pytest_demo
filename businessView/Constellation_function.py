from common.desired_caps import appium_desired
from businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging,time,os

class Constellation(HomeView):

    constellation_everday = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_constellation"]/android.widget.FrameLayout[1]')
    constellation_match = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_constellation"]/android.widget.FrameLayout[2]')

    subscribe_button = (By.ID, 'com.palm.test:id/btn_pay')

    month_button = (By.ID,'com.palm.test:id/view_payment_btn2')
    year_button = (By.ID,'com.palm.test:id/view_payment_btn1')
    GP_subscribe_button = (By.ID,'com.android.vending:id/footer_placeholder')
    constellation = (By.ID,'com.palm.test:id/iv_cntselect_cnt')


    result_title = (By.ID,'com.palm.test:id/tv_titlebar_title')
    everyday_result_title = (By.ID,'com.palm.test:id/iv_cntdaily_cnt')

    today = (By.ID,'com.palm.test:id/tv_cntdaily_today')
    tomorrow = (By.ID,'com.palm.test:id/tv_cntdaily_tomorrow')
    future = (By.ID,'com.palm.test:id/tv_cntdaily_future')
    more = (By.ID,'com.palm.test:id/tv_cntdaily_more')

    edit = (By.ID,'com.palm.test:id/me_edit_btn')
    Done = (By.ID,'com.palm.test:id/tv_titlebar_text')



    def everyday_costellation_enter(self):
        '''每日星座功能进入'''
        logging.info('============select and enter everyday constellation==========')
        self.switch_navigation_me()
        logging.info('==========edit personal information==========')
        try:
            edit = self.driver.find_element(*self.edit)
        except NoSuchElementException:
            print('can not find the edit')
            return False
        else:
            edit.click()

        self.username_edit('lichenyu')
        self.birthday_select()
        self.male_select()
        logging.info('========personal information finished=========')
        try:
            Done = self.driver.find_element(*self.Done)
        except NoSuchElementException:
            print('can not find the Done or can not click')
            return False
        else:
            Done.click()
            time.sleep(2)
            self.getScreenShot('personal information')

        logging.info('==========go to the home page===========')
        try:
            homePage = self.driver.find_element(*self.navigation_home)
        except NoSuchElementException:
            print('can not find the home page')
            return False
        else:
            homePage.click()
        time.sleep(2)

        logging.info('=========go to the constellation home page========')
        try:
            constelllation = self.driver.find_elements(*self.item_image)[2]
        except NoSuchElementException:
            print('can not find the constellation page')
            return False
        else:
            constelllation.click()
        time.sleep(2)
        logging.info('=========go to the constellation everyday=========')

        try:
            constellation_everyday = self.driver.find_element(*self.constellation_everday)
        except NoSuchElementException:
            print('can not find the constellation everyday')
        else:
            constellation_everyday.click()
        time.sleep(2)

        self.getScreenShot('constellation everyday page')
        return True

    def everyday_constellation_today(self):
        '''每日星座今日界面'''
        self.switch_navigation_me()
        logging.info('==========edit personal information==========')
        try:
            edit = self.driver.find_element(*self.edit)
        except NoSuchElementException:
            print('can not find the edit')
            return  False
        else:
            edit.click()

        self.username_edit('lichenyu')
        self.birthday_select()
        self.male_select()
        logging.info('========personal information finished=========')
        try:
            Done = self.driver.find_element(*self.Done)
        except NoSuchElementException:
            print('can not find the Done or can not click')
            return False
        else:
            Done.click()
            time.sleep(2)
            self.getScreenShot('personal information')

        logging.info('==========go to the home page===========')
        try:
            homePage = self.driver.find_element(*self.navigation_home)
        except NoSuchElementException:
            print('can not find the home page')
            return False
        else:
            homePage.click()
        time.sleep(2)

        logging.info('=========go to the constellation home page========')
        try:
            constelllation = self.driver.find_elements(*self.item_image)[2]
        except NoSuchElementException:
            print('can not find the constellation page')
            return False
        else:
            constelllation.click()
        time.sleep(2)
        logging.info('=========go to the constellation everyday=========')

        try:
            constellation_everyday = self.driver.find_element(*self.constellation_everday)
        except NoSuchElementException:
            print('can not find the constellation everyday')
        else:
            constellation_everyday.click()
        time.sleep(2)

        logging.info('===========enter everyday constellation today page===========')
        try:
            today = self.driver.find_element(*self.today)
        except NoSuchElementException:
            print('can not find the today')
            return False
        else:
            today.click()
            time.sleep(2)
            self.getScreenShot('constellation today page')
            return True

    def everyday_constellation_tomorrow(self):
        '''每日星座明日界面'''
        self.switch_navigation_me()
        logging.info('==========edit personal information==========')
        try:
            edit = self.driver.find_element(*self.edit)
        except NoSuchElementException:
            print('can not find the edit')
            return False
        else:
            edit.click()

        self.username_edit('lichenyu')
        self.birthday_select()
        self.male_select()
        logging.info('========personal information finished=========')
        try:
            Done = self.driver.find_element(*self.Done)
        except NoSuchElementException:
            print('can not find the Done or can not click')
            return False
        else:
            Done.click()
            time.sleep(2)
            self.getScreenShot('personal information')

        logging.info('==========go to the home page===========')
        try:
            homePage = self.driver.find_element(*self.navigation_home)
        except NoSuchElementException:
            print('can not find the home page')
            return False
        else:
            homePage.click()
        time.sleep(2)

        logging.info('=========go to the constellation home page========')
        try:
            constelllation = self.driver.find_elements(*self.item_image)[2]
        except NoSuchElementException:
            print('can not find the constellation page')
            return False
        else:
            constelllation.click()
        time.sleep(2)
        logging.info('=========go to the constellation everyday=========')

        try:
            constellation_everyday = self.driver.find_element(*self.constellation_everday)
        except NoSuchElementException:
            print('can not find the constellation everyday')
        else:
            constellation_everyday.click()
        time.sleep(2)

        logging.info('=========enter everyday constellation tomorrow page=========')
        try:
            tomorrow = self.driver.find_element(*self.tomorrow)
        except NoSuchElementException:
            print('can not find the tomorrow')
            return False
        else:
            tomorrow.click()
            time.sleep(2)
            self.getScreenShot('constellation tomorrow page')
            return True

    def everyday_constellation_future(self):
        '''每日星座未来界面'''
        self.switch_navigation_me()
        logging.info('==========edit personal information==========')
        try:
            edit = self.driver.find_element(*self.edit)
        except NoSuchElementException:
            print('can not find the edit')
            return False
        else:
            edit.click()

        self.username_edit('lichenyu')
        self.birthday_select()
        self.male_select()
        logging.info('========personal information finished=========')
        try:
            Done = self.driver.find_element(*self.Done)
        except NoSuchElementException:
            print('can not find the Done or can not click')
            return False
        else:
            Done.click()
            time.sleep(2)
            self.getScreenShot('personal information')

        logging.info('==========go to the home page===========')
        try:
            homePage = self.driver.find_element(*self.navigation_home)
        except NoSuchElementException:
            print('can not find the home page')
            return False
        else:
            homePage.click()
        time.sleep(2)

        logging.info('=========go to the constellation home page========')
        try:
            constelllation = self.driver.find_elements(*self.item_image)[2]
        except NoSuchElementException:
            print('can not find the constellation page')
            return False
        else:
            constelllation.click()
        time.sleep(2)
        logging.info('=========go to the constellation everyday=========')

        try:
            constellation_everyday = self.driver.find_element(*self.constellation_everday)
        except NoSuchElementException:
            print('can not find the constellation everyday')
        else:
            constellation_everyday.click()
        time.sleep(2)

        logging.info('==========enter everyday constellation future page==========')
        try:
            future = self.driver.find_element(*self.future)
        except NoSuchElementException:
            print('can not find the future')
            return False
        else:
            future.click()
            time.sleep(2)
            self.getScreenShot('constellation future page')
            return True

    def everyday_constellation_more(self):
        '''每日星座更多'''
        self.switch_navigation_me()
        logging.info('==========edit personal information==========')
        try:
            edit = self.driver.find_element(*self.edit)
        except NoSuchElementException:
            print('can not find the edit')
            return False
        else:
            edit.click()

        self.username_edit('lichenyu')
        self.birthday_select()
        self.male_select()
        logging.info('========personal information finished=========')
        try:
            Done = self.driver.find_element(*self.Done)
        except NoSuchElementException:
            print('can not find the Done or can not click')
            return False
        else:
            Done.click()
            time.sleep(2)
            self.getScreenShot('personal information')

        logging.info('==========go to the home page===========')
        try:
            homePage = self.driver.find_element(*self.navigation_home)
        except NoSuchElementException:
            print('can not find the home page')
            return False
        else:
            homePage.click()
        time.sleep(2)

        logging.info('=========go to the constellation home page========')
        try:
            constelllation = self.driver.find_elements(*self.item_image)[2]
        except NoSuchElementException:
            print('can not find the constellation page')
            return False
        else:
            constelllation.click()
        time.sleep(2)
        logging.info('=========go to the constellation everyday=========')

        try:
            constellation_everyday = self.driver.find_element(*self.constellation_everday)
        except NoSuchElementException:
            print('can not find the constellation everyday')
        else:
            constellation_everyday.click()
        time.sleep(2)

        logging.info('==========enter everyday constellation more page========')
        try:
            more = self.driver.find_element(*self.more)
        except NoSuchElementException:
            print('can not find the more')
            return False
        else:
            more.click()
            time.sleep(2)
            self.getScreenShot('constellation select page')
            return True


    def constellation_Match_enter(self):
        '''星座匹配界面功能进入'''
        self.switch_Constellation()
        logging.info('========select and enter constellation matching========')
        try:
            constellation_match = self.driver.find_element(*self.constellation_match)
        except NoSuchElementException:
            print('can not find the constellation matching')
            return False
        else:
            constellation_match.click()
            return True

    def same_Aries_match(self):
        '''白羊相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Aries match Aries=======')
        try:
            Aries_match = self.driver.find_elements(*self.constellation)[0]
        except NoSuchElementException:
            print('can not find the Aries')
            return False
        else:
            os.system('adb shell input tap 395 357')
            Aries_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Aries constellation match result')
                return True

    def same_Taurus_match(self):
        '''金牛相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Taurus match Taurus=======')
        try:
            Taurus_match = self.driver.find_elements(*self.constellation)[1]
        except NoSuchElementException:
            print('can not find the Taurus')
            return False
        else:
            os.system('adb shell input tap 395 357')
            Taurus_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Taurus constellation match result')
                return True

    def same_Gemini_match(self):
        '''双子相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Gemini match Gemini=======')
        try:
            Gemini_match = self.driver.find_elements(*self.constellation)[2]
        except NoSuchElementException:
            print('can not find the Gemini')
            return False
        else:
            os.system('adb shell input tap 395 357')
            Gemini_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Gemini constallation match result')
                return True

    def same_Cancer_match(self):
        '''巨蟹相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Cancer match Cancer=======')
        try:
            Cancer_match = self.driver.find_elements(*self.constellation)[3]
        except NoSuchElementException:
            print('can not find the Aries')
            return False
        else:
            os.system('adb shell input tap 395 357')
            Cancer_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Cancer constellation match result')
                return True

    def same_Leo_match(self):
        '''狮子相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Leo match Leo=======')
        try:
            Leo_match = self.driver.find_elements(*self.constellation)[4]
        except NoSuchElementException:
            print('can not find the Leo')
            return False
        else:
            os.system('adb shell input tap 395 357')
            Leo_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Leo constellation match result')
                return True

    def same_Virgo_match(self):
        '''处女相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Virgo match Virgo=======')
        try:
            Virgo_match = self.driver.find_elements(*self.constellation)[5]
        except NoSuchElementException:
            print('can not find the Virgo')
            return False
        else:
            os.system('adb shell input tap 395 357')#点击取消星座引导页面动画
            Virgo_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Virgo constellation match result')
                return True

    def same_Libra_match(self):
        '''天秤相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Libra match Libra=======')
        try:
            Libra_match = self.driver.find_elements(*self.constellation)[6]
        except NoSuchElementException:
            print('can not find the Libra')
            return False
        else:
            os.system('adb shell input tap 395 357')
            Libra_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Libra constellation match result')
                return True

    def same_Scorpio_match(self):
        '''天蝎相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Scorpio match Scorpio=======')
        try:
            Scorpio_match = self.driver.find_elements(*self.constellation)[7]
        except NoSuchElementException:
            print('can not find the Scorpio')
            return False
        else:
            os.system('adb shell input tap 395 357')
            Scorpio_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Scorpoio constellation match result')
                return True

    def same_Sagittarius_match(self):
        '''射手相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Sagittarius match Sagittarius=======')
        try:
            Sagittarius_match = self.driver.find_elements(*self.constellation)[8]
        except NoSuchElementException:
            print('can not find the Sagittarius')
            return False
        else:
            os.system('adb shell input tap 395 357')
            Sagittarius_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Sagittarius constellation match result')
                return True

    def same_Capricornus_match(self):
        '''摩羯相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Capricornus match Capricornus=======')
        try:
            Capricornus_match = self.driver.find_elements(*self.constellation)[9]
        except NoSuchElementException:
            print('can not find the Aries')
            return False
        else:
            os.system('adb shell input tap 395 357')
            Capricornus_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Capricornus constellation match result')
                return True

    def same_Aquarius_match(self):
        '''水瓶相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Aquarius match Aquarius=======')
        try:
            Aquarius_match = self.driver.find_elements(*self.constellation)[10]
        except NoSuchElementException:
            print('can not find the Aquarius')
            return False
        else:
            os.system('adb shell input tap 395 357')
            Aquarius_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Aquarius constellation match result')
                return True

    def same_Pisces_match(self):
        '''双鱼相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Pisces match Pisces=======')
        try:
            Pisces_match = self.driver.find_elements(*self.constellation)[11]
        except NoSuchElementException:
            print('can not find the Aries')
            return False
        else:
            os.system('adb shell input tap 395 357')
            Pisces_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                time.sleep(2)
                self.getScreenShot('get Pisces constellation match result')
                return True




if __name__ == '__main__':
    driver = appium_desired()
    l = Constellation(driver)
    l.everyday_costellation_enter()
    # l.same_Sagittarius_match()
    # l.same_Aquarius_match()
    # l.same_Pisces_match()
    # l.everyday_constellation_future()
    # l.everyday_constellation_today()
    # l.everyday_constellation_tomorrow()
    # l.everyday_constellation_more()