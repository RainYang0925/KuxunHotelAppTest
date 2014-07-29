'''
Home:

'''
from config import getelements

def get_textViewList(driver):
    testViewList = driver.find_elements_by_xpath(getelements['textView'])
    return testViewList

def get_textView(driver):
    textView = driver.find_element_by_xpath(getelements['textView'])
    return textView

def get_buttonList(driver):
    buttonList = driver.find_elements_by_xpath(getelements['buttonView'])
    return buttonList

def get_searchCityArea(driver):
    searchCityResult = driver.find_element_by_xpath(getelements['editText'])
    return searchCityResult

def buttonClick(city, buttonList):
    for i in range(len(buttonList)):
            if city == buttonList[i].text:
                buttonList[i].click()
                break