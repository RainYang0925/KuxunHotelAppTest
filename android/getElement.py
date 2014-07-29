'''
Home:

'''
from config import getelements

def get_textViewList(driver):
    testViewList = driver.find_elements_by_xpath(getelements['textView'])
    return testViewList

def get_textView(driver):
    textView = driver.find_element_by_xpath(getelements['textView'])

def get_buttonList(driver):
    buttonList = driver.find_elements_by_xpath(getelements['buttonView'])
    return buttonList

def get_search_city_result(driver):
    searchCityResult = driver.find_element_by_xpath(getelements['editText'])
    return searchCityResult