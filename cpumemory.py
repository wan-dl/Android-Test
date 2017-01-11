#!/usr/bin/env python
# -*- coding: utf8 -*-
# 2016-04-14 

__auther__ = "youxian_tester <sx.work@outlook.com>"
__version__ = "v1.10"

import os
import shutil
import random
import time
import csv
from diagnostics import InfoGathering
from mobileDetecting import get_phone_sn

package_name = "com.jiuai"

#实例化InfoGathering文件中的类
aig = InfoGathering()

#get mobile sn
phone_sn = get_phone_sn()

cpu = []
info = []

#获取内存pss值,cpu
with open("mem.txt",'w+') as m:  
    for i in range(600): 
        pss_value = aig.meminfo(phone_sn,package_name)
        cpu_value = list(aig.cpuinfo(phone_sn,package_name))
        print pss_value,cpu_value
        time.sleep(2)
        cpu.append(cpu_value)
        m.write(pss_value +"\n")

#将获取的cpu利用率写入文档
with open("cpu.csv",'wb') as c:
    w = csv.writer(c)
    w.writerow(["cpu_total","cpu_user","cpu_kernel"])
    w.writerows(tuple(cpu)) 
        
