#!/usr/bin/env python
# -*- coding: utf8 -*-
#Beijing.sanyuanqiao.youxian

__auther__ = "youxian_test <sx.work@outlook.com>"
__version__ = "v1.0"

import os
import re
from itertools import islice

package_name = 'com.jiuai'

"""
2016-06-23
1.使用此方法可能统计不全activity
2.三星手机获取存在问题
"""

#获取app的每个activity  
def usagestats(package_name):
    search_keyword = ''.join(package_name + '.activity')
    os.popen("adb shell dumpsys usagestats | grep {0} > usagestats.log".format(search_keyword))

    activity_name = []
    with open("usagestats.log","r") as ulog:
        lines = [ line.replace('>=','') for line in ulog ]
        for line in lines:
            resp = re.split(r"[:|,]",line)
            activity_name.append(resp[0].strip())
    return {}.fromkeys(activity_name).keys()

#创建activity维护列表
with open("ActivityName_Maintenance.txt","w+") as anm:
    for idx,activityName in enumerate(usagestats(package_name)):
        print idx, activityName
        anm.write(activityName +"\n")