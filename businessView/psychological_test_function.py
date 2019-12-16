from common.desired_caps import appium_desired
from businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging,time


class Psychological(HomeView):

    psychological_1 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_psychology"]/android.widget.FrameLayout[1]')
    psychological_2 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_psychology"]/android.widget.FrameLayout[2]')
    psychological_3 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_psychology"]/android.widget.FrameLayout[3]')

    yes = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androi'
                    'd.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]')

    no = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                   '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]')

    back = (By.ID,'com.palm.test:id/iv_titlebar_back')
    toast_yes = (By.ID,'com.palm.test:id/tv_positive')
    toast_no = (By.ID,'com.palm.test:id/tv_negative')

    previous = (By.ID,'com.palm.test:id/layout_psyquiz_previous')

    def psychological_question_1(self):
        '''心理测试问题1的进入'''
        self.switch_psychological_test()
        logging.info('psychological question 1 enter')
        try:
            psychological_1 = self.driver.find_element(*self.psychological_1)
        except NoSuchElementException:
            print('can not find the psychological question 1')
            return False
        else:
            psychological_1.click()
        return True

    def psychological_question_2(self):
        '''心理测试问题2的进入'''
        self.switch_psychological_test()
        logging.info('psychological question 2 enter')
        try:
            psychological_2 = self.driver.find_element(*self.psychological_2)
        except NoSuchElementException:
            print('can not find the psychological question 2')
            return False
        else:
            psychological_2.click()
        return True


    def psychological_question_3(self):
        '''心理测试问题3的进入'''
        self.switch_psychological_test()
        logging.info('psychological question 3 enter')
        try:
            psychological_3 = self.driver.find_element(*self.psychological_3)
        except NoSuchElementException:
            print('can not find the psychological question 3')
            return False
        else:
            psychological_3.click()
        return True
        # self.driver.find_element_by_android_uiautomator(
        #  'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Are you a romanticist?").instance(0));'
        #  ).click()


    def psychological_question_all_yes_1(self):
        '''心理测试题1全部都是yes'''
        self.psychological_question_1()
        logging.info('==========start answer the quanestion 1============')
        for i in range(1,13):
            try:
                yes = self.driver.find_element(*self.yes)
            except NoSuchElementException:
                print('can not find the yes')
                return False
            else:
                yes.click()
                time.sleep(1)
        self.getScreenShot('question 1 all yes')
        return True

    def psychological_question_all_no_1(self):
        '''心理测试题1全部都是no'''
        self.psychological_question_1()
        logging.info('==========start answer the question 1===========')
        for i in range(1,13):
            try:
                no = self.driver.find_element(*self.no)
            except NoSuchElementException:
                print('can not find the no')
                return False
            else:
                no.click()
                time.sleep(1)
        self.getScreenShot('question 1 all no')
        return True

    def psychological_question_1_quit_yes(self):
        '''心理测试题1中途退出点击yes'''
        self.psychological_question_1()
        logging.info('============start answer the question 1=========')
        for i in range(1,5):
            try:
                yes = self.driver.find_element(*self.yes)
            except NoSuchElementException:
                print('can not find the yes')
                return False
            else:
                yes.click()
                time.sleep(1)
        self.driver.find_element(*self.back).click()
        time.sleep(1)
        self.getScreenShot('quit toast')
        try:
            toast_yes = self.driver.find_element(*self.toast_yes)
        except NoSuchElementException:
            print('can not find the toast_yes')
            return False
        else:
            toast_yes.click()
        time.sleep(1)
        logging.info('========check psychological home back=========')
        try:
            self.driver.find_elements(*self.item_image)[4]
        except NoSuchElementException:
            print('can not back to psychological home')
            return False
        else:
            self.getScreenShot('Back to psychological home')
            return True


    def psychological_question_1_quit_no(self):
        '''心理测试题1中途退出点击no'''
        self.psychological_question_1()
        logging.info('============start answer the question 1=========')
        for i in range(1,5):
            try:
                yes = self.driver.find_element(*self.yes)
            except NoSuchElementException:
                print('can not find the yes')
                return False
            else:
                yes.click()
                time.sleep(1)
        self.driver.find_element(*self.back).click()
        time.sleep(1)
        self.getScreenShot('quit toast')
        try:
            toast_no = self.driver.find_element(*self.toast_no)
        except NoSuchElementException:
            print('can not find the toast_no')
            return False
        else:
            toast_no.click()
        time.sleep(1)
        logging.info('========check psychological question page exist=========')
        try:
            self.driver.find_element(*self.yes)
        except NoSuchElementException:
            print('the psychological question page does not exist')
            return False
        else:
            self.getScreenShot('Back to psychological question page')
            return True


    def psychological_question_all_yes_2(self):
        '''心理测试题2全部都是yes'''
        self.psychological_question_2()
        logging.info('==========start answer the quanestion 2============')
        for i in range(1,13):
            try:
                yes = self.driver.find_element(*self.yes)
            except NoSuchElementException:
                print('can not find the yes')
                return False
            else:
                yes.click()
                time.sleep(1)
        self.getScreenShot('question 2 all yes')
        return True

    def psychological_question_all_no_2(self):
        '''心理测试题2全部都是no'''
        self.psychological_question_2()
        logging.info('==========start answer the question 2===========')
        for i in range(1,13):
            try:
                no = self.driver.find_element(*self.no)
            except NoSuchElementException:
                print('can not find the no')
                return False
            else:
                no.click()
                time.sleep(1)
        self.getScreenShot('question 2 all no')
        return True

    def psychological_question_2_quit_yes(self):
        '''心理测试题2中途退出点击yes'''
        self.psychological_question_2()
        logging.info('============start answer the question 2=========')
        for i in range(1,5):
            try:
                yes = self.driver.find_element(*self.yes)
            except NoSuchElementException:
                print('can not find the yes')
                return False
            else:
                yes.click()
                time.sleep(1)
        self.driver.find_element(*self.back).click()
        time.sleep(1)
        self.getScreenShot('quit toast')
        try:
            toast_yes = self.driver.find_element(*self.toast_yes)
        except NoSuchElementException:
            print('can not find the toast_yes')
            return False
        else:
            toast_yes.click()
        time.sleep(1)
        logging.info('========check psychological home back=========')
        try:
            self.driver.find_elements(*self.item_image)[4]
        except NoSuchElementException:
            print('can not back to psychological home')
            return False
        else:
            self.getScreenShot('Back to psychological home')
            return True


    def psychological_question_2_quit_no(self):
        '''心理测试题2中途退出点击no'''
        self.psychological_question_2()
        logging.info('============start answer the question 2=========')
        for i in range(1,5):
            try:
                yes = self.driver.find_element(*self.yes)
            except NoSuchElementException:
                print('can not find the yes')
                return False
            else:
                yes.click()
                time.sleep(1)
        self.driver.find_element(*self.back).click()
        time.sleep(1)
        self.getScreenShot('quit toast')
        try:
            toast_no = self.driver.find_element(*self.toast_no)
        except NoSuchElementException:
            print('can not find the toast_no')
            return False
        else:
            toast_no.click()
        time.sleep(1)
        logging.info('========check psychological question page exist=========')
        try:
            self.driver.find_element(*self.yes)
        except NoSuchElementException:
            print('the psychological question page does not exist')
            return False
        else:
            self.getScreenShot('Back to psychological question page')
            return True


    def psychological_question_all_yes_3(self):
        '''心理测试题3全部都是yes'''
        self.psychological_question_3()
        logging.info('==========start answer the quanestion 3============')
        for i in range(1,13):
            try:
                yes = self.driver.find_element(*self.yes)
            except NoSuchElementException:
                print('can not find the yes')
                return False
            else:
                yes.click()
                time.sleep(1)
        self.getScreenShot('question 3 all yes')
        return True

    def psychological_question_all_no_3(self):
        '''心理测试题3全部都是no'''
        self.psychological_question_3()
        logging.info('==========start answer the question 3===========')
        for i in range(1,13):
            try:
                no = self.driver.find_element(*self.no)
            except NoSuchElementException:
                print('can not find the no')
                return False
            else:
                no.click()
                time.sleep(1)
        self.getScreenShot('question 3 all no')
        return True

    def psychological_question_3_quit_yes(self):
        '''心理测试题3中途退出点击yes'''
        self.psychological_question_3()
        logging.info('============start answer the question 3=========')
        for i in range(1,5):
            try:
                yes = self.driver.find_element(*self.yes)
            except NoSuchElementException:
                print('can not find the yes')
                return False
            else:
                yes.click()
                time.sleep(1)
        self.driver.find_element(*self.back).click()
        time.sleep(1)
        self.getScreenShot('quit toast')
        try:
            toast_yes = self.driver.find_element(*self.toast_yes)
        except NoSuchElementException:
            print('can not find the toast_yes')
            return False
        else:
            toast_yes.click()
        time.sleep(1)
        logging.info('========check psychological home back=========')
        try:
            self.driver.find_elements(*self.item_image)[4]
        except NoSuchElementException:
            print('can not back to psychological home')
            return False
        else:
            self.getScreenShot('Back to psychological home')
            return True


    def psychological_question_3_quit_no(self):
        '''心理测试题3中途退出点击no'''
        self.psychological_question_3()
        logging.info('============start answer the question 1=========')
        for i in range(1,5):
            try:
                yes = self.driver.find_element(*self.yes)
            except NoSuchElementException:
                print('can not find the yes')
                return False
            else:
                yes.click()
                time.sleep(1)
        self.driver.find_element(*self.back).click()
        time.sleep(1)
        self.getScreenShot('quit toast')
        try:
            toast_no = self.driver.find_element(*self.toast_no)
        except NoSuchElementException:
            print('can not find the toast_no')
            return False
        else:
            toast_no.click()
        time.sleep(1)
        logging.info('========check psychological question page exist=========')
        try:
            self.driver.find_element(*self.yes)
        except NoSuchElementException:
            print('the psychological question page does not exist')
            return False
        else:
            self.getScreenShot('Back to psychological question page')
            return True




if __name__ == '__main__':
    driver = appium_desired()
    l = Psychological(driver)
    # l.psychological_question_1()
    # l.psychological_question_all_yes_1()
    # l.psychological_question_all_no_1()
    # l.psychological_question_1_quit_yes()
    # l.psychological_question_1_quit_no()
    # l.psychological_question_2()
    # l.psychological_question_all_yes_2()
    # l.psychological_question_all_no_2()
    # l.psychological_question_2_quit_yes()
    # l.psychological_question_2_quit_no()
    l.psychological_question_3()
    # l.psychological_question_all_yes_3()
    # l.psychological_question_all_no_3()
    # l.psychological_question_3_quit_yes()
    # l.psychological_question_3_quit_no()
