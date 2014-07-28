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
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    #Test the app startup normal
    def test_start_normal(self):
        self.textViewList = getElement.get_textViewList(self.driver)
        self.assertEqual(self.textViewList[0].text, u'酷讯酒店', 'The app title is wrong')

    #Test the selectCity button
    def test_choose_city(self):
        self.buttonList = getElement.get_buttonList(self.driver)
        self.buttonList[4].click()
        time.sleep(2)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelSelectCityActivity', 'The activity name is wrong')

    #Test the hotCity click
    def test_click_hot_city(self):
        self.buttonList = getElement.get_buttonList(self.driver)
        for i in range(len(self.buttonList)):
            if u'上海' in self.buttonList[i].text:
                self.buttonList[i].click
                break
        time.sleep(2)
        self.buttonList = getElement.get_buttonList(self.driver)
        self.assertEqual(self.buttonList[4].text, u'上海', 'The city is not right')


    #Test the hotel city select
    '''
    def test_hot_city_select(self):
        pass
        self.searchCity = getElement.get_search_city_result(self.driver)
        self.searchCity.sendKeys(u'北')
    '''


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HotelMainTest)
    unittest.TextTestRunner(verbosity=2).run(suite)





