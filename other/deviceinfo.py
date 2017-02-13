#!/usr/bin/env python
# -*- coding: utf8 -*-
# 2016-05-01 

__auther__ = "youxian_tester <sxwork@outlook.com>"
__version__ = "v1.1.0"

import os
import shutil
import random
import pickle
import csv
import re

def str_sub(content,num):
    ct = content.replace('[','').replace(']','')
    return ct.split(':')[num].strip()

for mi in os.popen("adb shell getprop"):
    if "ro.build.fingerprint" in mi:
        print("Phone: {0}".format(str_sub(mi,1)))
    if "ro.serialno" in mi:
        print("Serial-number: {0}".format(str_sub(mi,1)))
    if "ro.sf.lcd_density" in mi:
        print("Pixel density: {0}".format(str_sub(mi,1)))
    if "dhcp.wlan0.ipaddress" in mi:
        print("Ip Address: {0}".format(str_sub(mi,1)))
    if "ro.build.version.release" in mi:
        print("System_Version: {0}".format(str_sub(mi,1)))