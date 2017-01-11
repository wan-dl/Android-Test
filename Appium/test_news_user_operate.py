#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser

from appium import webdriver
from selenium.webdriver.common.by import By

import screenshot
from common import MobileSwipe
from test_config import test_start
from testcase.account import login,logout,register
from testcase.editaddress import add_address

# set config.ini
cfg = ConfigParser()
cfg.read('config.ini')

# set username data
username = '18931945511'
password = 'a123456'
nickname = 'test18931945511'
identifying_code = '1234'


class TestAndroidJiuai(unittest.TestCase):
    """ Test:
        No 1. skip app Guide page
        No 2. New user register
        No 3. Home Page refresh
        No 4. Add Address
    """
    
    @classmethod
    def setUpClass(self):
        #Appium Android settings
        self.driver = test_start()

        #mobile swipe
        self.sw = MobileSwipe()
    
    # Swipe:app Guide page 
    def test_initialize(self):
        sleep(3)
        for c in range(5):
            self.sw.left_swipe(self.driver)
        self.driver.find_element_by_xpath("//android.widget.ImageView").click()
        sleep(3)
        self.assertEqual('.activity.MainActivity',self.driver.current_activity)

    # User Register
    def test_register(self):
        register(self.driver,username,identifying_code,password,nickname)

    # Home Page: Refresh
    @unittest.skip("NO Run")
    def test_home_refresh(self):
        self.driver.find_element_by_id(cfg.get('nav','main')).click()
        for c in range(100):
            self.sw.down_swipe(self.driver)

    # Edit Address
    def test_add_address(self):
        add_address(self.driver)

    # def tearDownClass(self):
    #     self.driver.quit()

# texture testcase
def suite_jiuai():
    tests = [ 
              "test_initialize",
              "test_register",
              "test_home_refresh",
              "test_add_address"
            ]
    return unittest.TestSuite(map(TestAndroidJiuai,tests))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_jiuai())
