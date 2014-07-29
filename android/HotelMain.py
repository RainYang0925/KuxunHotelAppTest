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
        buttonListCity = getElement.get_buttonList(self.driver)

        getElement.buttonClick(u'上海', buttonListCity)
        time.sleep(2)
        buttonListMain = getElement.get_buttonList(self.driver)

        self.assertEqual(buttonListMain[4].text, u'上海', 'The city is not right')

    #Test the date button
    def testcase_4_selectDate(self):
        self.buttonListMain[5].click()
        time.sleep(2)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelSelectDateActivity', 'The activity is wrong')

    #Test the HotCity suggestion
    #Use spell becase the appium Not supported the chinese characters yet
    def testcase_5_hotCitySuggestion(self):
        self.buttonListMain[4].click()
        time.sleep(2)
        searchArea = getElement.get_searchCityArea(self.driver)
        searchArea.send_keys('bei')
        suggestionCityResutlList = getElement.get_buttonList(self.driver)
        getElement.buttonClick(u'北戴河', suggestionCityResutlList)
        time.sleep(2)
        buttonListMain = getElement.get_buttonList(self.driver)
        self.assertEqual(buttonListMain[4].text, u'北戴河', 'The city is wrong')

    #check keyword button click
    def testcase_5_keywordButtonClick(self):
        self.buttonListMain[6].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelSelectKeywordActivity', 'The activity is wrong')

    def testcase_6_keywordOptionsCheck(self):
        self.buttonListMain[6].click()
        time.sleep(2)
        keywordActButtonList = getElement.get_buttonList(self.driver)
        self.assertEqual(keywordActButtonList[-3].text, u'热门商圈', 'The landmark position is wrong')
        self.assertEqual(keywordActButtonList[-2].text, u'机场车站', 'The station position is wrong')
        self.assertEqual(keywordActButtonList[-1].text, u'快捷品牌', 'The brand position is wrong')
        if len(keywordActButtonList) == 6:
            self.assertEqual(keywordActButtonList[-4].text, u'搜索历史', 'The history position is wrong')

    def testcase_7_chooseLandmarkCheck(self):
        pass

    def testcase_8_landmarkSuggestion(self):
        pass

    def testcase_9_chooseStationCheck(self):
        self.buttonListMain[6].click()
        time.sleep(2)
        keywordActButtonList = getElement.get_buttonList(self.driver)
        keywordActButtonList[-2].click()

        keywordActRelativeLayoutList = getElement.get_RelativeLayoutList(self.driver)
        for i in range(len(keywordActRelativeLayoutList)):
            try:
                if u'北京西站' == getElement.get_RelativeTextView(self.driver, i).text:
                    keywordActRelativeLayoutList[i - 1].click()
            except:
                pass
        time.sleep(1)
        buttonListMainAct = getElement.get_buttonList(self.driver)
        self.assertEqual(buttonListMainAct[6].text, u'北京西站', 'The keyword is wrong')

    def testcase_10_stationSuggestion(self):
        pass

    def testcase_11_chooseBrandCheck(self):
        pass

    def tsetcase_12_brandSuggestion(self):
        pass



if __name__ == '__main__':
    unittest.main()





