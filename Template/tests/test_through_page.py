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
from conf import appium_config
from common.utils import el_click_id,el_click_xpath
from common.utils import screenshot
from common.utils import MobileSwipe

# config.ini
cfg = ConfigParser()
cfg.read('element.ini')

class ThroughPage(unittest.TestCase):
	
	@classmethod
	def setUpClass(self):
		self.driver = appium_config.appium_start()

	def test_through_page(self):

		el_click_id(self.driver,cfg.get('Home',"EL_HOME"))
		screenshot(self.driver,"../logs/home.png")

		el_click_xpath(self.driver,cfg.get("Home","EL_EL_MOBILE"))
		screenshot(self.driver,"../logs/mobile.png")

if __name__ == "__main__":
    unittest.main()