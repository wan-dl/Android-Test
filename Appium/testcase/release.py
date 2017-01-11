#!/usr/bin/env python
#-*- coding:utf-8  -*-

# @auther:jiuai
# 2016/07/24
# TestCase:商品发布

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from common import screenshot
from common import el_click,el_send_keys,el_xpath_click
from common import el_text
from common import MobileSwipe

# config.ini
cfg = ConfigParser()
cfg.read('config.ini')

# jiuai_data.dat
tdi= ConfigParser()
tdi.read('jiuai_data.dat')

# 滑动
sw = MobileSwipe()

# set goods data
goods_title = tdi.get('release','goods_title')
goods_describe = u'PRO 6采用了压力感应屏幕，魅族称其为3D Press，并搭载了索尼IMX 230摄像头'
goods_original_price = '1999'
goods_sale_price = '1200'

# 选择商品分类
def set_goods_type(driver):
    """ Func: Goods Type

        //android.widget.ListView[2]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]
    """
    try:
        # set Goods Type
        el_click(driver,cfg.get('release','goods_type'))
        screenshot(driver,'screenshot/Release_GoodsType_init_page.png')

        # 分类: 一级
        driver.find_element_by_xpath('//android.widget.FrameLayout[1]').click()
        screenshot(driver,'screenshot/Release_GoodsType_first.png')
        #分类：二级
        el = "//android.widget.ListView[2]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]"
        el_xpath_click(driver,el)
    except:
        screenshot(driver,'screenshot/Release_GoodsType_error.png')
        return False

# 添加照片
def add_photo(driver):
    """ 选择照片
    
        //android.widget.GridView[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]
    
        usage:
            在选择图片页面,从上到下,第一张照片: FrameLayout为[1]
    """
    try:
        el_click(driver,cfg.get('release','main_release'))
        sleep(1)
        screenshot(driver,'screenshot/Release_1_Photo_init_page.png')

        sleep(1)
        el = "//android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.CheckBox[1]"
        #el_xpath_click(driver,e1)
        driver.find_element_by_xpath("//android.widget.CheckBox").click()
        sleep(1)
    except:
        return False
    else:
        screenshot(driver,'screenshot/Release_1_Photo_choice_finish.png')
        el_click(driver,cfg.get('release','ok'))
        screenshot(driver,'screenshot/Release_1_Photo_release.png')

# 录制视频
def add_video(driver):
    """ 添加视频使用xpath定位

        //android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[3]/android.widget.ImageView[1]
        
        Usage:
            在当前页面,添加图片视频区域,从左到右,从1开始计数,<添加视频>按钮处于第几个,则RelativeLayout填写几即可.
            如：在只添加一张图、当前区域未进行滑动的情况下,RelativeLayout则为[3]
            
            若添加图片视频区域进行了滑动操作,添加视频框输入第一个，则RelativeLayout为[1]
    """
    try:
        screenshot(driver,'screenshot/Release_Video_init_page.png')

        el = "//android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[3]/android.widget.ImageView[1]"
        el_xpath_click(driver,el)

        # find: capture Video btn
        capture_btn = driver.find_element_by_id(cfg.get('release','capture_btn'))
        # 长按录制10s
        action = TouchAction(driver)
        action.long_press(capture_btn,None,None,10000).perform()

        screenshot(driver,'screenshot/Release_Video_capture_finish.png')        

        sleep(1)
        el_click(driver,cfg.get('release','capture_finish'))
        screenshot(driver,'screenshot/Release_Video_capture_commit.png')
        sleep(5)
    except:
        try:
            screenshot(driver,'screenshot/Release_Video_error.png')
            el_click(driver,cfg.get('release','capture_close'))
        except:
            pass

# 选择品牌
def choice_brand(driver):
    try:
        el_click(driver,cfg.get('release','choice_brand'))
        screenshot(driver,'screenshot/Release_Brand_init_page.png')

        el = "//android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]"
        el_xpath_click(driver,el)
    except:
        return False    
    else:
        screenshot(driver,'screenshot/Release_Brand_select_finish.png')

def goods_attrib_select(driver,attrib_name,attrib_content): 
    """ attrib_name: 商品属性规格名称
           1.存储容量、手机维修、手机保修、手机外观、屏幕情况、购买情况、全新非全新
           2.在未滑动屏幕时，从上到下，元素定位:
               //android.widget.LinearLayout[1]  1 2 3 ...
        attrib_content: 属性内容 LinearLayout 1 2 3 ..

        Usage:
            goods_attrib_select(driver,1,1)
    """
    el = "//android.widget.LinearLayout[attribute_name_num]/android.widget.GridView[1]/android.widget.LinearLayout[attribute_content_num]/android.widget.CheckBox[1]"

    attribute = el.replace("attribute_name_num",attrib_name).replace("attribute_content_num",attrib_content)

    el_xpath_click(driver,attribute)

# 手机类商品属性规格
def goods_attribute(driver):
    try:
        el_click(driver,cfg.get('release','goods_attribute'))
        screenshot(driver,'screenshot/Release_GoodsAttribute_init_page.png')

        # 存储容量、手机维修、手机保修、手机外观、屏幕情况
        goods_attrib_select(driver,"1","2")
        goods_attrib_select(driver,"2","2")
        goods_attrib_select(driver,"3","2")
        goods_attrib_select(driver,"4","2")
        goods_attrib_select(driver,"5","2")
        screenshot(driver,'screenshot/Release_GoodsAttribute_choice_swipe_before.png')

        # 滑动到底部
        sw.down_swipe(driver)
        
        # 购买渠道、全新非全新
        goods_attrib_select(driver,"5","2")
        goods_attrib_select(driver,"6","2")
        screenshot(driver,'screenshot/Release_GoodsAttribute_finish.png')
        
    except:
        screenshot(driver,'screenshot/Release_GoodsAttribute_error.png')
    else:
        el_click(driver,cfg.get('release','complete'))
        screenshot(driver,'screenshot/Release_GoodsAttribute_end.png')


# 商品发布
def release_goods(driver):

    # 选择照片
    add_photo(driver)

    # 填写标题
    el_send_keys(driver,cfg.get('release','goods_title'),goods_title)
    
    # 选择商品分类
    set_goods_type(driver)

    # 选择商品是否全新
    el_click(driver,cfg.get('release','new'))

    # 填写商品描述
    el_send_keys(driver,cfg.get('release','goods_describe'),goods_describe)

    # 增加视频
    add_video(driver)

    # 商品所在地
    el_location = el_text(driver,cfg.get('release','goods_location'))
    locate_fail_content = u'位置获取失败'
    
    if locate_fail_content in el_location:
        el_click(driver,cfg.get('release','goods_location'))
        screenshot(driver,'screenshot/Release_select_goods_location.png')
        el_click(driver,cfg.get('release','goods_location_btn'))
    else:
        pass

    screenshot(driver,'screenshot/Release_pageSwipe_begin.png')
    for c in range(3):
        sw.down_swipe(driver)
    screenshot(driver,'screenshot/Release_pageSwipe_behind.png')

    # 商品原价、商品售价、是否包邮
    sleep(2)
    el_send_keys(driver,cfg.get('release','goods_original_price'),goods_original_price)
    el_send_keys(driver,cfg.get('release','goods_sale_price'),goods_sale_price)
    el_click(driver,cfg.get('release','free_postage'))

    # 点击确定发布或下一步
    btn_content = el_text(driver,cfg.get('release','determine_release_btn'))

    btn_next_content = u"下一步"

    if btn_next_content in btn_content:
        screenshot(driver,'screenshot/Release_first_page_end.png')
        el_click(driver,cfg.get('release','release_next'))
        screenshot(driver,'screenshot/Release_second_page_start.png')
        # 选择品牌
        choice_brand(driver)
        # 属性规格
        goods_attribute(driver)

        el_click(driver,cfg.get('release','determine_release_btn'))        
        screenshot(driver,'screenshot/Release_TwoPage_finish.png')
    else:
        el_click(driver,cfg.get('release','determine_release_btn'))        
        screenshot(driver,'screenshot/Release_OnePage_finish.png')

