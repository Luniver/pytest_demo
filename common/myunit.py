from common.desired_caps import appium_desired
import logging
from time import sleep

class StartEnd():
    def setup(self):
        logging.info('==setUp==')
        self.driver = appium_desired()

    def teardown(self):
        logging.info('==tearDown==')
        sleep(5)
        self.driver.quit()