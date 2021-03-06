from common.myunit import StartEnd
from businessView.tarot_function import Tarot
import pytest
import logging
import allure


class Test_search_love_tarot(StartEnd):

    @allure.feature('test_search_love_tarot_enter')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_search_love_tarot_enter(self):
        logging.info('======test_search_love_tarot_enter start=====')
        l = Tarot(self.driver)
        assert l.search_true_love() == True

    @allure.feature('test_search_love_get_five')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_search_love_get_five(self):
        logging.info('=====test_search_love_get_five start=====')
        l = Tarot(self.driver)
        assert l.search_true_love() == True
        assert l.get_search_love_five() == True

    @allure.feature('test_search_love_quit_show')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_search_love_quit_show(self):
        logging.info('=====test_search_love_quit_show start=====')
        l = Tarot(self.driver)
        assert l.search_true_love() == True
        assert l.search_love_quit_show() == True

    @allure.feature('test_search_love_quit_yes')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_search_love_quit_yes(self):
        logging.info('=====test_search_love_quit_yes start======')
        l = Tarot(self.driver)
        assert l.search_true_love() == True
        assert l.search_love_quit_yes() == True

    @allure.feature('test_search_love_quit_no')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_search_love_quit_no(self):
        logging.info('=====test_search_love_quit_no start======')
        l = Tarot(self.driver)
        assert l.search_true_love() == True
        assert l.search_love_quit_no() == True

if __name__ == '__main__':
    pytest.main(['-s','test014_search_love_tarot.py'])

