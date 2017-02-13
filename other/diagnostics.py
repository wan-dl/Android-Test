#!/usr/bin/env python
# -*- coding: utf8 -*-
#Beijing.sanyuanqiao.youxian

__auther__ = "youxian_test <sx.work@outlook.com>"
__version__ = "v1.0"

import os
import re
from itertools import islice

'''
    adb shell dumpsys命令可得到app的基本信息.包括包信息、cpu、内存、电量、wifi、页面启动时间.
    Using Help:
    1) https://source.android.com/devices/tech/debug/dumpsys.html
    2) https://developer.android.com/training/testing/performance.html
'''

class InfoGathering():

    def __init__(self):
        self.om = os.system
        self.op = os.popen

    #用dumpsys package com.package得到包基本信息，包括安装信息、包基本信息
    def package_info(self,phone_sn,apk_package_name):
        op = self.op
        versioninfo = [] 
        for lines in op("adb -s {0} shell dumpsys package {1}".format(phone_sn,apk_package_name)):
            #添加userId字段到list,方便以后其他地段调用
            if 'userId' in lines:
                versioninfo.append(lines.strip().split("=")[0])
            if 'versionName' in lines:
                versioninfo.append(lines.strip().split("=")[1])
            if 'versionCode' in lines:
                versioninfo.append(lines[:18].strip().split("=")[1])
            if 'lastUpdateTime' in lines:
                versioninfo.append(lines.strip().split("=")[1])
        return versioninfo

    #内存信息
    #统计pss值（实际使用的物理内存（比例分配共享库占用的内存）
    def meminfo(self,phone_sn,apk_package_name):
        op = self.op
        pss = ""
        try:
            meminfo = op("adb -s {0} shell dumpsys meminfo {1} | grep TOTAL".format(phone_sn,apk_package_name)).read() 
            pss = meminfo.split()[1]   
        except IndexError:
            pss = "0"
        return pss

    #cpu信息
    def cpuinfo(self,phone_sn,package_name):
        op = self.op
        try:
            cpuinfo = op("adb -s {0} shell dumpsys cpuinfo | grep {1}".format(phone_sn,package_name)).read()
            ci = cpuinfo.split()
            cputotal,user,kernel = ci[0],ci[2],ci[5]
        except IndexError:
            cputotal,user,kernel = "0%","0%","0%"
        return cputotal,user,kernel

    
    """ 
    注意：这里是Activity,不是App应用的启动时间！
        app应用的启动时间应该以页面完全显示为准，即应用第一帧.

    Activity启动:onCreat---onStart---onResume
        1. Start-Up time Statistics Application each activity page.
        2. According to the statistical period
        example = ["activity_name","start_count","0-250m","250-500ms","500-750ms","750-1000ms", \
            "1000-1500ms","1500-2000ms","2000-3000ms","3000-4000ms","4000-5000ms",">=5000ms"] 
    """

    #Activity每个页面启动时间       
    def usagestats(self,phone_sn,package_name):
        om = self.om
        search_keyword = ''.join(package_name + '.activity')
        om("adb -s {0} shell dumpsys usagestats | grep {1} > usagestats.log".format(phone_sn,search_keyword))

        activity_page_startup_time = []

        with open("usagestats.log","r") as ulog:
            lines = [ line.replace('>=','') for line in ulog ]
            for line in lines:
                resp = re.split(r"[:|,]",line)
                #使用islice跳过可迭代对象的元素个数
                page_time_bucket = dict( [ tb.strip().split("=") for tb in islice(resp,2,None) ] )
                print(resp[0])
                #Activity时间段统计：
                time_bucket = ["","","","","","","","","",""]
                
                if '0-250ms' in page_time_bucket:
                    time_bucket[0] = page_time_bucket["0-250ms"]

                if '250-500ms' in page_time_bucket:
                    time_bucket[1] = page_time_bucket["250-500ms"]

                if '500-750ms' in page_time_bucket:
                    time_bucket[2] = page_time_bucket["500-750ms"]

                if '750-1000ms' in page_time_bucket:
                    time_bucket[3] = page_time_bucket["750-1000ms"]

                if '1000-1500ms' in page_time_bucket:
                    time_bucket[4] = page_time_bucket["1000-1500ms"]

                if '1500-2000ms' in page_time_bucket:
                    time_bucket[5] = page_time_bucket["1500-2000ms"]

                if '2000-3000ms' in page_time_bucket:
                    time_bucket[6] = page_time_bucket["2000-3000ms"]

                if '3000-4000ms' in page_time_bucket:
                    time_bucket[7] = page_time_bucket["3000-4000ms"]

                if '4000-5000ms' in page_time_bucket:
                    time_bucket[8] = page_time_bucket["4000-5000ms"]

                if '5000ms' in page_time_bucket:
                    time_bucket[9] = page_time_bucket["5000ms"]

                activity_page_startup_time.append(tuple([resp[0]]+[resp[1]]+time_bucket))
        return activity_page_startup_time

    #获取apk流量信息
    def flowinfo(self,phone_sn,apk_package_name):
        om = self.om
        flowinfo = om("adb -s {0} shell dumpsys netstats {1}".format(phone_sn,apk_package_name))
        return flowinfo

if __name__ == "__main__":
    InfoGathering()
