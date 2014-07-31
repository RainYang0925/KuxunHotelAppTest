#encoding: utf-8

import devicesOpt

desired_capabilities = {}

def desired_caps():

    if len(list(desired_capabilities)) == 0:
        desired_capabilities['platformName'] = 'Android'
        desired_capabilities['platforVersion'] = '4.2'

        #get device info
        desired_capabilities['deviceName'] = devicesOpt.deviceName()

        #kuxun hotel apk
        desired_capabilities['appPackage'] = 'com.kuxun.scliang.hotel'
        desired_capabilities['appActivity'] = 'com.kuxun.hotel.HotelMainActivity'

    return desired_capabilities

getelements = {
    'textView':'//android.widget.TextView',
    'buttonView':'//android.widget.Button',
    'editText':'//android.widget.EditText',
    'relativeLayout':'//android.widget.RelativeLayout',
    'relaTextView':'//android.widget.RelativeLayout[%s]/android.widget.TextView'
}
