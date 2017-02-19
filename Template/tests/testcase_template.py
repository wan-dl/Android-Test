#!/usr/bin/env python
#-*- coding:utf-8 -*-

# @author wdl
# @time update 2017-02-29 V1.0.1

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
from common.utils import el_id_click,el_xpath_click,el_text
from common.utils import screenshot
from common.utils import MobileSwipe

# config.ini
cfg = ConfigParser()
cfg.read("../conf/element.ini")

class ThroughHomePage(unittest.TestCase):
   
    #@classmethod,在此类中只进行一次初始化和清理工作 
    @classmethod
    def setUpClass(self):
        self.driver = appium_config.appium_start()
        self.swipe = MobileSwipe()

    def test_initial(self):
        """
        首页:首页初始页面
        """
        el_id_click(self.driver,cfg.get("Home","El_Home"))
        screenshot(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

# texture Testcase
def suite():
    tests = [
        "test_initial",
    ]
    return unittest.TestSuite(map(ThroughHomePage,tests))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
