#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

import screenshot
from test_config import test_start
from common import MobileSwipe
from testcase.account import login
from testcase.release import release_goods
from testcase.intro import intro

# set config.ini
cfg = ConfigParser()
cfg.read('config.ini')

# set username data
username = '18311446031'
password = 'a123456'

class TestAndroidJiuai(unittest.TestCase):
    """ Test:
        No 1. skip app Guide page
        No 2. user login
        No 3. Release goods
    """
    
    @classmethod
    def setUpClass(self):
        #Appium Android settings
        self.driver = test_start()

        #mobile swipe
        self.sw = MobileSwipe()
    
    # Swipe:app Guide page 
    def test_initialize(self):
        intro(self.driver)
        #self.assertEqual('.activity.MainActivity',self.driver.current_activity)

    # User Register
    def test_login(self):
        login(self.driver,username,password)

    # Release Goods
    def test_release_goods(self):
        release_goods(self.driver)

    # def tearDownClass(self):
    #     self.driver.quit()

# texture testcase
def suite_jiuai():
    tests = [ 
              "test_initialize",
              "test_login",
              "test_release_goods"
            ]
    return unittest.TestSuite(map(TestAndroidJiuai,tests))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_jiuai())
