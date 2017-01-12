#!/usr/bin/env python
# -*- coding: utf8 -*-
# 2016-09-06

__auther__ = "youxian_tester <sx.work@outlook.com->"
__version__ = "v1.2"


# Monkey是android Sdk自带的一个工具，用于模拟随机事件
# Monkey运行业内标准：final release前，Monkey跑完的总次数应为25W次，其结果里不允许有nullPointException出现.

import os
import time
import shutil
import random
import pickle
import logging

#设置要测试的app的包名
com_package_name = "com.jiuai"

#获取当前目录
script_dir = os.getcwd()

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

    ''' 
    关于adb monkey,官网：https://developer.android.com/studio/test/monkey.html
    Monkey事件：
        --throttle 在事件之间插入固定延迟
        --pct-touch 触摸事件百分比
        --pct-nav 基本导航事件up/down/left/righ
        --pct-majornav 主要导航事件back key、 menu key等
        --pct-motion 动作事件
        --pct-syskeys 系统按键事件Home、Back等
        --pct-appswitch activity之间的切换事件
        --pct-anyevent 其他类型事件
        --pct-trackball 轨迹事件
        -v 日志级别
    Monkey调试选项：
        --ignore-crashes 忽略发生的崩溃继续运行
        --ignore-timeouts 忽略超时
        --ignore-security-exceptions 忽略安全异常
        --kill-process-after-error 发生错误后直接杀掉进程
        --monitor-native-crashes 监视并报告 Android 系统中本地代码的崩溃事件
        --wait-dbg 直到连接了调试器才执行monkey测试
    '''
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
