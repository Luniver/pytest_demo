from common.desired_caps import appium_desired
from businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging,time

class Tarot(HomeView):
    tarot_function = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_tarot"]/android.widget.FrameLayout')

    tarot1 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv"]/android.widget.LinearLayout[2]')
    tarot2 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv"]/android.widget.LinearLayout[9]')
    tarot3 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv"]/android.widget.LinearLayout[17]')
    tarot4 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv"]/android.widget.LinearLayout[12]')
    tarot5 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv"]/android.widget.LinearLayout[7]')



    tarot_close = (By.ID,'com.palm.test:id/iv_close')
    share = (By.ID,'com.palm.test:id/iv_titlebar_share')

    quit_yes = (By.ID,'com.palm.test:id/tv_positive')
    quit_no = (By.ID,'com.palm.test:id/tv_negative')

    tarot_page = (By.ID,'com.palm.test:id/rl_tarot')
    tarot_back = (By.ID,'com.palm.test:id/iv_titlebar_back')
    quit_message = (By.ID,'com.palm.test:id/tv_message')

    page_title = (By.ID,'com.palm.test:id/tv_titlebar_title')

    def everyday_tarot_enter(self):
        '''每日塔罗牌功能进入'''
        self.switch_tarot()
        logging.info('=======select and enter everyday tarot========')
        try:
            everyday_tarot = self.driver.find_elements(*self.tarot_function)[0]
        except NoSuchElementException:
            print('can not find the everyday tarot')
            return False
        else:
            everyday_tarot.click()
            self.getScreenShot('TarotEveryday enterPage')
        try:
            self.driver.find_element(*self.page_title)
        except NoSuchElementException:
            print('not in everyday tarot page')
            return False
        else:
            print('now in everyday tarot page')
            return True

    def search_true_love(self):
        '''寻找真爱功能进入'''
        self.switch_tarot()
        logging.info('=====select and enter search true love====')
        try:
            true_love = self.driver.find_elements(*self.tarot_function)[1]
        except NoSuchElementException:
            print('can not find the true love')
            return False
        else:
            true_love.click()
            self.getScreenShot('SearchTrueLove')
        try:
            self.driver.find_element(*self.page_title)
        except NoSuchElementException:
            print('not in true love page')
            return False
        else:
            print('now in true love page')
            return True

    def career(self):
        '''职业功能进入'''
        self.switch_tarot()
        logging.info('====select and enter career====')
        self.swipeDown()
        try:
            career = self.driver.find_elements(*self.tarot_function)[2]
        except NoSuchElementException:
            print('can not find the career')
            return False
        else:
            career.click()
            self.getScreenShot('Career')
        try:
            self.driver.find_element(*self.page_title)
        except NoSuchElementException:
            print('not in career page')
            return False
        else:
            print('now in career page')
            return True

    def get_search_love_five(self):
        '''寻找真爱抽取五张牌'''
        logging.info('======get first tarot=====')
        try:
            first = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first.click()

        logging.info('=====first tarot information')

        self.getScreenShot('First love tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()



        logging.info('=====get second tarot====')
        try:
            second =self.driver.find_element(*self.tarot2)
        except NoSuchElementException:
            print('can not find the second tarot')
            return False
        else:
            second.click()

        logging.info('=====second tarot information=====')
        # time.sleep(2)
        self.getScreenShot('Second love tarot information')
        WebDriverWait(self.driver,20,1).until(
            EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_close'))).click()
        # time.sleep(1)


        logging.info('====get third tarot====')
        try:
            third = self.driver.find_element(*self.tarot3)
        except NoSuchElementException:
            print('can not find the third tarot')
            return False
        else:
            third.click()

        logging.info('=====third tarot information====')
        # time.sleep(2)
        self.getScreenShot('Third love tarot information')
        WebDriverWait(self.driver,20,1).until(
            EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_close'))).click()
        # time.sleep(1)

        logging.info('====get fourth tarot====')
        try:
            fourth = self.driver.find_element(*self.tarot4)
        except NoSuchElementException:
            print('can not find the fourth tarot')
            return False
        else:
            fourth.click()

        logging.info('=====fourth tarot information====')
        # time.sleep(2)
        self.getScreenShot('Fourth love tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        # time.sleep(1)


        logging.info('====get fifth tarot====')
        try:
            fifth = self.driver.find_element(*self.tarot5)
        except NoSuchElementException:
            print('can not find the fifth tarot')
            return False
        else:
            fifth.click()

        logging.info('=====fifth tarot information====')
        # time.sleep(2)
        self.getScreenShot('Fifth love tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        # time.sleep(1)

        self.getScreenShot('All love tarot page')
        return True

    def search_love_quit_show(self):
        '''寻找真爱塔罗牌退出提示'''
        logging.info('======get first tarot=====')
        try:
            first = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first.click()

        logging.info('=====first tarot information')

        self.getScreenShot('First love tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()

        # 点击返回
        try:
            back_btn = self.driver.find_element(*self.tarot_back)
        except NoSuchElementException:
            print('can not find the tarot back button')
            return False
        else:
            back_btn.click()

        try:
            self.driver.find_element(*self.quit_message)
        except NoSuchElementException:
            print('can not find the quit message')
            return False
        else:
            self.getScreenShot('tarot quit message')
            print('sucess focus quit message')
            return True

    def search_love_quit_yes(self):
        logging.info('======get first tarot=====')
        try:
            first = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first.click()

        logging.info('=====first tarot information')

        self.getScreenShot('First love tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()

        # 点击返回
        try:
            back_btn = self.driver.find_element(*self.tarot_back)
        except NoSuchElementException:
            print('can not find the tarot back button')
            return False
        else:
            back_btn.click()
        # 点击是
        try:
            quit_yes = self.driver.find_element(*self.quit_yes)
        except NoSuchElementException:
            print('can not find the quit yes button')
            return False
        else:
            quit_yes.click()
        try:
            self.driver.find_elements(*self.tarot_function)[2]
        except NoSuchElementException:
            print('not back to tarot function home page')
            return False
        else:
            self.getScreenShot('tarot home page')
            print('back to tarot function home page successed')
            return True

    def search_love_quit_no(self):
        logging.info('======get first tarot=====')
        try:
            first = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first.click()

        logging.info('=====first tarot information')

        self.getScreenShot('First love tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()

        # 点击返回
        try:
            back_btn = self.driver.find_element(*self.tarot_back)
        except NoSuchElementException:
            print('can not find the tarot back button')
            return False
        else:
            back_btn.click()

        # 点击否
        try:
            quit_no = self.driver.find_element(*self.quit_no)
        except NoSuchElementException:
            print('can not find the quit no button')
            return False
        else:
            quit_no.click()
        # 检查是否还在牌阵界面
        try:
            self.driver.find_element(*self.tarot_page)
        except NoSuchElementException:
            print('not in true tarot page')
            return False
        else:
            self.getScreenShot('ture tarot')
            print('still in true love tarot page')
            return True



    def get_career_four(self):
        '''职业抽四张牌'''
        logging.info('=====get first tarot=====')
        try:
            first = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first.click()

        logging.info('=====first  tarot information====')
        self.getScreenShot('First carrer tarot information')
        WebDriverWait(self.driver,20,1).until(
            EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_close'))).click()

        logging.info('=====get second tarot=====')
        try:
            second = self.driver.find_element(*self.tarot2)
        except NoSuchElementException:
            print('can not find the second tarot')
            return False
        else:
            second.click()

        logging.info('=====second  tarot information====')
        self.getScreenShot('Second career tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()

        logging.info('=====get third tarot=====')
        try:
            third = self.driver.find_element(*self.tarot3)
        except NoSuchElementException:
            print('can not find the third tarot')
            return False
        else:
            third.click()

        logging.info('=====third  tarot information====')
        self.getScreenShot('Third career tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()

        logging.info('=====get fourth tarot=====')
        try:
            fourth = self.driver.find_element(*self.tarot4)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            fourth.click()

        logging.info('=====fourth tarot information====')
        self.getScreenShot('Fourth career tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()

        self.getScreenShot('All career tarot page')
        return True

    def career_tarot_quit_show(self):
        '''职业塔罗牌退出提示显示'''
        logging.info('=====get first tarot=====')
        try:
            first = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first.click()

        logging.info('=====first  tarot information====')
        time.sleep(2)
        self.getScreenShot('First carrer tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        #点击返回
        try:
            back_btn = self.driver.find_element(*self.tarot_back)
        except NoSuchElementException:
            print('can not find the tarot back button')
            return False
        else:
            back_btn.click()

        try:
            self.driver.find_element(*self.quit_message)
        except NoSuchElementException:
            print('can not find the quit message')
            return False
        else:
            self.getScreenShot('tarot quit message')
            print('sucess focus quit message')
            return True

    def career_tarot_quit_yes(self):
        logging.info('=====get first tarot=====')
        try:
            first = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first.click()

        logging.info('=====first  tarot information====')
        time.sleep(2)
        self.getScreenShot('First carrer tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        # 点击返回
        try:
            back_btn = self.driver.find_element(*self.tarot_back)
        except NoSuchElementException:
            print('can not find the tarot back button')
            return False
        else:
            back_btn.click()
        #点击是
        try:
            quit_yes = self.driver.find_element(*self.quit_yes)
        except NoSuchElementException:
            print('can not find the quit yes button')
            return False
        else:
            quit_yes.click()
        try:
            self.driver.find_elements(*self.tarot_function)[2]
        except NoSuchElementException:
            print('not back to tarot function home page')
            return False
        else:
            self.getScreenShot('tarot home page')
            print('back to tarot function home page successed')
            return True

    def career_tarot_quit_no(self):
        logging.info('=====get first tarot=====')
        try:
            first = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first.click()

        logging.info('=====first  tarot information====')
        time.sleep(2)
        self.getScreenShot('First carrer tarot information')
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        # 点击返回
        try:
            back_btn = self.driver.find_element(*self.tarot_back)
        except NoSuchElementException:
            print('can not find the tarot back button')
            return False
        else:
            back_btn.click()
        #点击否
        try:
            quit_no = self.driver.find_element(*self.quit_no)
        except NoSuchElementException:
            print('can not find the quit no button')
            return False
        else:
            quit_no.click()
        #检查是否还在牌阵界面
        try:
            self.driver.find_element(*self.tarot_page)
        except NoSuchElementException:
            print('not in career tarot page')
            return False
        else:
            self.getScreenShot('career tarot')
            print('still in career tarot page')
            return True



    def get_three_tarot(self):
        '''塔罗牌的抽取'''
        self.everyday_tarot_enter()


        logging.info('=======start get first tarot=======')
        try:
            first_tarot = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first_tarot.click()
        logging.info('============get first tarot information==========')
        time.sleep(3)
        WebDriverWait(self.driver,20,1).until(
            EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_close'))).click()
        time.sleep(2)
        self.getScreenShot('get first tarot page')


        logging.info('=======start get second tarot=========')
        try:
            second_tarot = self.driver.find_element(*self.tarot2)
        except NoSuchElementException:
            print('can not find the second tarot')
            return False
        else:
            second_tarot.click()
        logging.info('==========get second tarot information========')
        time.sleep(3)
        WebDriverWait(self.driver,20,1).until(EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_close'))).click()
        time.sleep(2)
        self.getScreenShot('get second tarot page')


        logging.info('=========start get third tarot==========')
        try:
            third_tarot = self.driver.find_element(*self.tarot3)
        except NoSuchElementException:
            print('can not find the third tarot')
            return False
        else:
            third_tarot.click()
        logging.info('========get third tarot information=========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)
        self.getScreenShot('get all tarot page')
        logging.info('=======get all tarot information')
        return True

    def nothing_tarot_share(self):
        '''没有塔罗牌时点击分享分享'''
        self.everyday_tarot_enter()
        return self.driver.find_element(*self.share).is_enabled()

    def one_tarot_share(self):
        '''有一张塔罗牌时点击分享'''
        self.everyday_tarot_enter()

        logging.info('=======start get first tarot=======')
        try:
            first_tarot = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first_tarot.click()
        logging.info('============get first tarot information==========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        return self.driver.find_element(*self.share).is_enabled()

    def two_tarot_share(self):
        '''有两张塔罗牌时点击分享'''
        self.everyday_tarot_enter()

        logging.info('=======start get first tarot=======')
        try:
            first_tarot = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first_tarot.click()
        logging.info('============get first tarot information==========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        logging.info('=======start get second tarot=========')
        try:
            second_tarot = self.driver.find_element(*self.tarot2)
        except NoSuchElementException:
            print('can not find the second tarot')
            return False
        else:
            second_tarot.click()
        logging.info('==========get second tarot information========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        return self.driver.find_element(*self.share).is_enabled()

    def three_tarot_share(self):
        '''三张塔罗牌时点击分享'''
        self.everyday_tarot_enter()

        logging.info('=======start get first tarot=======')
        try:
            first_tarot = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first_tarot.click()
        logging.info('============get first tarot information==========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        logging.info('=======start get second tarot=========')
        try:
            second_tarot = self.driver.find_element(*self.tarot2)
        except NoSuchElementException:
            print('can not find the second tarot')
            return False
        else:
            second_tarot.click()
        logging.info('==========get second tarot information========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        logging.info('=========start get third tarot==========')
        try:
            third_tarot = self.driver.find_element(*self.tarot3)
        except NoSuchElementException:
            print('can not find the third tarot')
            return False
        else:
            third_tarot.click()
        logging.info('========get third tarot information=========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        try:
            self.driver.find_element(*self.share)
        except NoSuchElementException:
            print('can not find the share button')
            return False
        else:
            return self.driver.find_element(*self.share).is_enabled()



if __name__ == '__main__':
    driver = appium_desired()
    l = Tarot(driver)
    # l.everyday_tarot_enter()
    l.search_true_love()
    # l.get_search_love_five()
    # l.search_love_quit_show()
    # l.search_love_quit_yes()
    l.search_love_quit_no()
    # l.career()
    # l.get_career_four()
    # l.career_tarot_quit_show()
    # l.career_tarot_quit_yes()
    # l.career_tarot_quit_no()
    # l.get_three_tarot()
    # l.nothing_tarot_share()
    # l.one_tarot_share()
    # l.two_tarot_share()
    # l.three_tarot_share()

