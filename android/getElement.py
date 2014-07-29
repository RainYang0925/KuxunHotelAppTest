'''
Home:

'''
from config import getelements

def get_textViewList(driver):
    return driver.find_elements_by_xpath(getelements['textView'])

def get_textView(driver):
    return driver.find_element_by_xpath(getelements['textView'])

def get_buttonList(driver):
    return driver.find_elements_by_xpath(getelements['buttonView'])

def get_searchCityArea(driver):
    return driver.find_element_by_xpath(getelements['editText'])

def get_RelativeLayoutList(driver):
    return driver.find_elements_by_xpath(getelements['relativeLayout'])

def get_RelativeTextView(driver, i):
    return driver.find_element_by_xpath(getelements['relaTextView'] % i)


def buttonClick(city, buttonList):
    for i in range(len(buttonList)):
            if city == buttonList[i].text:
                buttonList[i].click()
                break
