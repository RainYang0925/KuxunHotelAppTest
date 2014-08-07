#encoding: utf-8

import time
import unittest
from appium import webdriver
import deviceOperate
import configure

class HomeMainTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platforVersion'] = '4.4'

        #get device info
        desired_caps['deviceName'] = deviceOperate.deviceName()

        #kuxun hotel apk
        desired_caps['appPackage'] = 'com.kuxun.scliang.hotel'
        desired_caps['appActivity'] = 'com.kuxun.hotel.HotelMainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

        self.textViewListHome = self.driver.find_elements_by_xpath('//android.widget.TextView')
        self.buttonListHome = self.driver.find_elements_by_xpath('//android.widget.Button')
    def tearDown(self):
        self.driver.quit()

    #Test the app Title
    def test_01_Title(self):
        self.assertEqual(self.textViewListHome[0].text, u'酷讯酒店')

    #Test the selectCity button
    def test_02_chooseCityACT(self):
        self.buttonListHome[4].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelSelectCityActivity', 'The activity name is wrong')

    #Test the hotCity click
    def test_03_clickHotCity(self):
        self.buttonListHome[4].click()
        time.sleep(1)

        buttonListCity = self.driver.find_elements_by_xpath('//android.widget.Button')
        configure.buttonClick(u'上海', buttonListCity)
        time.sleep(1)

        buttonListMain = self.driver.find_elements_by_xpath('//android.widget.Button')
        self.assertEqual(buttonListMain[4].text, u'上海', 'The city is not right')

    #Test the date button
    def test_04_selectDate(self):
        self.buttonListHome[5].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelSelectDateActivity', 'The activity is wrong')

    #Test the HotCity suggestion
    #Use spell becase the appium Not supported the chinese characters yet
    def test_05_hotCitySuggestion(self):
        self.buttonListHome[4].click()
        time.sleep(1)
        searchArea = self.driver.find_element_by_xpath('//android.widget.EditText')
        searchArea.send_keys('bei')
        suggestionCityResutlList = self.driver.find_elements_by_xpath('//android.widget.Button')
        configure.buttonClick(u'北戴河', suggestionCityResutlList)
        time.sleep(1)
        buttonListMain = self.driver.find_elements_by_xpath('//android.widget.Button')
        self.assertEqual(buttonListMain[4].text, u'北戴河', 'The city is wrong')

    #check keyword button click
    def test_06_keywordButtonClick(self):
        self.buttonListHome[6].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelSelectKeywordActivity', 'The activity is wrong')

    #check keywordAct UI
    def test_07_keywordOptionsCheck(self):
        self.buttonListHome[6].click()
        time.sleep(1)
        keywordActButtonList = self.driver.find_elements_by_xpath('//android.widget.Button')
        self.assertEqual(keywordActButtonList[-3].text, u'热门商圈', 'The landmark position is wrong')
        self.assertEqual(keywordActButtonList[-2].text, u'机场车站', 'The station position is wrong')
        self.assertEqual(keywordActButtonList[-1].text, u'快捷品牌', 'The brand position is wrong')
        if len(keywordActButtonList) == 6:
            self.assertEqual(keywordActButtonList[-4].text, u'搜索历史', 'The history position is wrong')

    #check keywordAct landmark
    def test_08_chooseLandmarkCheck(self):
        self.buttonListHome[6].click()
        time.sleep(1)
        buttonListKeywordAct = self.driver.find_elements_by_xpath('//android.widget.Button')
        buttonListKeywordAct[-3].click()

        relativeLayoutListKeywordAct = self.driver.find_elements_by_xpath('//android.widget.RelativeLayout')
        for i in range(len(relativeLayoutListKeywordAct)):
            try:
                if u'后海商圈' == self.driver.find_element_by_xpath('//android.widget.RelativeLayout[%s]/android.widget.TextView' % i).text:
                    relativeLayoutListKeywordAct[i - 1].click()
            except:
                pass
        time.sleep(1)
        buttonListMain = self.driver.find_elements_by_xpath('//android.widget.Button')
        self.assertEqual(buttonListMain[6].text, u'后海商圈', 'The  landmark keyword is wrong')

    #check keywordAct landmark suggestion
    #Loss of function suggestion
    def test_09_landmarkSuggestion(self):
        self.buttonListHome[6].click()
        time.sleep(1)
        keywordActButtonList = self.driver.find_elements_by_xpath('//android.widget.Button')

        searchArea =self.driver.find_element_by_xpath('//android.widget.EditText')
        searchArea.send_keys('bei')

        pass

    #check keywordAct station
    def test_10_chooseStationCheck(self):
        self.buttonListHome[6].click()
        time.sleep(1)
        buttonListKeywordAct = self.driver.find_elements_by_xpath('//android.widget.Button')
        buttonListKeywordAct[-2].click()

        relativeLayoutListKeywordAct = self.driver.find_elements_by_xpath('//android.widget.RelativeLayout')
        for i in range(len(relativeLayoutListKeywordAct)):
            try:
                if u'北京西站' == self.driver.find_element_by_xpath('//android.widget.RelativeLayout[%s]/android.widget.TextView' % i).text:
                    relativeLayoutListKeywordAct[i - 1].click()
            except:
                pass
        time.sleep(1)
        buttonListMain = self.driver.find_elements_by_xpath('//android.widget.Button')
        self.assertEqual(buttonListMain[6].text, u'北京西站', 'The  landmark keyword is wrong')

    #check keywordAct station suggestion
    #Loss of function suggestion
    def test_11_stationSuggestion(self):
        pass

    #check keywordAct brand
    def test_12_chooseBrandCheck(self):
        self.buttonListHome[6].click()
        time.sleep(1)
        buttonListKeywordAct = self.driver.find_elements_by_xpath('//android.widget.Button')
        buttonListKeywordAct[-1].click()

        relativeLayoutListKeywordAct = self.driver.find_elements_by_xpath('//android.widget.RelativeLayout')
        for i in range(len(relativeLayoutListKeywordAct)):
            try:
                if u'如家快捷' == self.driver.find_element_by_xpath('//android.widget.RelativeLayout[%s]/android.widget.TextView' % i).text:
                    relativeLayoutListKeywordAct[i - 1].click()
            except:
                pass
        time.sleep(1)
        buttonListMain = self.driver.find_elements_by_xpath('//android.widget.Button')
        self.assertEqual(buttonListMain[6].text, u'如家快捷', 'The  landmark keyword is wrong')

    #check keywordAct brand suggestion
    #Loss of function suggestion
    def test_13_brandSuggestion(self):
        pass


    #check price
    def test_14_price(self):
        self.buttonListHome[7].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelPriceSliderActivity', 'The price Actitity is wrong')

    #The UI can not be clicked, will do it in next script
    def test_15_priceChoose(self):
        pass

    #Click gps buton
    def test_16_gpsCitySearchHotel(self):

        cityNameMainAct = self.buttonListHome[4].text
        #print 'cityNameMain,', cityNameHome
        self.buttonListHome[8].click()
        time.sleep(1)
        self.assertEqual(self.driver.current_activity, 'com.kuxun.hotel.HotelListActivity', 'The hotlListAct is wrong')
        time.sleep(2)
        textViewHotelList = self.driver.find_elements_by_xpath('//android.widget.TextView')
        #print textViewHotelList[4].text
        cityNameHotelList = cityNameMainAct if cityNameMainAct in textViewHotelList[4].text else textViewHotelList[4].text
        #print cityNameHotelList
        self.assertEqual(cityNameHotelList, cityNameMainAct, 'The city is not pass by the mainAct')

    #check choose city
    def test_17_chooseCitySerarchHotel(self):
        self.buttonListHome[4].click()
        time.sleep(1)
        buttonListCityAct = self.driver.find_elements_by_xpath('//android.widget.Button')
        configure.buttonClick(u'上海', buttonListCityAct)
        time.sleep(1)
        buttonListMainAct =self.driver.find_elements_by_xpath('//android.widget.Button')
        cityNameMainAct = buttonListMainAct[4].text
        #print cityNameMainAct
        self.buttonListHome[8].click()
        time.sleep(2)
        textViewHotelList = self.driver.find_elements_by_xpath('//android.widget.TextView')
        cityNameHotelList = cityNameMainAct if cityNameMainAct in textViewHotelList[4].text else textViewHotelList[4].text
        #print cityNameHotelList
        self.assertEqual(cityNameHotelList, cityNameMainAct, 'The city is not pass by the mainAct')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HomeMainTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
