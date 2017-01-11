#!/usr/bin/env python
#-*- coding:utf-8  -*-

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser

from common import screenshot
from common import el_click,el_text

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
    el_click(driver,cfg.get('nav','my'))
    el_click(driver,cfg.get('my','personal'))
    el_click(driver,cfg.get('login','tvregister'))

    #register:the first step 
    el_click(driver,cfg.get('login','user')).send_keys(username)
    el_click(driver,cfg.get('register','getcode'))
    el_click(driver,cfg.get('register','inputcode')).send_keys(identifying_code)
    el_click(driver,cfg.get('login','pwd')).send_keys(password)
    sleep(2)
    driver.keyevent(66)
    el_click(driver,cfg.get('register','reg_next_btn'))
        
    #register:the second setp
    el_click(driver,cfg.get('register','nickname')).send_keys(nickname)
    el_click(driver,cfg.get('register','register_btn'))
    sleep(3)

    #register succesful page
    #assert ".activity.RegisterRecommendActivity" in driver.current_activity
    #sleep(2)
    driver.get_screenshot_as_file('screenshot/go_home.png')
    #driver.find_element_by_xpath("//android.widget.LinearLayout[@index='5']/ImageView")
    el_click(driver,cfg.get('register','gohome'))
    sleep(2)

def login_input_verify(driver,username,passwd):
    el_click(driver,cfg.get('login','user')).send_keys(username)
    el_click(driver,cfg.get('login','pwd')).send_keys(passwd)

def login(driver,username,valid_pwd,invalid_pwd):
    #open login page
    sleep(1)
    el_click(driver,cfg.get('nav','my'))
    screenshot(driver,'screenshot/Login_init_page.png')

    login_btn_content = el_text(driver,cfg.get('my','login_btn')
    try:
        not_login_content = u'注册/登录'
        if not_login_content in login_btn_content:
            el_click(driver,cfg.get('my','login_btn'))
            screenshot(driver,'screenshot/Login_input_page.png')

            #input mobile and password
            try:
                login_input_verify(driver,username,invalid_pwd)
                el_click(driver,cfg.get('login','loginbtn'))
                screenshot(driver,'screenshot/Login_invalid.png')
            
                el_click(driver,"com.jiuai:id/linearLayout_mask")
            except:
                login_input_verify(driver,username,valid_pwd)
                el_click(driver,cfg.get('login','loginbtn'))
                screenshot(driver,'screenshot/Login_valid_success.png')
                
                el_click(driver,"com.jiuai:id/linearLayout_mask")
    except:
        return False


def logout(driver):
    sleep(2)
    el_click(driver,cfg.get('my','setting'))
    el_click(driver,cfg.get('setting','logout'))

    #wait 2s
    sleep(2)
    el_click(driver,cfg.get('setting','btn_positive'))
