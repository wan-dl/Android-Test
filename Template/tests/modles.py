#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import time
import unittest
from configparser import ConfigParser
from selenium import webdriver
from appium import webdriver

sys.path.append("..")
from conf.appium_config import appium_start
from common.utils import el_click_id,el_click_xpath
from common.utils import screenshot
from common.utils import MobileSwipe

# config.ini
cfg = ConfigParser()
cfg.read('element.ini')

class ThroughPage(unittest.TestCase):

	def __init__(self):
		pass

	def test_test(self):
		pass

if __name__ == "__main__":
    unittest.main()