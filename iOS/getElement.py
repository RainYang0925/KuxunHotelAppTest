'''
Home:

'''


def get_textViewList(driver):
    testViewList = driver.find_elements_by_xpath('//android.widget.TextView')
    return testViewList

def get_buttonList(driver):
    buttonList = driver.find_elements_by_xpath('//android.widget.Button')
    return buttonList

def get_search_city_result(driver):
    searchCityResult = driver.find_elements_by_xpath('//android.widget.EditText')
    return searchCityResult