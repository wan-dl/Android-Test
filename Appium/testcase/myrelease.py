#!/usr/bin/env python
#-*- coding:utf-8  -*-

# @auther:jiuai
# 2016/07/25
# TestCase:我的发布

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from common import screenshot
from common import el_click,el_send_keys,el_xpath_click
from common import el_text,el_xpath_text
from common import MobileSwipe

# config.ini
cfg = ConfigParser()
cfg.read('config.ini')

# jiuai_data.dat
tdi= ConfigParser()
tdi.read('jiuai_data.dat')

sw = MobileSwipe()

def online_goods(driver):

    el_click(driver,cfg.get('nav','my'))
    el_click(driver,cfg.get('release','option_my_release'))

    el_xpath_click(driver,'//android.widget.HorizontalScrollView[1]')

    goods_title = el_xpath_text(driver,'//android.widget.RelativeLayout[1]/android.widget.TextView[1]')


