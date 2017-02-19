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
cfg.read("../conf/element.ini")

class ThroughHomePage(unittest.TestCase):
    """
    TestCase: Home Page Through.
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
            self.driver.implicitly_wait(10)
        #self.driver.set_page_load_timeout(30)
        el_id_click(self.driver,cfg.get("Home","El_Home"))
        screenshot(self.driver)
    
    def test_scan(self):
        """
        首页:二维码扫描
        """
        el_id_click(self.driver,cfg.get("Home","El_Qr")) 
        screenshot(self.driver)
        time.sleep(1)
        el_id_click(self.driver,cfg.get("Action","Left"))

    def test_carousel(self):
        """
        首页:轮播
        """
        el_id_click(self.driver,cfg.get("Home","El_Carousel"))
        self.driver.implicitly_wait(10)
        screenshot(self.driver)
        el_id_click(self.driver,cfg.get("Action","Left"))

    def test_ad_left(self):
        """
        首页:广告位-左
        """
        el_id_click(self.driver,cfg.get("Home","El_Ad_Left"))
        screenshot(self.driver)
        el_id_click(self.driver,cfg.get("Action","Left"))

    def test_ad_right(self):
        """
        首页:广告位-右
        """
        el_id_click(self.driver,cfg.get("Home","El_Ad_Right"))
        screenshot(self.driver)
        el_id_click(self.driver,cfg.get("Action","Left"))
 
    def test_recommend_class(self):
        """
        首页:推荐品类
        """
        e1 = cfg.get("Home","El_Category1")
        e2 = cfg.get("Home","El_Category2")
        e3 = cfg.get("Home","El_Category3")
        e4 = cfg.get("Home","El_Category4")
        recommend_class_list = [e1,e2,e3,e4]

        while 1:
            self.swipe.swipe_down_half(self.driver)
            if u"更多品类" in el_text(self.driver,cfg.get("Home","EL_More_Category")):
                screenshot(self.driver)
                break
        for e in recommend_class_list:
            el_id_click(self.driver,e)
            screenshot(self.driver)
            el_id_click(self.driver,cfg.get("Action","Back"))      

    def test_more_category(self):
        """
        首页:更多品类
        """ 
        if u"更多品类" in el_text(self.driver,cfg.get("Home","El_More_Category")):
            screenshot(self.driver)
        else:
            self.swipe.swipe_down_half(self.driver)

        el_id_click(self.driver,cfg.get("Home","El_More_Category"))
        screenshot(self.driver)
        el_id_click(self.driver,cfg.get("Action","Finish"))

    def test_recommend_brand(self):
        """
        首页:推荐品牌
        """
        e1 = cfg.get("Home","El_Brand1")
        e2 = cfg.get("Home","El_Brand2")
        e3 = cfg.get("Home","El_Brand3")
        e4 = cfg.get("Home","El_Brand4")
        recommend_class_list = [e1,e2,e3,e4]

        while 1:
            self.swipe.swipe_down_half(self.driver)
            if u"更多品牌" in el_text(self.driver,cfg.get("Home","EL_More_Brand")):
                screenshot(self.driver)
                break
        for e in recommend_class_list:
            el_id_click(self.driver,e)
            screenshot(self.driver)
            el_id_click(self.driver,cfg.get("Action","Left"))   

    def test_more_brand(self):
        """
        首页:更多品牌
        """
        el_id_click(self.driver,cfg.get("Home","El_More_Category"))
        screenshot(self.driver)
        el_id_click(self.driver,cfg.get("Action","Finish"))
        

    def test_recommend(self):
        """
        首页:推荐
        """
        self.swipe.swipe_down_half(self.driver)
        el_id_click(self.driver,cfg.get("Home","El_TJ"))
        screenshot(self.driver)

    def test_recommend_light(self):
        """
        首页:轻奢
        """
        el_id_click(self.driver,cfg.get("Home","EL_QS"))
        screenshot(self.driver)

    def test_recommend_big(self):
        """
        首页:大牌
        """
        el_id_click(self.driver,cfg.get("Home","EL_DP"))
        screenshot(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

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
