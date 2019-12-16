from selenium.webdriver.common.by import By
from common.myunit import StartEnd
from businessView.me_view import MePage
import pytest
import logging
import allure

class Test_information_input(StartEnd):
    me_et_name = (By.ID, 'com.palm.test:id/me_et_name')
    me_name = (By.ID, "com.palm.test:id/me_name")
    me_et_birthday = (By.ID, 'com.palm.test:id/me_et_birthday')
    me_birthday = (By.ID, "com.palm.test:id/me_date")
    done = (By.ID, 'com.palm.test:id/tv_titlebar_text')

    @allure.feature("test_all_information_input")
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_all_information_input(self):
        logging.info("========input all information=======")
        l = MePage(self.driver)
        assert l.switch_navigation_me() == True
        assert l.information_edit_enter() == True
        l.username_edit("lichenyu")
        input_name = (self.driver.find_element(*self.me_et_name)).get_attribute('text')
        l.birthday_select()
        input_birthday = (self.driver.find_element(*self.me_et_birthday)).get_attribute('text')
        l.male_select()
        l.information_done()
        assert input_name == (self.driver.find_element(*self.me_name)).get_attribute('text')
        assert input_birthday == (self.driver.find_element(*self.me_birthday)).get_attribute('text')

    @allure.feature("test_no_name_Done_check")
    @pytest.mark.flaky(reruns=3,reruns_delay=2)
    def test_no_name_Done_check(self):
        logging.info("====input other information but not name====")
        l = MePage(self.driver)
        l.switch_navigation_me()
        l.information_edit_enter()
        l.birthday_select()
        l.male_select()
        assert (self.driver.find_element(*self.done)).is_enabled() == False

    @allure.feature("test_no_birthday_Done_check")
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_no_birthday_Done_check(self):
        logging.info("====input other information but not birthday====")
        l = MePage(self.driver)
        l.switch_navigation_me()
        l.information_edit_enter()
        l.username_edit("lichenyu")
        l.male_select()
        assert (self.driver.find_element(*self.done)).is_enabled() == False

    @allure.feature("test_no_sex_Done_check")
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_no_sex_Done_check(self):
        logging.info("====input other information but not sex====")
        l = MePage(self.driver)
        l.switch_navigation_me()
        l.information_edit_enter()
        l.username_edit("lichenyu")
        l.birthday_select()
        assert (self.driver.find_element(*self.done)).is_enabled() == False

    @allure.feature("test_no_information_Done_check")
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_no_information_Done_check(self):
        logging.info("====input no information====")
        l = MePage(self.driver)
        l.switch_navigation_me()
        l.information_edit_enter()
        assert (self.driver.find_element(*self.done)).is_enabled() == False

if __name__ == '__main__':
    pytest.main('-s', 'test011_MePage_information_input.py')







