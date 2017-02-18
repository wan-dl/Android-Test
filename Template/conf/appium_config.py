#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import re
from appium import webdriver

sys.path.append("..")
from common.mobile import get_serialno

#Read mobile deviceId
device_id = get_serialno()

#Read mobile os Version
os_version = os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_id)).read()
    
def appium_start():
    
    config = {
        'platformName':'Android',
        'platformVersion':os_version,
        'deviceName':device_id,
        # 'appPackage':'com.jiuai',
        # 'appActivity':'.activity.MainActivity',
        'app':'/Users/xiaohutu/GitHub/Android-Test/com.jiuai.apk',
        #'app':'D:\com.jiuai.apk',
        'newCommandTimeout':30,    
        'automationName': 'Appium',
        'unicodeKeyboard':True,
        'resetKeyboard':True}

    return  webdriver.Remote('http://localhost:4723/wd/hub', config)
