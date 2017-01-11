#!/usr/bin/env python
#-*- coding:utf-8  -*-

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser

#config.ini
cfg = ConfigParser()
cfg.read('config.ini')

"""
Func：
    登录: login
    注册: register
    退出: logout
"""

def register(driver,username,identifying_code,password,nickname):
    #open register page
    sleep(3)
    driver.find_element_by_id(cfg.get('nav','my')).click()
    driver.find_element_by_id(cfg.get('my','personal')).click()
    driver.find_element_by_id(cfg.get('login','tvregister')).click()

    #register:the first step 
    driver.find_element_by_id(cfg.get('login','user')).send_keys(username)
    driver.find_element_by_id(cfg.get('register','getcode')).click()
    driver.find_element_by_id(cfg.get('register','inputcode')).send_keys(identifying_code)
    driver.find_element_by_id(cfg.get('login','pwd')).send_keys(password)
    sleep(2)
    driver.keyevent(66)
    driver.find_element_by_id(cfg.get('register','reg_next_btn')).click()
        
    #register:the second setp
    driver.find_element_by_id(cfg.get('register','nickname')).send_keys(nickname)
    driver.find_element_by_id(cfg.get('register','register_btn')).click()
    sleep(3)

    #register succesful page
    #assert ".activity.RegisterRecommendActivity" in driver.current_activity
    #sleep(2)
    driver.get_screenshot_as_file('screenshot/go_home.png')
    #driver.find_element_by_xpath("//android.widget.LinearLayout[@index='5']/ImageView").click()
    driver.find_element_by_id(cfg.get('register','gohome')).click()
    sleep(2)

def login(driver,username,password):
    #open login page
    sleep(3)
    driver.find_element_by_id(cfg.get('nav','my')).click()
    driver.find_element_by_id(cfg.get('my','personal')).click()

    #input mobile and password
    driver.find_element_by_id(cfg.get('login','user')).send_keys(username)
    driver.find_element_by_id(cfg.get('login','pwd')).send_keys(password)
    driver.find_element_by_id(cfg.get('login','loginbtn')).click()

    #Click the mask
    try:
        sleep(2)
        driver.find_element_by_id("com.jiuai:id/linearLayout_mask").click()
    except:
        pass

    #Screenshot: After the successs of the user login
    driver.get_screenshot_as_file('screenshot/login.png')


def logout(driver):
    sleep(2)
    driver.find_element_by_id(cfg.get('my','setting')).click()
    driver.find_element_by_id(cfg.get('setting','logout')).click()

    #wait 2s
    sleep(2)
    driver.find_element_by_id(cfg.get('setting','btn_positive')).click()
