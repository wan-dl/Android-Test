#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import time
import unittest
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

sys.path.append("..")
from conf import appium_config
from common.utils import el_id_click,el_xpath_click
from common.utils import screenshot
from common.utils import MobileSwipe

# config.ini
cfg = ConfigParser()
cfg.read('../conf/element.ini')

class ThroughPage(unittest.TestCase):
	
	@classmethod
	def setUpClass(self):
		self.driver = appium_config.appium_start()
		self.swipe = MobileSwipe()

	def test_through_page(self):
		
		if self.driver.current_activity != ".activity.MainActivity":
			self.driver.implicitly_wait(10)
		el_id_click(self.driver,cfg.get('Home',"EL_HOME"))
		screenshot(self.driver,"../logs/home.png")

		for n in range(5):
			self.swipe.swipe_down(self.driver)

if __name__ == "__main__":
    unittest.main()