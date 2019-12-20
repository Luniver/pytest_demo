from common.desired_caps import appium_desired
from businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging,time,os

class Face(HomeView):

    face_function = (By.CLASS_NAME,'android.widget.FrameLayout')
    face_takephoto =(By.ID,'com.palm.test:id/face_picture')
    face_picture = (By.ID,'com.palm.test:id/face_picture_choose')
    gender_face_picture = (By.ID,'com.palm.test:id/ib_album_choose')
    picture = (By.CLASS_NAME,'android.widget.FrameLayout')
    face_ok = (By.ID,'com.palm.test:id/face_ok')
    baby_face_ok = (By.ID,'com.palm.test:id/btn_palmscan_ok')
    gender_face_ok = (By.ID,'com.palm.test:id/ib_ok')
    picture_item = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]')

    PermissionYes = (By.ID,'com.palm.test:id/tv_positive')
    PermissionNo = (By.ID,'com.palm.test:id/tv_negative')
    PrivacyPolicy = (By.ID,'com.palm.test:id/tv_policy')

    mother_photo = (By.ID,'com.palm.test:id/iv_face_baby_camera1')
    father_photo = (By.ID,'com.palm.test:id/iv_face_baby_camera2')

    continue_button = (By.ID,'com.palm.test:id/btn_payment_continue')
    baby_result = (By.ID,'com.palm.test:id/iv_face_center')

    toast = (By.ID, 'com.palm.test:id/tv_message')

    def old_face_enter(self):
        '''变老功能的进入'''
        self.switch_face()
        logging.info('========select and enter old face========')
        try:
            face = self.driver.find_elements(*self.face_function)[1]
        except NoSuchElementException:
            print('can not find the old face button')
            return False
        else:
            face.click()
            # self.getScreenShot('Old_Face_Homepage')
            return True

    def baby_face_enter(self):
        '''宝宝功能的进入'''
        self.switch_face()
        logging.info("======select and enter baby face=======")
        try:
            baby = self.driver.find_elements(*self.face_function)[2]
        except NoSuchElementException:
            print('can not find the baby face button')
            return False
        else:
            baby.click()
            # self.getScreenShot('Baby_Face_Homepage')
            return True

    def gender_change_enter(self):
        '''变性功能进入'''
        self.switch_face()
        logging.info("=====select and enter gender change=====")
        self.swipeDown()
        try:
            gender = self.driver.find_elements(*self.face_function)[2]
        except NoSuchElementException:
            print("can not find the gender change button")
            return False
        else:
            gender.click()

            return True

    def  get_gender_change(self):
        '''变性拍照'''
        # self.gender_change_enter()
        self.allow_once()
        logging.info('=====go to picture====')
        try:
            picture = self.driver.find_element(*self.gender_face_picture)
        except NoSuchElementException:
            print('can not find the gender picture')
            return False
        else:
            picture.click()
        self.allow_once()
        time.sleep(2)
        try:
            picture_item = self.driver.find_element(*self.picture_item)
        except NoSuchElementException:
            print('can not find the picture item')
        else:
            picture_item.click()
        time.sleep(2)
        logging.info('=====choose one picture=====')
        os.system('adb shell input tap 395 357')
        time.sleep(3)

        logging.info('=====picture confirm====')
        try:
            picture_ok = self.driver.find_element(*self.gender_face_ok)
        except NoSuchElementException:
            print('can not find the ok button')
            return False
        else:
            picture_ok.click()

        logging.info('=======Permission Need=========')
        try:
            Yes = self.driver.find_element(*self.PermissionYes)
        except NoSuchElementException:
            print('can not find the PermissionYes')
            return False
        else:
            Yes.click()

        time.sleep(2)

        logging.info('=======wait the old face result=======')
        self.close_event()
        time.sleep(2)
        self.getScreenShot('old face result')
        return True

    def baby_mother_take_photo(self):
        '''宝宝功能妈妈拍照'''
        # self.baby_face_enter()
        try:
            mother_photo = self.driver.find_element(*self.mother_photo)
        except NoSuchElementException:
            print('can not find the mother photo button')
            return False
        else:
            mother_photo.click()
        self.allow_event()
        try:
            picture = self.driver.find_element(*self.face_picture)
        except NoSuchElementException:
            print('can not find the face picture')
            return False
        else:
            picture.click()

        time.sleep(1)
        try:
            picture_item = self.driver.find_element(*self.picture_item)
        except NoSuchElementException:
            print('can not find the picture item')
            return False
        else:
            picture_item.click()
        time.sleep(2)
        logging.info('=====choose one picture====')
        os.system('adb shell input tap 395 357')
        time.sleep(2)

        logging.info('=======picture sure=========')
        try:
            picture_ok = self.driver.find_element(*self.baby_face_ok)
        except NoSuchElementException:
            print('can not find the ok button')
            return False
        else:
            picture_ok.click()

        logging.info('=======Permission Need=========')
        try:
            Yes = self.driver.find_element(*self.PermissionYes)
        except NoSuchElementException:
            print('can not find the PermissionYes')
            return False
        else:
            Yes.click()

        time.sleep(2)

        logging.info('=======wait the baby mather result=======')
        time.sleep(2)

        try:
            self.driver.find_element(*self.continue_button)
        except NoSuchElementException:
            print("picture upload failed")
            return False
        else:
            print('picture mother upload successed')
            self.getScreenShot('mother_photo')
            return True

    def baby_father_take_photo(self):
        '''宝宝功能爸爸拍照'''
        try:
            father_photo = self.driver.find_element(*self.father_photo)
        except NoSuchElementException:
            print('can not find the mother photo button')
            return False
        else:
            father_photo.click()
        self.allow_event()
        try:
            picture = self.driver.find_element(*self.face_picture)
        except NoSuchElementException:
            print('can not find the face picture')
            return False
        else:
            picture.click()

        time.sleep(1)
        try:
            picture_item = self.driver.find_element(*self.picture_item)
        except NoSuchElementException:
            print('can not find the picture item')
            return False
        else:
            picture_item.click()
        time.sleep(2)
        logging.info('=====choose one picture====')
        os.system('adb shell input tap 395 357')
        time.sleep(2)

        logging.info('=======picture sure=========')
        try:
            picture_ok = self.driver.find_element(*self.baby_face_ok)
        except NoSuchElementException:
            print('can not find the ok button')
            return False
        else:
            picture_ok.click()

        logging.info('=======Permission Need=========')
        try:
            Yes = self.driver.find_element(*self.PermissionYes)
        except NoSuchElementException:
            print('can not find the PermissionYes')
            pass
        else:
            Yes.click()

        time.sleep(2)

        logging.info('=======wait the baby father result=======')
        time.sleep(2)

        try:
            self.driver.find_element(*self.continue_button)
        except NoSuchElementException:
            print("picture upload failed")
            return False
        else:
            print('picture father upload successed')
            self.getScreenShot('father_photo')
            return True

    def get_baby_result(self):
        '''宝宝生成'''
        logging.info('=====continue button click=====')
        try:
            continue_button = self.driver.find_element(*self.continue_button)
        except NoSuchElementException:
            print('can not find the continue button')
            return False
        else:
            continue_button.click()

        self.close_event()
        logging.info('=====get result=====')
        try:
            self.driver.find_element(*self.baby_result)
        except NoSuchElementException:
            print('can not find the baby result')
            return False
        else:
            print('get baby resut')
            self.getScreenShot('Baby Result')
            return True

    def baby_check_toast(self):
        '''检测提示toast'''
        logging.info('===check less mother or father toast===')
        try:
            self.driver.find_element(*self.toast)
        except NoSuchElementException:
            print('can not find the toast')
            return False
        else:
            print('get less mother or father toast')
            self.getScreenShot('less mother or father toast')
            return True

    def get_old_face(self):
        '''变老拍照'''
        self.old_face_enter()
        self.allow_once()
        logging.info('========into picture======')
        try:
            picture = self.driver.find_element(*self.face_picture)
        except NoSuchElementException:
            print('can not find the face picture')
            return False
        else:
            picture.click()
        self.allow_once()
        time.sleep(2)
        try:
            picture_item = self.driver.find_element(*self.picture_item)
        except NoSuchElementException:
            print('can not find the picture item')
        else:
            picture_item.click()
        time.sleep(2)
        logging.info('=======choose a picture=======')
        os.system('adb shell input tap 395 357')
        time.sleep(2)

        logging.info('=======picture sure=========')
        try:
            picture_ok = self.driver.find_element(*self.face_ok)
        except NoSuchElementException:
            print('can not find the ok button')
            return False
        else:
            picture_ok.click()

        logging.info('=======Permission Need=========')
        try:
            Yes = self.driver.find_element(*self.PermissionYes)
        except NoSuchElementException:
            print('can not find the PermissionYes')
            return False
        else:
            Yes.click()

        time.sleep(2)


        logging.info('=======wait the old face result=======')
        self.close_event()
        time.sleep(2)
        self.getScreenShot('old face result')
        return True




if __name__ == '__main__':
    driver = appium_desired()
    l = Face(driver)
    # l.old_face_enter()
    # l.get_old_face()
    # l.baby_face_enter()
    l.gender_change_enter()
    l.get_gender_change()
    # l.baby_mother_take_photo()
    # l.baby_father_take_photo()
    # l.get_baby_result()