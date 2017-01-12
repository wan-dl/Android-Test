#!/usr/bin/env python
# -*- coding:utf-8 -*

import os
import sys

def str_sub(content,num):
    ct = content.replace('[','').replace(']','')
    return ct.split(':')[num].strip()

def device_detecting():
    """
    Detecting Android Mobile.
    Objective:解决当多个手机连接电脑，Android adb shell命令使用问题.

    当只有一台手机时，使用adb shell getprop即可获取deviceId.
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
        sys.exit()
    devices_info = dict(zip(phone_brand,serial_num))
    return devices_info
#device_detecting()
