# @ Author Krishna chetan, 04-01-2019
# -*- coding: utf-8 -*-
import unittest, time
import os
os.system("appium -a 127.0.0.1 -p 4723")
time.sleep(10)
from appium import webdriver
#imports

class Android_Tinder_Swipe(unittest.TestCase):
#Class to run tests against the Tinder app

    def setUp(self):
    #Setup for the test
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8'
        desired_caps['deviceName'] = 'krishna'
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'com.tinder'
        desired_caps['appActivity'] = 'com.tinder.activities.MainActivity'
        desired_caps['noReset'] = True
        # To prevent app from resetting every time you launch tests
        desired_caps['appWaitActivity'] = 'com.tinder.activities.MainActivity'
        # Adding appWait Activity since the activity name changes as the focus shifts to the Tinder app's first page
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
    #Tear down the test
        self.driver.quit()

    def test_tinder_rightswipe(self):
        self.driver.implicitly_wait(30)
        #Waiting for screen to load
        try:
            for x in range(0, 9999):
                self.driver.find_element_by_id("com.tinder:id/gamepad_like").click()
                #Click on like button
        except Exception, e:
            print ('Failed to swipe due to following error : ' + str(e))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_Tinder_Swipe)
    unittest.TextTestRunner(verbosity=2).run(suite)