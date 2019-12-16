from common.myunit import StartEnd
from businessView.palm_function import Palm
import logging
import allure
import pytest


class Test_Palm_judge(StartEnd):

    @allure.feature('test_palm_judge_enter')
    @pytest.mark.flaky(reruns=3,reruns_delay=2)
    def test_palm_judge_enter(self):
        logging.info("==test_palm_judge_enter start ==")
        l = Palm(self.driver)
        assert l.palm_judgement_enter() ==True

    @allure.feature('test_palm_judge_lifeline')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_palm_judge_lifeline(self):
        logging.info("==test_palm_judge_lifeline start ==")
        l = Palm(self.driver)
        assert l.palm_judge_lifeline() == True

    @allure.feature('test_palm_judge_heartline')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_palm_judge_heartline(self):
        logging.info("==test_palm_judge_heartline start ==")
        l = Palm(self.driver)
        assert l.palm_judge_heartline() == True

    @allure.feature('test_palm_judge_businessline')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_palm_judge_businessline(self):
        logging.info("==test_palm_judge_businessline start ==")
        l = Palm(self.driver)
        assert l.palm_judge_businessline() == True

    @allure.feature('test_palm_judge_headline')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_palm_judge_headline(self):
        logging.info("==test_palm_judge_headline start ==")
        l = Palm(self.driver)
        assert l.palm_judge_headline() == True

    @allure.feature('test_palm_judge_destinyline')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_palm_judge_destinyline(self):
        logging.info("==test_palm_judge_destinyline start ===")
        l = Palm(self.driver)
        assert  l.palm_judge_destinyline() == True

if __name__ == '__main__':
    pytest.main(['-s','-q','--alluredir','./report'])





