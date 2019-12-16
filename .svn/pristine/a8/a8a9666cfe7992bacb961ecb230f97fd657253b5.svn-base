from common.myunit import StartEnd
from businessView.Constellation_function import Constellation
import logging
import pytest
import allure
import os


class Test_Constellation_match(StartEnd):

    @allure.feature('test_constellation_Match_enter')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_constellation_Match_enter(self):
        logging.info('==========test constellation_Match_enter start===========')
        l = Constellation(self.driver)
        assert l.constellation_Match_enter() == True

    @allure.feature('test_same_Aries_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Aries_match(self):
        logging.info('=========test_same_Aries_match start==========')
        l =Constellation(self.driver)
        assert l.same_Aries_match() == True
    @allure.feature('test_same_Taurus_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Taurus_match(self):
        logging.info('=========test_same_Taurus_match start==========')
        l =Constellation(self.driver)
        assert l.same_Taurus_match() == True

    @allure.feature('test_same_Gemini_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Gemini_match(self):
        logging.info('=========test_same_Gemini_match start==========')
        l =Constellation(self.driver)
        assert l.same_Gemini_match() == True

    @allure.feature('test_same_Cancer_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Cancer_match(self):
        logging.info('=========test_same_Cancer_match start==========')
        l =Constellation(self.driver)
        assert l.same_Cancer_match() == True

    @allure.feature('test_same_Leo_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Leo_match(self):
        logging.info('=========test_same_Leo_match start==========')
        l =Constellation(self.driver)
        assert l.same_Leo_match() == True

    @allure.feature('test_same_Virgo_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Virgo_match(self):
        logging.info('=========test_same_Virgo_match start==========')
        l =Constellation(self.driver)
        assert l.same_Virgo_match() == True

    @allure.feature('test_same_Libra_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Libra_match(self):
        logging.info('=========test_same_Libra_match start==========')
        l =Constellation(self.driver)
        assert l.same_Libra_match() == True

    @allure.feature('test_same_Scorpio_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Scorpio_match(self):
        logging.info('=========test_same_Scorpio_match start==========')
        l =Constellation(self.driver)
        assert l.same_Scorpio_match() == True

    @allure.feature('test_same_Sagittarius_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Sagittarius_match(self):
        logging.info('=========test_same_Sagittarius_match start==========')
        l =Constellation(self.driver)
        assert l.same_Sagittarius_match() == True

    @allure.feature('test_same_Capricornus_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Capricornus_match(self):
        logging.info('=========test_same_Capricornus_match start==========')
        l =Constellation(self.driver)
        assert l.same_Capricornus_match() == True

    @allure.feature('test_same_Aquarius_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Aquarius_match(self):
        logging.info('=========test_same_Aquarius_match start==========')
        l =Constellation(self.driver)
        assert l.same_Aquarius_match() == True

    @allure.feature('test_same_Pisces_match')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_same_Pisces_match(self):
        logging.info('=========test_same_Pisces_match start==========')
        l =Constellation(self.driver)
        assert l.same_Pisces_match() == True


if __name__ == '__main__':
    pytest.main(['-s','-q','--alluredir','./report/xml'])
    os.system('allure generate report/ -o allure-reports/')