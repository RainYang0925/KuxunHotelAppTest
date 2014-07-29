#encoding: utf-8

import time
import unittest
from appium import webdriver
import getElement

class HotelMainTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platforVersion'] = '4.2'
        desired_caps['deviceName'] = '219ff832'
        desired_caps['appPackage'] = 'com.kuxun.scliang.hotel'
        desired_caps['appActivity'] = 'com.kuxun.hotel.HotelMainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(30)

        self.buttonListMain = getElement.get_buttonList(self.driver)
        self.textViewListMain = getElement.get_textViewList(self.driver)

    def tearDown(self):
        self.driver.quit()

    #Test the app startup normal
    def testcase_1_startNormal(self):
        self.assertEqual(self.textViewListMain[0].text, u'酷讯酒店', 'The app title is wrong')

    #Test the selectCity button
    def testcase_2_chooseCity(self):
        self.buttonListMain[4].click()
        time.sleep(2)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelSelectCityActivity', 'The activity name is wrong')


    #Test the hotCity click
    def testcase_3_clickHotCity(self):
        self.buttonListMain[4].click()
        time.sleep(2)
        self.buttonListCity = getElement.get_buttonList(self.driver)
        for i in range(len(self.buttonListCity)):
            if u'上海' in self.buttonListCity[i].text:
                self.buttonListCity[i].click()
                break
        time.sleep(2)
        self.buttonListMain = getElement.get_buttonList(self.driver)
        for i in range(len(self.buttonListMain)):
            print self.buttonListMain[i].text, i
        print self.buttonListMain[6].text
        self.assertEqual(self.buttonListMain[6].text, u'上海', 'The city is not right')

    #Test the date button
    def testcase_4_selectDate(self):
        self.buttonListMain[5].click()
        time.sleep(2)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelSelectDateActivity', 'The activity is wrong')



if __name__ == '__main__':
    unittest.main()





