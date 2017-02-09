#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from time import sleep
from configparser import ConfigParser

from appium import webdriver
from selenium.webdriver.common.by import By

from appium_config import appium_start
from common import el_click,el_send_keys,el_xpath_click

#从element.ini文件读取元素
cfg = ConfigParser()
cfg.read('element.ini')

def hongbao(driver):
	try:
		el_xpath_click(driver,cfg.get('Home','TV Hongbao'))
	except Exception as e:
		return False

driver = appium_start()

hongbao(driver)

