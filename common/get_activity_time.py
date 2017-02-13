#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re
import csv
from diagnostics import InfoGathering

#设置apk包名
package_name = "com.jiuai"

# set phone_sn
phone_sn = '79AEALJ342EL'

#实例化InfoGathering类
uss = InfoGathering()

with open("usagestats.csv",'wb') as f:
    w = csv.writer(f)
    w.writerow(["activity_name","start_count","0-250m","250-500ms","500-750ms","750-1000ms", \
            "1000-1500ms","1500-2000ms","2000-3000ms","3000-4000ms","4000-5000ms",">=5000ms"])
    w.writerows(uss.usagestats(phone_sn,package_name))

 
