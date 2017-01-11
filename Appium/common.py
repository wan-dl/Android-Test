#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,sys
import unittest
from time import sleep
from appium import webdriver

# element locators
def el_click(driver,el):
    return driver.find_element_by_id(el).click()

def el_xpath_click(driver,el):
    return driver.find_element_by_xpath(el).click()

def el_send_keys(driver,el,data):
    return driver.find_element_by_id(el).send_keys(data)

def el_text(driver,el):
    return driver.find_element_by_id(el).text

def el_xpath_text(driver,el):
    return driver.find_element_by_xpath(el).text

def screenshot(driver,filename):
    return driver.get_screenshot_as_file(filename)

# Swipe: Left Right Up Down
class MobileSwipe():
    """解决：上滑、下滑、左滑、右滑 
    """
    def __init__(self):
        pass

    def up_swipe(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/2, height/4,width/2, height/4*3, 800)

    def down_swipe(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/2, height/4*3,width/2, height/4, 800)

    def left_swipe(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/4*3, height/2,width/4, height/2, 800)

    def right_swipe(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/4, height/2,width/4*3, height/2, 800)

if __name__ == "__main__":
    MobileSwipe()
