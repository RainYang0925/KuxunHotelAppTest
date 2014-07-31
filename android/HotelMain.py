#encoding: utf-8

import time
import unittest
from appium import webdriver
import getElement


class HotelMainTestCase(unittest.TestCase):

    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platforVersion'] = '4.2'

        #xiaomi 3
        desired_caps['deviceName'] = '219ff832'

        #xiaomi 2s
        #desired_caps['deviceName'] = '4b8f91d6'

        #kuxun hotel apk
        desired_caps['appPackage'] = 'com.kuxun.scliang.hotel'
        desired_caps['appActivity'] = 'com.kuxun.hotel.HotelMainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

        self.buttonListMain = getElement.get_buttonList(self.driver)
        self.textViewListMain = getElement.get_textViewList(self.driver)

    def tearDown(self):
        self.driver.quit()

    #Test the app startup normal
    def test_01_startNormal(self):
        self.assertEqual(self.textViewListMain[0].text, u'酷讯酒店', 'The app title is wrong')


    #Test the selectCity button
    def test_02_chooseCity(self):
        self.buttonListMain[4].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelSelectCityActivity', 'The activity name is wrong')


    #Test the hotCity click
    def test_03_clickHotCity(self):
        self.buttonListMain[4].click()
        time.sleep(1)
        buttonListCity = getElement.get_buttonList(self.driver)

        getElement.buttonClick(u'上海', buttonListCity)
        time.sleep(1)
        buttonListMain = getElement.get_buttonList(self.driver)

        self.assertEqual(buttonListMain[4].text, u'上海', 'The city is not right')

    #Test the date button
    def test_04_selectDate(self):
        self.buttonListMain[5].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelSelectDateActivity', 'The activity is wrong')


    #Test the HotCity suggestion
    #Use spell becase the appium Not supported the chinese characters yet
    def test_05_hotCitySuggestion(self):
        self.buttonListMain[4].click()
        time.sleep(1)
        searchArea = getElement.get_searchArea(self.driver)
        searchArea.send_keys('bei')
        suggestionCityResutlList = getElement.get_buttonList(self.driver)
        getElement.buttonClick(u'北戴河', suggestionCityResutlList)
        time.sleep(1)
        buttonListMain = getElement.get_buttonList(self.driver)
        self.assertEqual(buttonListMain[4].text, u'北戴河', 'The city is wrong')

    #check keyword button click
    def test_06_keywordButtonClick(self):
        self.buttonListMain[6].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelSelectKeywordActivity', 'The activity is wrong')

    #check keywordAct UI
    def test_07_keywordOptionsCheck(self):
        self.buttonListMain[6].click()
        time.sleep(1)
        keywordActButtonList = getElement.get_buttonList(self.driver)
        self.assertEqual(keywordActButtonList[-3].text, u'热门商圈', 'The landmark position is wrong')
        self.assertEqual(keywordActButtonList[-2].text, u'机场车站', 'The station position is wrong')
        self.assertEqual(keywordActButtonList[-1].text, u'快捷品牌', 'The brand position is wrong')
        if len(keywordActButtonList) == 6:
            self.assertEqual(keywordActButtonList[-4].text, u'搜索历史', 'The history position is wrong')

    #check keywordAct landmark
    def test_08_chooseLandmarkCheck(self):
        self.buttonListMain[6].click()
        time.sleep(1)
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
    def test_09_landmarkSuggestion(self):
        self.buttonListMain[6].click()
        time.sleep(1)
        keywordActButtonList = getElement.get_buttonList(self.driver)

        searchArea = getElement.get_searchArea(self.driver)
        searchArea.send_keys('bei')

        pass

    #check keywordAct station
    def test_10_chooseStationCheck(self):
        self.buttonListMain[6].click()
        time.sleep(1)
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
    def test_11_stationSuggestion(self):
        pass

    #check keywordAct brand
    def test_12_chooseBrandCheck(self):
        self.buttonListMain[6].click()
        time.sleep(1)
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
    def test_13_brandSuggestion(self):
        pass

    #check price
    def test_14_price(self):
        self.buttonListMain[7].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelPriceSliderActivity', 'The price Actitity is wrong')

    #The UI can not be clicked, will do it in next script
    def test_15_priceChoose(self):
        pass

    #Click gps buton
    def test_16_gpsCitySearchHotel(self):

        cityNameMain = self.buttonListMain[4].text
        print 'cityNameMain,', cityNameMain
        self.buttonListMain[8].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelListActivity', 'The hotlListAct is wrong')
        time.sleep(2)
        textViewHotelList = getElement.get_textViewList(self.driver)
        print textViewHotelList[4].text
        cityNameHotelList = cityNameMain if cityNameMain in textViewHotelList[4].text else textViewHotelList[4].text
        print cityNameHotelList
        self.assertEqual(cityNameHotelList, cityNameMain, 'The city is not pass by the mainAct')

    #check choose city
    def test_17_chooseCitySerarchHotel(self):
        self.buttonListMain[4].click()
        time.sleep(1)
        buttonListCityAct = getElement.get_buttonList(self.driver)
        getElement.buttonClick(u'上海', buttonListCityAct)
        time.sleep(1)
        buttonListMainAct = getElement.get_buttonList(self.driver)
        cityNameMainAct = buttonListMainAct[4].text
        print cityNameMainAct
        self.buttonListMain[8].click()
        time.sleep(2)
        textViewList = getElement.get_textViewList(self.driver)
        cityNameHotelList = cityNameMainAct if cityNameMainAct in textViewList[4].text else textViewList[4].text
        print cityNameHotelList
        self.assertEqual(cityNameHotelList, cityNameMainAct, 'The city is not pass by the mainAct')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HotelMainTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)





