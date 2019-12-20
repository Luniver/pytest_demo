from common.myunit import StartEnd
from businessView.face_function import Face
import pytest
import logging
import allure


class Test_Baby_face(StartEnd):

    @allure.feature('test_baby_face_enter')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_baby_face_enter(self):
        logging.info('======est_baby_face_enter start======')
        l = Face(self.driver)
        assert l.baby_face_enter() == True

    @allure.feature('test_baby_face_mother_photo')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_baby_face_mother_photo(self):
        logging.info('=====test_baby_face_mother_photo start======')
        l = Face(self.driver)
        assert l.baby_face_enter() == True
        assert l.baby_mother_take_photo() == True

    @allure.feature('test_baby_face_father_photo')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_baby_face_father_photo(self):
        logging.info('=====test_baby_face_father_photo start======')
        l =Face(self.driver)
        assert l.baby_face_enter() == True
        assert l.baby_father_take_photo() == True

    @allure.feature('test_baby_face_mother_continue')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_baby_face_mother_continue(self):
        logging.info('=====test_baby_face_mother_continue start======')
        l = Face(self.driver)
        assert l.baby_face_enter() == True
        assert l.baby_mother_take_photo() == True
        assert l.get_baby_result() == False
        assert l.baby_check_toast() == True

    @allure.feature('test_baby_face_father_continue')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_baby_face_father_continue(self):
        logging.info('=====test_baby_face_father_continue start======')
        l = Face(self.driver)
        assert l.baby_face_enter() == True
        assert l.baby_father_take_photo() == True
        assert l.get_baby_result() == False
        assert l.baby_check_toast() == True

    @allure.feature('test_get_baby_result')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_get_baby_result(self):
        logging.info('=====test_get_baby_result start=====')
        l = Face(self.driver)
        assert l.baby_face_enter() == True
        assert l.baby_mother_take_photo() == True
        assert l.baby_father_take_photo() == True
        assert l.get_baby_result() == True

if __name__ == '__main__':
    pytest.main(['-s','test016_baby_face.py'])

