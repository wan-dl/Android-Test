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

#读取config.ini
cfg = ConfigParser()
cfg.read("../conf/element.ini")

def handle_page_return(driver,el):
    """
    当从下级页面返回到上级页面时,因元素无法定位或发生异常时,
    使用系统返回键返回，从而不影响后续case执行。
    """
    try:
        el_id_click(driver,el)
    except Exception as e:
        print(e)
        driver.keyevent(4)

class ProductInformation(unittest.TestCase):
    """
    TestCase: 
    Description: 
    """

    #@classmethod,在此类中只进行一次初始化和清理工作 
    @classmethod
    def setUpClass(self):
        self.driver = appium_config.appium_start()

    def test_initial(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

# texture Testcase
def suite_goods():
    tests = [
        "test_initial",        
    ]
    return unittest.TestSuite(map(ProductInformation,tests))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_goods())
