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
        searchArea = getElement.get_searchArea(self.driver)
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

    #check keywordAct UI
    def testcase_6_keywordOptionsCheck(self):
        self.buttonListMain[6].click()
        time.sleep(2)
        keywordActButtonList = getElement.get_buttonList(self.driver)
        self.assertEqual(keywordActButtonList[-3].text, u'热门商圈', 'The landmark position is wrong')
        self.assertEqual(keywordActButtonList[-2].text, u'机场车站', 'The station position is wrong')
        self.assertEqual(keywordActButtonList[-1].text, u'快捷品牌', 'The brand position is wrong')
        if len(keywordActButtonList) == 6:
            self.assertEqual(keywordActButtonList[-4].text, u'搜索历史', 'The history position is wrong')

    #check keywordAct landmark
    def testcase_7_chooseLandmarkCheck(self):
        self.buttonListMain[6].click()
        time.sleep(2)
        keywordActButtonList = getElement.get_buttonList(self.driver)
        keywordActButtonList[-3].click()

        keywordActRelativeLayoutList = getElement.get_RelativeLayoutList(self.driver)
        for i in range(len(keywordActRelativeLayoutList)):
            try:
                if u'后海商圈' == getElement.get_RelativeTextView(self.driver, i).text:
                    keywordActRelativeLayoutList[i - 1].click()
            except:
                pass
        time.sleep(1)
        buttonListMainAct = getElement.get_buttonList(self.driver)
        self.assertEqual(buttonListMainAct[6].text, u'后海商圈', 'The  landmark keyword is wrong')

    #check keywordAct landmark suggestion
    #Loss of function suggestion
    def testcase_8_landmarkSuggestion(self):
        self.buttonListMain[6].click()
        time.sleep(1)
        keywordActButtonList = getElement.get_buttonList(self.driver)

        searchArea = getElement.get_searchArea(self.driver)
        searchArea.send_keys('bei')

        pass

    #check keywordAct station
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
        self.assertEqual(buttonListMainAct[6].text, u'北京西站', 'The station keyword is wrong')

    #check keywordAct station suggestion
    #Loss of function suggestion
    def testcase_10_stationSuggestion(self):
        pass

    #check keywordAct brand
    def testcase_11_chooseBrandCheck(self):
        self.buttonListMain[6].click()
        time.sleep(2)
        keywordActButtonList = getElement.get_buttonList(self.driver)
        keywordActButtonList[-1].click()

        keywordActRelativeLayoutList = getElement.get_RelativeLayoutList(self.driver)
        for i in range(len(keywordActRelativeLayoutList)):
            try:
                if u'如家快捷' == getElement.get_RelativeTextView(self.driver, i).text:
                    keywordActRelativeLayoutList[i - 1].click()
            except:
                pass
        time.sleep(1)
        buttonListMainAct = getElement.get_buttonList(self.driver)
        self.assertEqual(buttonListMainAct[6].text, u'如家快捷', 'The  landmark keyword is wrong')

    #check keywordAct brand suggestion
    #Loss of function suggestion
    def testcase_12_brandSuggestion(self):
        pass

    #check price
    def testcase_13_price(self):
        self.buttonListMain[7].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelPriceSliderActivity', 'The price Actitity is wrong')

    #The UI can not be clicked, will do it in next script
    def testcase_14_priceChoose(self):
        pass

if __name__ == '__main__':
    unittest.main()





