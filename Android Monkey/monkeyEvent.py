#!/usr/bin/env python
# -*- coding: utf8 -*-
# 2016-09-06

__auther__ = "youxian_tester <sx.work@outlook.com->"
__version__ = "v1.2"

import os
import time
import shutil
import random
import pickle
import logging

#获取当前目录
script_dir = os.getcwd()

#获取当前时间
currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print currentTime
#设置要测试的app的包名
com_package_name = "com.jiuai"

def str_sub(content,num):
    ct = content.replace('[','').replace(']','')
    return ct.split(':')[num].strip()

def device_detecting():
    """
    Detecting Android Mobile.
    Objective:解决当多个手机连接电脑，Android adb shell命令使用问题。
    """
    phone_brand = []
    serial_num = []
    device_list = os.popen(" adb devices -l").read()
    if "model" in device_list:
        serial_num = [sn.split()[0] for sn in device_list.split('\n') if sn and not sn.startswith('List')]
        for sn in serial_num:
            for mi in os.popen("adb -s {0} shell getprop".format(sn)):
                if "ro.build.fingerprint" in mi:
                    model = str_sub(mi,1).split('/')
                    phone_brand.append(model[0] + '/' + model[1])
    else:
        print("\n Did not detect any Device.")
    devices_info = dict(zip(phone_brand,serial_num))
    return devices_info

#发送随机事件到app
def run_events(phone_sn,packageName):
    return os.system("adb -s {0} shell monkey \
        -p {1} \
        --throttle  10 \
        --monitor-native-crashes \
        --pct-touch  5 \
        --pct-nav 5 \
        --pct-majornav 15 \
        --pct-motion 10 \
        --pct-appswitch 60 \
        --pct-anyevent 5 \
        -v -v -v 100".format(phone_sn,packageName))                                                                                                                                                                                                                                                                                                                                 

# 手机日志清除工作
def cleanup(phone_sn,packageName):
    return os.system("adb -s {0} shell logcat -c {1}".format(phone_sn,packageName))

#将日志写入文件
def log(phone_sn):
    #logfile = ''.join(str(time.time()) + '.log')
    #return os.popen("adb -s {0} shell logcat -d *:W > {1}".format(phone_sn,logfile))
    with open(str(time.time())+'.log','w') as f:
        f.writelines(os.popen("adb -s {0} shell logcat -d *:W".format(phone_sn)))

#执行
try:
    #获取手机的sn
    print("\n %s" % device_detecting())
    phone_sn = raw_input(" \n -> Please input mobile brand to connect:")
        
    try:
        cleanup(phone_sn,com_package_name)
        run_events(phone_sn,com_package_name)
    except Exception,e:
        print(e)
    finally:
        log(phone_sn)
        
except Exception,e:
    print(e)
