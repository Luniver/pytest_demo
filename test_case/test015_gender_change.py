from common.myunit import StartEnd
from businessView.face_function import Face
import pytest
import logging
import allure

class Test_gender_change(StartEnd):

    @allure.feature('test_gender_change_enter')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_gender_change_enter(self):
        logging.info('=====test_gender_change_enter start=====')
        l = Face(self.driver)
        assert l.gender_change_enter() == True

    @allure.feature('test_get_gender_change')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_get_gender_change(self):
        logging.info('=====test_get_gender_change start=====')
        l = Face(self.driver)
        assert l.gender_change_enter() == True
        assert l.get_gender_change() == True


if __name__ == '__main__':
    pytest.main(['-s','test015_gender_change.py'])