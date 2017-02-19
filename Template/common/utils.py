#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    Appium Webdriver utils.
    Easy to use appium webdriver method.
'''

__author__ = "wdl"
__copyright__ = "Copyright 2016"
__version__ = "v1.0.5"

import os
import sys
import time
import unittest
from time import sleep
from appium import webdriver

def wait_time(func):
    def inner(*args):
        time.sleep(0.5)
        f = func(*args)
        time.sleep(0.5)
        return f
    return inner

# element locators
# element click
def el_id_click(driver,el):
    return driver.find_element_by_id(el).click()

def el_class_click(driver,el):
    return driver.find_element_by_class_name(el).click()

def el_xpath_click(driver,el):
    return driver.find_element_by_xpath(el).click()

#action
def el_send_keys(driver,el,data):
    return driver.find_element_by_id(el).send_keys(data)

def el_text(driver,el):
    return driver.find_element_by_id(el).text

@wait_time
def screenshot(driver):
    filename = ''.join("../logs/" + str(time.time()) + ".png")
    return driver.get_screenshot_as_file(filename)

# Swipe: Left Right Up Down
class MobileSwipe():
    
    def __init__(self):
        pass

    def swipe_up(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/2, height/4,width/2, height/4*3, 800)

    def swipe_down(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/2, height/4*3,width/2, height/4, 800)

    def swipe_down_half(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/2, height/4*3,width/2, height/4*2, 800)

    def swipe_left(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/4*3, height/2,width/4, height/2, 800)

    def swipe_right(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/4, height/2,width/4*3, height/2, 800)

if __name__ == "__main__":
    MobileSwipe()
