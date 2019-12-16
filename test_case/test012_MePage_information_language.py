from selenium.webdriver.common.by import By
from common.myunit import StartEnd
from businessView.me_view import MePage
import pytest
import logging
import allure

class Test_information_language(StartEnd):
    me_et_name = (By.ID, 'com.palm.test:id/me_et_name')
    me_name = (By.ID, "com.palm.test:id/me_name")

    @allure.feature("test_input_english")
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_input_english(self):
        logging.info("======input name in english======")
        l = MePage(self.driver)
        l.switch_navigation_me()
        l.information_edit_enter()
        l.username_edit("lichenyu")
        logging.info("=====input lichenyu=====")
        input_name = (self.driver.find_element(*self.me_et_name)).get_attribute('text')
        l.birthday_select()
        l.male_select()
        l.information_done()
        assert input_name == (self.driver.find_element(*self.me_name)).get_attribute('text')

    @allure.feature("test_input_chinese")
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_input_chinese(self):
        logging.info("======input name in chinese======")
        l = MePage(self.driver)
        l.switch_navigation_me()
        l.information_edit_enter()
        l.username_edit("李宸宇")
        logging.info("=====input 李宸宇=====")
        input_name = (self.driver.find_element(*self.me_et_name)).get_attribute('text')
        l.birthday_select()
        l.male_select()
        l.information_done()
        assert input_name == (self.driver.find_element(*self.me_name)).get_attribute('text')

    @allure.feature("test_input_japanese")
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_input_japanese(self):
        logging.info("======input name in japanese======")
        l = MePage(self.driver)
        l.switch_navigation_me()
        l.information_edit_enter()
        l.username_edit("本当ですか")
        logging.info("=====input 本当ですか=====")
        input_name = (self.driver.find_element(*self.me_et_name)).get_attribute('text')
        l.birthday_select()
        l.male_select()
        l.information_done()
        assert input_name == (self.driver.find_element(*self.me_name)).get_attribute('text')

    @allure.feature("test_input_korean")
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_input_korean(self):
        logging.info("======input name in korean======")
        l = MePage(self.driver)
        l.switch_navigation_me()
        l.information_edit_enter()
        l.username_edit("진짜예요?")
        logging.info("=====input 진짜예요?=====")
        input_name = (self.driver.find_element(*self.me_et_name)).get_attribute('text')
        l.birthday_select()
        l.male_select()
        l.information_done()
        assert input_name == (self.driver.find_element(*self.me_name)).get_attribute('text')

    @allure.feature("test_input_Portuguese")
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_input_Portuguese(self):
        logging.info("======input name in Portuguese======")
        l = MePage(self.driver)
        l.switch_navigation_me()
        l.information_edit_enter()
        l.username_edit("Constelação")
        logging.info("=====input Constelação=====")
        input_name = (self.driver.find_element(*self.me_et_name)).get_attribute('text')
        l.birthday_select()
        l.male_select()
        l.information_done()
        assert input_name == (self.driver.find_element(*self.me_name)).get_attribute('text')

if __name__ == '__main__':
    pytest.main('-s', 'test012_MePage_information_language.py')