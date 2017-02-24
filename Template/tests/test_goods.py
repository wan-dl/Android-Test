#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author:wdl
#@updatetime: 20170221 v1.0.1
import os
import re
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

def handle_page_return(driver,el):
    """
    当从下级页面返回到上级页面时,因元素无法定位或发生异常时,使用系统返回键返回，从而不影响后续case执行。
    """
    try:
        el_id_click(driver,el)
    except Exception as e:
        print(e)
        driver.keyevent(4)

class ProductInformation(unittest.TestCase):
    """
    TestCase: Goods
    Description: 1.元素点击 2.截图 3.点击左上角返回按钮
    """

    #@classmethod,在此类中只进行一次初始化和清理工作 
    @classmethod
    def setUpClass(self):
        self.driver = appium_config.appium_start()
        self.swipe = MobileSwipe()

    def test_initial(self):
        """
        首页:首页初始页面
        """
        if self.driver.current_activity != ".activity.MainActivity":
            self.driver.implicitly_wait(20)
        time.sleep(3)
        for n in range(5):
            self.swipe.swipe_down(self.driver)

    def test_currency_symbo(self):
        """
        商品: 货币符号
        """
        pass
        
    def test_sale_price_verify(self):
        """
        商品: 售价数值判断(大于0为正常数值)
        """
        sale_price = el_text(self.driver,cfg.get("Goods","El_Sale_Price"))
        print(sale_price)
        if sale_price <= 0:
            return False

    def test_like(self):
        """
        商品: 点赞
        """
        text = el_text(self.driver,cfg.get("Goods","El_Like_Count"))
        num = ''.join(re.findall("(-[0-9]+)",text))
        if num < 0 or num is None:
            return False
        el_id_click(self.driver,cfg.get("Goods","El_Like_Count"))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

# texture Testcase
def suite_goods():
    tests = [
        "test_initial",
        "test_currency_symbo",
        "test_sale_price_verify",
        "test_like"
        
    ]
    return unittest.TestSuite(map(ProductInformation,tests))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_goods())
