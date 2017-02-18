#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = "wdl"
__version__ = "v1.0"

import os
import sys
import platform

def check():

    if "ANDROID_HOME" in os.environ.keys():
        print("ANDROID_HOME environment.................Pass")
    else:
        print("No Found $ANDROID_HOME in PATH")

    if "Windows" not in platform.system():
        appium_path = str(os.popen("which appium").readlines())
        if "appium" in appium_path:
            print("Appium Environment...................Pass.")
        else:
            print("Appium Environment...................Fail.")

check()
