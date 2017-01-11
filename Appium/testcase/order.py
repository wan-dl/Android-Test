#!/usr/bin/env python
#-*- coding:utf-8  -*-

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser

from common import el_click,el_send_keys
from common import MobileSwipe

#config.ini
cfg = ConfigParser()
cfg.read('config.ini')

"""
    TestCase:
    1. 选择商品
"""
sw = MobileSwipe()

def select_goods(driver):
    el_click(driver,cfg.get('nav','main'))
    for c in range(10):
        sw.down_swipe(driver)

    driver.find_element_by_xpath("//android.widget.RelativeLayout[2]").click()

def to_buy(driver):
    el_click(driver,cfg.get('goods_details','tobuy'))
    