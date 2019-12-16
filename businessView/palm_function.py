from common.desired_caps import appium_desired
from businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging, time


class Palm(HomeView):
    palm_scan = (By.XPATH, '//*[@resource-id="com.palm.test:id/rcv_plam"]/android.widget.FrameLayout[1]')
    palm_judge = (By.XPATH, '//*[@resource-id="com.palm.test:id/rcv_plam"]/android.widget.FrameLayout[2]')
    palmscan_takephoto = (By.ID, 'com.palm.test:id/iv_palmscan_takephoto')
    palmscan_change = (By.ID, 'com.palm.test:id/iv_palmscan_change')
    palmscan_ok = (By.ID, 'com.palm.test:id/btn_palmscan_ok')
    palmscan_cancel = (By.ID, 'com.palm.test:id/btn_palmscan_cancel')
    # palmscan_failure = (By.LINK_TEXT,'無法檢測到手掌，請再試一次')
    palmscan_toast = (By.ID, 'com.palm.test:id/tv_negative')
    palmscan_back = (By.ID, 'com.palm.test:id/iv_palmscan_back')

    palmline_question = (By.XPATH, '//*[@resource-id="com.palm.test:id/rcv"]/android.widget.LinearLayout')
    question_option = (By.ID, 'com.palm.test:id/rb_option')
    result_back = (By.ID, 'com.palm.test:id/iv_titlebar_back')

    def everyday_palm_enter(self):
        '''每日手相功能进入'''
        self.switch_palm()
        logging.info('==========select and enter everydayPalm==========')
        try:
            everydayPalm = self.driver.find_element(*self.palm_scan)
        except NoSuchElementException:
            print('can not find everydayPalm')
            return False
        else:
            everydayPalm.click()
            return True

    def palm_scan_takephoto(self):
        '''手相扫描拍照'''
        self.switch_palm()
        while True:
            logging.info('=========please take a picture===========')
            WebDriverWait(self.driver, 20, 1).until(
                EC.visibility_of_element_located((By.ID, 'com.palm.test:id/btn_palmscan_ok'))).click()
            # try:
            #     takephoto = self.find_element(*self.palmscan_takephoto)
            #     self.get_page_title()
            # except NoSuchElementException:
            #     logging.info('can not find takephoto button')
            #     self.find_element(*self.palmscan_back).click()
            # else:
            #     takephoto.click()
            try:
                ok = self.find_element(*self.palmscan_ok)
            except NoSuchElementException:
                logging.info('can not find ok button')
            else:
                ok.click()
            time.sleep(5)
            logging.info('=========you have take a photo===========')

            try:
                toast = self.driver.find_element(*self.palmscan_toast)
            except NoSuchElementException:
                logging.info('your photo check success')
                break
            else:
                logging.info('your photo check failure,please take a photo again')
                toast.click()
                continue

    def palm_judgement_enter(self):
        '''掌纹判断功能进入'''
        self.switch_palm()
        logging.info('========select palm judgement=======')
        try:
            palmjudge = self.driver.find_element(*self.palm_judge)
        except NoSuchElementException:
            print('can not find the palm judgement')
            return False
        else:
            logging.info('=========enter palm judge function=========')
            palmjudge.click()
            return True

    def palm_judge_lifeline(self):
        '''掌纹判断生命线'''
        self.palm_judgement_enter()
        logging.info('========choose lifeline=======')
        try:
            lifeline = self.driver.find_elements(*self.palmline_question)[0]
        except NoSuchElementException:
            print('can not find the lifeline')
            return False
        else:
            lifeline.click()
        time.sleep(4)
        self.getScreenShot('lifelineQuestion')
        # 选择第一个选项
        logging.info('=======choose first option======')
        try:
            first_option = self.driver.find_elements(*self.question_option)[0]
        except NoSuchElementException:
            print('can not find first option')
            return False
        else:
            first_option.click()
        # #选择第二个选项
        # logging.info('=======choose second option======')
        # try:
        #     second_option = self.driver.find_elements(*self.question_option)[1]
        # except NoSuchElementException:
        #     print('can not find first option')
        # else:
        #     second_option.click()
        self.close_event()
        logging.info('=======get result==========')
        time.sleep(4)
        self.getScreenShot('lifelineResult')
        # 返回按钮点击回到首页
        logging.info('=======back to home========')
        try:
            back = self.driver.find_element(*self.result_back)
        except NoSuchElementException:
            print('can not find the result back')
            return False
        else:
            back.click()
            return True

    def palm_judge_heartline(self):
        '''掌纹判断感情线'''
        self.palm_judgement_enter()
        logging.info('========choose heartline=======')
        try:
            heartline = self.driver.find_elements(*self.palmline_question)[1]
        except NoSuchElementException:
            print('can not find the heartline')
            return False
        else:
            heartline.click()
        time.sleep(4)
        self.getScreenShot('heartlineQuestion')
        # 选择第一个选项
        logging.info('=======choose first option======')
        try:
            first_option = self.driver.find_elements(*self.question_option)[0]
        except NoSuchElementException:
            print('can not find first option')
            return False
        else:
            first_option.click()
        # #选择第二个选项
        # logging.info('=======choose second option======')
        # try:
        #     second_option = self.driver.find_elements(*self.question_option)[1]
        # except NoSuchElementException:
        #     print('can not find first option')
        # else:
        #     second_option.click()
        self.close_event()
        logging.info('=======get result==========')
        time.sleep(4)
        self.getScreenShot('heartlinelineResult')
        # 返回按钮点击回到首页
        logging.info('=======back to home========')
        try:
            back = self.driver.find_element(*self.result_back)
        except NoSuchElementException:
            print('can not find the result back')
            return False
        else:
            back.click()
            return True

    def palm_judge_headline(self):
        '''掌纹判断智慧线'''
        self.palm_judgement_enter()
        logging.info('========choose headline=======')
        try:
            headline = self.driver.find_elements(*self.palmline_question)[2]
        except NoSuchElementException:
            print('can not find the headline')
            return False
        else:
            headline.click()
        time.sleep(4)
        self.getScreenShot('headlineQuestion')
        # 选择第一个选项
        logging.info('=======choose first option======')
        try:
            first_option = self.driver.find_elements(*self.question_option)[0]
        except NoSuchElementException:
            print('can not find first option')
            return False
        else:
            first_option.click()
        # #选择第二个选项
        # logging.info('=======choose second option======')
        # try:
        #     second_option = self.driver.find_elements(*self.question_option)[1]
        # except NoSuchElementException:
        #     print('can not find first option')
        # else:
        #     second_option.click()
        self.close_event()
        logging.info('=======get result==========')
        time.sleep(4)
        self.getScreenShot('headlineResult')
        # 返回按钮点击回到首页
        logging.info('=======back to home========')
        try:
            back = self.driver.find_element(*self.result_back)
        except NoSuchElementException:
            print('can not find the result back')
            return False
        else:
            back.click()
            return True

    def palm_judge_businessline(self):
        '''掌纹判断财富线'''
        self.palm_judgement_enter()
        logging.info('========choose businessline=======')
        try:
            businessline = self.driver.find_elements(*self.palmline_question)[3]
        except NoSuchElementException:
            print('can not find the businessline')
            return False
        else:
            businessline.click()
        time.sleep(4)
        self.getScreenShot('businesslineQuestion')
        # 选择第一个选项
        logging.info('=======choose first option======')
        try:
            first_option = self.driver.find_elements(*self.question_option)[0]
        except NoSuchElementException:
            print('can not find first option')
            return False
        else:
            first_option.click()
        # #选择第二个选项
        # logging.info('=======choose second option======')
        # try:
        #     second_option = self.driver.find_elements(*self.question_option)[1]
        # except NoSuchElementException:
        #     print('can not find first option')
        # else:
        #     second_option.click()
        self.close_event()
        logging.info('=======get result==========')
        time.sleep(4)
        self.getScreenShot('businesslineResult')
        # 返回按钮点击回到首页
        logging.info('=======back to home========')
        try:
            back = self.driver.find_element(*self.result_back)
        except NoSuchElementException:
            print('can not find the result back')
            return False
        else:
            back.click()
            return True

    def palm_judge_destinyline(self):
        '''掌纹判断命运线'''
        self.palm_judgement_enter()
        logging.info('========choose destinyline=======')
        try:
            destinyline = self.driver.find_elements(*self.palmline_question)[4]
        except NoSuchElementException:
            print('can not find the destinyline')
            return False
        else:
            destinyline.click()
        time.sleep(4)
        self.getScreenShot('destinylineQuestion')
        # 选择第一个选项
        logging.info('=======choose first option======')
        try:
            first_option = self.driver.find_elements(*self.question_option)[0]
        except NoSuchElementException:
            print('can not find first option')
            return False
        else:
            first_option.click()
        # #选择第二个选项
        # logging.info('=======choose second option======')
        # try:
        #     second_option = self.driver.find_elements(*self.question_option)[1]
        # except NoSuchElementException:
        #     print('can not find first option')
        # else:
        #     second_option.click()
        self.close_event()
        logging.info('=======get result==========')
        time.sleep(4)
        self.getScreenShot('destinylineResult')
        # 返回按钮点击回到首页
        logging.info('=======back to home========')
        try:
            back = self.driver.find_element(*self.result_back)
        except NoSuchElementException:
            print('can not find the result back')
            return False
        else:
            back.click()
            return True


if __name__ == '__main__':
    driver = appium_desired()
    l = Palm(driver)
    # l.everyday_palm_enter()
    # l.palm_judgement_enter()
    # l.palm_judge_lifeline()
    # l.palm_judge_heartline()
    # l.palm_judge_headline()
    # l.palm_judge_businessline()
    l.palm_judge_destinyline()






