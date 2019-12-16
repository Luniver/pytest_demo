from common.myunit import StartEnd
from businessView.tarot_function import Tarot
import pytest
import logging
import allure


class Test_TarotEveryday(StartEnd):

    @allure.feature('test_tarot_everyday_enter')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_tarot_everyday_enter(self):
        logging.info('===========test_tarot_everyday_enter start=========')
        l = Tarot(self.driver)
        assert l.everyday_tarot_enter() == True

    @allure.feature('test_get_three_tarot')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_get_three_tarot(self):
        logging.info('==========test_get_three_tarot start=========')
        l = Tarot(self.driver)
        assert l.get_three_tarot() == True

    @allure.feature('test_no_tarot_share')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_no_tarot_share(self):
        logging.info('==========test_no_tarot_share start===========')
        l = Tarot(self.driver)
        assert l.nothing_tarot_share() == False

    @allure.feature('test_one_tarot_share')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_one_tarot_share(self):
        logging.info('==========test_one_tarot_share start=========')
        l = Tarot(self.driver)
        assert l.one_tarot_share() == False

    @allure.feature('test_two_tarot_share')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_two_tarot_share(self):
        logging.info('===========test_two_tarot_share start==========')
        l = Tarot(self.driver)
        assert l.two_tarot_share() == False

    @allure.feature('test_three_tarot_share')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_three_tarot_share(self):
        logging.info('============test_three_tarot_share start===========')
        l = Tarot(self.driver)
        assert l.three_tarot_share() == True

if __name__ == '__main__':
    pytest.main(['-s','test006_tarot_everyday.py'])