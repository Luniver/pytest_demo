from common.myunit import StartEnd
from businessView.psychological_test_function import Psychological
import pytest
import logging
import allure

class Test_Psychological_test(StartEnd):

    @allure.feature('test_question_1_enter')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_question_1_enter(self):
        logging.info('===========test_question_1_enter start===========')
        l = Psychological(self.driver)
        assert l.psychological_question_1() == True

    @allure.feature('test_question_2_enter')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_question_2_enter(self):
        logging.info('===========test_question_2_enter start============')
        l = Psychological(self.driver)
        assert l.psychological_question_2() == True


    @allure.feature('test_question_1_answer_yes')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_question_1_answer_yes(self):
        '''问题1全部回答yes'''
        logging.info('============test_question_1_answer_yes start==========')
        l = Psychological(self.driver)
        assert l.psychological_question_all_yes_1() == True

    @allure.feature('test_question_1_answer_no')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_question_1_answer_no(self):
        '''问题1全部回答no'''
        logging.info('============test_question_1_answer_no start===========')
        l = Psychological(self.driver)
        assert l.psychological_question_all_no_1() == True

    @allure.feature('test_question_1_quit_yes')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_question_1_quit_yes(self):
        '''问题1中途退出点击yes'''
        logging.info('============test_question_1_quit_yes start=============')
        l = Psychological(self.driver)
        assert l.psychological_question_1_quit_yes() == True

    @allure.feature('test_question_1_quit_no')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_question_1_quit_no(self):
        '''问题1中途退出点击no'''
        logging.info('============test_question_1_quit_no start==============')
        l = Psychological(self.driver)
        assert l.psychological_question_1_quit_no() == True

    @allure.feature('test_question_2_answer_yes')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_question_2_answer_yes(self):
        '''问题2全部回答yes'''
        logging.info('============test_question_2_answer_yes start==========')
        l = Psychological(self.driver)
        assert l.psychological_question_all_yes_2() == True

    @allure.feature('test_question_2_answer_no')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_question_2_answer_no(self):
        '''问题2全部回答no'''
        logging.info('============test_question_2_answer_no start===========')
        l = Psychological(self.driver)
        assert l.psychological_question_all_no_2() == True

    @allure.feature('test_question_2_quit_yes')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_question_2_quit_yes(self):
        '''问题2中途退出点击yes'''
        logging.info('============test_question_2_quit_yes start=============')
        l = Psychological(self.driver)
        assert l.psychological_question_2_quit_yes() == True

    @allure.feature('test_question_2_quit_no')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_question_2_quit_no(self):
        '''问题2中途退出点击no'''
        logging.info('============test_question_2_quit_no start==============')
        l = Psychological(self.driver)
        assert l.psychological_question_2_quit_no() == True


if __name__ == '__main__':
    pytest.main(['-s','test009_psychological.py'])