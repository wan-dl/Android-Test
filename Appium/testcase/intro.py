#!/usr/bin/env python
#-*- coding:utf-8  -*-

import os,sys
import unittest
from time import sleep
from appium import webdriver
from common import el_click,el_send_keys,el_xpath_click
from common import MobileSwipe

sw = MobileSwipe()

# 引导页
def intro(driver):
    try:
        driver.get_screenshot_as_file("screenshot/intro.png")
        sleep(2)
        for c in range(5):
            sw.left_swipe(driver)

        driver.get_screenshot_as_file("screensot/intro_1.png")
        driver.find_element_by_xpath("//android.widget.ImageView").click()
    except:
        pass
    finally:
        sleep(2)
