from businessView.homeview import HomeView
from common.myunit import StartEnd
import pytest
import logging
import allure

class Test_Home_enter(StartEnd):

    # @unittest.skip('test_home_enter')
    # @pytest.fixture()
    # def setup(self):
    #     logging.info('======setUp======')
    #     self.driver = appium_desired()
    @allure.feature('test_home_enter')
    @pytest.mark.flaky(reruns=3,reruns_dely=2)
    def test_home_enter(self):
        logging.info('==test_information_finish==')
        # username = '李宸宇'
        l = HomeView(self.driver)
        # self.assertTrue(l.username_input(username))
        # self.assertTrue(l.birthday_select())
        # # self.assertTrue(l.male_select())
        # self.assertTrue(l.female_select())
        # self.assertTrue(l.next_button())
        # l.allow_event()
        # self.assertTrue(l.back_event())
        assert l.switch_navigation_home() == True

    # def teardown(self):
    #     logging.info('======tearDown=======')
    #     sleep(5)
    #     self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-s','q','test001_homepage_enter.py','--alluredir=report','test001_homepage_enter.py'])