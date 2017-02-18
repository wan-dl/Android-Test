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
from common.utils import el_id_click,el_xpath_click,el_text
from common.utils import screenshot
from common.utils import MobileSwipe

# config.ini
cfg = ConfigParser()
cfg.read('../conf/element.ini')

class ThroughHomePage(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver = appium_config.appium_start()
        self.swipe = MobileSwipe()

    def test_initial(self):
        """
        首页:首页初始页面
        """
        if self.driver.current_activity != ".activity.MainActivity":
            self.driver.implicitly_wait(10)
        el_id_click(self.driver,cfg.get('Home',"EL_HOME"))
        screenshot(self.driver)
    
    def test_scan(self):
        """
        首页:二维码扫描
        """
        el_id_click(self.driver,cfg.get('Home',"EL_QR")) 
        screenshot(self.driver)
        time.sleep(1)
        el_id_click(self.driver,cfg.get('Action',"LEFT"))

    def test_carousel(self):
        """
        首页:轮播
        """
        pass

    def test_ad_left(self):
        """
        首页:广告位-左
        """
        el_id_click(self.driver,cfg.get('Home',"EL_AD_LEFT"))
        screenshot(self.driver)
        el_id_click(self.driver,cfg.get('Action',"LEFT"))

    def test_ad_right(self):
        """
        首页:广告位-右
        """
        el_id_click(self.driver,cfg.get('Home',"EL_AD_RIGHT"))
        screenshot(self.driver)
        el_id_click(self.driver,cfg.get('Action',"LEFT"))
 
    def test_recommend_class(self):
        pass

    def test_more_category(self):
        pass

    def test_recommend_brand(self):
        pass

    def test_more_brand(self):
        pass

    def test_recommend(self):
        """
        推荐
        """
        while 1:
            self.swipe.swipe_down(self.driver)
            if u'推荐' in el_text(self.driver,cfg.get('Home',"EL_TJ")):
                screenshot(self.driver)
                break
    def test_recommend_light(self):
        """
        轻奢
        """
        pass

    def test_recommend_big(self):
        """
        大牌
        """
        pass

# texture Testcase
def suite_home():
    tests = [
        "test_initial",
        "test_scan",
        "test_carousel",
        "test_ad_left",
        "test_ad_right",
        "test_recommend_class",
        "test_more_category",
        "test_recommend_brand",
        "test_more_brand",
        "test_recommend",
        "test_recommend_light",
        "test_recommend_big"
    ]
    return unittest.TestSuite(map(ThroughHomePage,tests))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_home())
