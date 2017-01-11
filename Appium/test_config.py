#!/usr/bin/env python

from appium import webdriver

def test_start():
    config = {
        'platformName': 'Android',
        'platformVersion': '6.0',
        'deviceName': '1115fb3599a03104',
        'app': "/Users/xiaohutu/Documents/com.jiuai.apk",
        'newCommandTimeout': 30,    
        'automationName': 'Appium',
        'unicodeKeyboard':True,
        'resetKeyboard':True}

    return  webdriver.Remote('http://localhost:4723/wd/hub', config)
