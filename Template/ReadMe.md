本文不在叙述Appium环境安装。
 如有需要请参考：http://www.jianshu.com/p/7a6fa7ab662b

#### 1. 创建项目目录
```
mkdir project{conf,common,logs,doc,tests}

#conf：存放appium-android配置设置，以及App页面元素配置文件；
#logs：存放日志以及截图；
#doc：存放文档；
#common：存放工具类的脚本；
#tests：存放测试脚本；
```
整个目录如下：

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1534169-a8b83a1eae33cb97.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 2. Appium Android配置文件
Appium Android Settings 设置如下：
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1534169-39e8fa8d2c7159eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Python脚本配置如下：
```
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import re
from appium import webdriver

sys.path.append("..")
#用于解决多个手机连接问题
from common.mobile import get_serialno

#Read mobile deviceId
device_id = get_serialno()

#Read mobile os Version
os_version = os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_id)).read()
    
def appium_start():
    config = {
        'platformName':'Android',                      #平台
        'platformVersion':os_version,                  #系统版本
        'deviceName':device_id,                        #测试设备ID
        # 'appPackage':'com.jiuai',
        # 'appActivity':'.activity.MainActivity',
        'app':'/Users/xiaohutu/GitHub/Android-Test/com.jiuai.apk',      #apk路径
        #'app':'D:\com.jiuai.apk',
        'newCommandTimeout':30,    
        'automationName': 'Appium',
        'unicodeKeyboard':True,                         #编码,可解决中文输入问题
        'resetKeyboard':True}
    return  webdriver.Remote('http://localhost:4723/wd/hub', config)
```
 上述脚本保存为：appium_config.py

备注：
```
from common.mobile import get_serialno
用于解决多个手机连接问题。具体脚本见：https://github.com/yi-heng/Android-Test/blob/master/Template/common/mobile.py
```
#### 3. Android元素定位
uiautomatorviewer是Android SDK自带的工具，在$ANDROID_HOME/tools目录下，可使用此工具查看页面元素。
使用的测试app为本公司的开发的：旧爱，如下：

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1534169-a980b2dd7240a5cf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
driver.find_element_by_id(resource-id).click()
```
建议：将所有的页面元素集中到一个文件，提高Appium脚本的复用性、可配置性，如命名为config.ini或el.ini
见另外教程：http://www.jianshu.com/p/980a82cde7df

#### 4. 测试脚本编写
先来一段脚本吧，如下：
```
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

```
1. 使用前，先要导入相关库。
2. 使用configparser读取ini或cfg配置文件。
3. 使用python unitest测试库
