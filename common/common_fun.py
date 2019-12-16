from baseView.baseView import BaseView
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time,os,re


class Commom(BaseView):
    cancelBtn = (By.ID,'com.android.systemui:id/back')
    homeBtn = (By.ID,'com.android.systemui:id/home')
    recentBtn = (By.ID,'com.android.systemui:id/recent_apps')

    allow = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
    deny = (By.ID, 'com.android.packageinstaller:id/permission_deny_button')

    backBtn = (By.ID, 'com.palm.test:id/iv_palmscan_back')
    closeBtn = (By.ID, 'com.palm.test:id/iv_payment_close')

    et_name = (By.ID, 'com.palm.test:id/me_et_name')
    et_birthday = (By.ID, 'com.palm.test:id/me_et_birthday')
    et_male = (By.ID, 'com.palm.test:id/me_tv_male')
    et_female = (By.ID, 'com.palm.test:id/me_tv_female')

    years = (By.ID, 'android:id/date_picker_header_year')
    next_month = (By.ID, 'android:id/next')
    prev_month = (By.ID, 'android:id/prev')
    sure = (By.ID, 'android:id/button1')
    cancel = (By.ID, 'android:id/button2')
    year2018 = (By.XPATH, '//*[@text="2018"]')
    day22 = (By.XPATH, '//*[@text="22"]')

    subscribe_id = (By.ID,'com.palm.test:id/view_payment_btn1')

    def username_edit(self,username):
        '''编辑用户名'''
        logging.info('=========username eidt========')
        try:
            name = self.driver.find_element(*self.et_name)
        except NoSuchElementException:
            print('can not find et_name')
            return False
        else:
            name.clear()
            name.send_keys(username)
            return True

    def birthday_select(self):
        '''选择生日，星座'''
        logging.info('========select birthday=======')
        #点击输入生日
        try:
            birthday_select = self.driver.find_element(*self.et_birthday)
        except NoSuchElementException:
            print('can not find birthday_select input')
            return False
        else:
            birthday_select.click()


        logging.info('========click years to choose=======')
        #点击选择年份
        try:
            years = self.driver.find_element(*self.years)
        except NoSuchElementException:
            print('can not find the years choose')
            return False
        else:
            years.click()

        logging.info('========choose years========')
        #选择年份
        try:
            yearchoose = self.driver.find_element(*self.year2018)
        except NoSuchElementException:
            print('can not find the year2018')
            return False
        else:
            yearchoose.click()

        logging.info('========select month========')
        #选择上一个月
        try:
            prev_month = self.driver.find_element(*self.prev_month)
        except NoSuchElementException:
            print('can not find the prev_month')
            return False
        else:
            prev_month.click()

        logging.info('========select day========')
        #选这日期
        try:
            day = self.driver.find_element(*self.day22)
        except NoSuchElementException:
            print('can not find the day22')
            return False
        else:
            day.click()

        logging.info('=======sure click=========')
        #确认点击
        try:
            sureBtn = self.driver.find_element(*self.sure)
        except NoSuchElementException:
            print('can not find the sureBtn')
            return False
        else:
            sureBtn.click()
            logging.info('========auto select Constellation======')
            return True

    def male_select(self):
        '''男性选择'''
        logging.info('========sexual set male===========')
        try:
            maleBtn = self.driver.find_element(*self.et_male)
        except NoSuchElementException:
            print('no maleBtn to choose')
            return False
        else:
            maleBtn.click()
            return True

    def female_select(self):
        '''女性选择'''
        logging.info('========sexual set female==========')
        try:
            femaleBtn = self.driver.find_element(*self.et_female)
        except NoSuchElementException:
            print('no femaleBtn to choose')
            return False
        else:
            femaleBtn.click()
            return True



    def check_cancel_Btn(self):
        logging.info('===========check cancel_btn===========')
        time.sleep(2)
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancelBtn.click()

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    def allow_event(self):
        '''允许进入'''
        logging.info('========allow to in=============')
        try:
            allowBtn= self.driver.find_element(*self.allow)
        except NoSuchElementException:
            print('can not find the button')
        else:
            allowBtn.click()
        time.sleep(1)
        try:
            allowBtn= self.driver.find_element(*self.allow)
        except NoSuchElementException:
            print('can not find the allow toast')
        else:
            allowBtn.click()

    def allow_once(self):
        '''点击允许'''
        logging.info("========allow to in=======")
        try:
            allowBtn = self.driver.find_element(*self.allow)
        except NoSuchElementException:
            print('can not find the button')
            return False
        else:
            allowBtn.click()
            return True


    def back_event(self):
        '''返回事件'''
        logging.info('========back event============')
        # time.sleep(2)
        # try:
        #     backBtn = self.driver.find_element(*self.backBtn)
        # except NoSuchElementException:
        #     print('can not find the back button')
        #     return False
        # else:
        #     backBtn.click()
        #     return True
        WebDriverWait(self.driver, 10, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_palmscan_back'))).click()

    def close_event(self):
        '''关闭订阅页'''
        logging.info('========close subscribe page======')
        time.sleep(5)
        # try:
        #     self.driver.find_element(*self.subscribe_id)
        # except NoSuchElementException:
        #     print('can not find the subscribe')
        #     return False
        # else:
        #     os.system('adb shell input tap 57 110')
        #     return True
        try:
            self.driver.find_element(*self.closeBtn)
        except NoSuchElementException:
            print('can not find the subscribe page or you are subscribed user')
            pass
        else:
            self.driver.keyevent(4)
            return True
        # WebDriverWait(self.driver, 10, 0.2).until(
        #     EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_payment_close'))).click()

    def first_close_event(self):
        '''启动关闭订阅页'''
        logging.info('============close first subscribe page============')
        time.sleep(10)
        try:
            self.driver.find_element(*self.closeBtn)
        except NoSuchElementException:
            print('can not find the first subscribe page or you are subscribed user')
            pass
        else:
            self.driver.keyevent(4)
            self.driver.keyevent(4)
            return True

    def get_page_title(self):
        '''获取页面事件'''
        self.page = self.driver.page_source
        self.titles = re.findall(r'target="_blank">(.*?)</a></h2>', self.page)
        for title in self.titles:
            print(title)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeDown(self):
        logging.info('swipe Down')
        l = self.get_size()
        x1 = int(l[1] * 0.5)
        y1 = int(l[0] * 0.999)
        y2 = int(l[0] * 0.001)
        self.swipe(x1,y1,x1,y2,1000)

