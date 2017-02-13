#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import re
from appium import webdriver

#Read mobile deviceId
readDeviceId = list(os.popen('adb devices -l').readlines())
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]

#Read mobile os Version
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
osVersion = re.findall(r'^\w*\b',deviceAndroidVersion[0])[0]

def appium_start():
    config = {
        'platformName':'Android',
        'platformVersion':osVersion,
        'deviceName':deviceId,
        'appPackage':"com.jiuai",
        'newCommandTimeout':30,    
        'automationName': 'Appium',
        'unicodeKeyboard':True,
        'resetKeyboard':True}

    return  webdriver.Remote('http://localhost:4723/wd/hub', config)
