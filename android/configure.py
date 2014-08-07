#encoding: utf-8

def buttonClick(city, buttonList):
    for i in range(len(buttonList)):
            if city == buttonList[i].text:
                buttonList[i].click()
                break