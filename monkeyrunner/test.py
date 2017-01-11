#!/usr/bin/env python
#-*- coding:utf-8 -*-

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

device = MonkeyRunner.waitForConnection()

packageName = 'com.jiuai'

#device.removePackage(packageName)

LoginActivity = "com.jiuai.activity.LoginActivity"

runComponent = packageName + '/' + LoginActivity

device.startActivity(component=runComponent)

device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)