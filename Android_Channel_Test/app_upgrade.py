#!/usr/bin/env python
# -*- coding: utf8 -*-
# 2016-06-09
# Android app发版前最后检查

__auther__ = "youxian_tester <sx.work@outlook.com->"
__version__ = "v1.2"

import os
import shutil
import random
import pickle
import csv
from diagnostics import InfoGathering
from mobileDetecting import device_detecting

#获取当前目录
script_dir = os.getcwd()

#获取手机的sn
print("\n %s" % device_detecting())
phone_sn = raw_input(" \n -> Please input mobile brand to connect:")
#phone_sn = "79AEALJ342EL"

#路径检查
def check_path(directory):
    try:
        if os.path.isdir(directory):
            print(" -> The PATH True. \n")
            vapk = [ cv for cv in os.listdir(directory) if os.path.splitext(cv)[1] == '.apk' ]
        if len(vapk) == 0:
            raise NameError
    except IOError:
        print(" -> Error: Please check File path")

#设置渠道版本目录
new_version_catalogue = str(raw_input(" \n -> Please input New App Channel catalogue: "))
check_path(new_version_catalogue)

old_version_catalogue = str(raw_input(" -> Please input Old App Channel catalogue: "))
check_path(old_version_catalogue)

#设置要测试的app的包名
com_package_name = "com.jiuai"

#发送随机事件到app
def run_events(phone_sn):
    return os.popen("adb -s {0} shell monkey -p com.jiuai -s 10 \
     --kill-process-after-error  --monitor-native-crashes --pct-nav 15 \
     --pct-majornav 20 --pct-appswitch 30 --pct-motion 30  --pct-anyevent 5 \
     --throttle 20 -v -v -v 2000".format(phone_sn))

#diagnostics文件中的类
aig = InfoGathering()

#升级前版本信息获取
def apk_check_before_upgrade(phone_sn,com_package_name):
    #获取手机安装的所有第三方包
    tp = [ plp.strip().split(":")[1] for plp in os.popen("adb -s {0} shell pm list package -3".format(phone_sn)) ]

    if com_package_name in tp:
        print("\n Old app is installed the phone.\n")

        #获取apk三个信息：versionName,versionCode,LastUpdatetime
        before_upgrade_version_info = aig.package_info(phone_sn,com_package_name)
        before_upgrade_version_info[0] = com_package_name
        print(" -> Version Basic info:\n\t {0}".format(before_upgrade_version_info))
    else:
        print(" -> The phone is not installed old apk.")

# 安装apk,并获取信息
def install_apk(phone_sn,apkname,com_package_name):
    try:
        install_log = os.popen("adb -s {0} install -r {1}".format(phone_sn,apkname)).read()
        if "Success" in pickle.dumps(install_log):
            install_status = 'Success'

            #获取apk三个信息：versionName,versionCode,LastUpdatetime
            after_upgrade_version_info = aig.package_info(phone_sn,com_package_name)
            after_upgrade_version_info[0] = apkname
            after_upgrade_version_info.insert(1,install_status)

            print("{0} : Apk Install Successful.".format(apkname))
            print("\t Apk Info: {0} \n".format(after_upgrade_version_info))
        else:
            after_upgrade_version_info = []
            print("{0} : Apk Install Fail.".format(apkname))
    except OSError:
        print("Error")
    else:
        # clean Mobile app data
        os.popen("adb -s {0} shell pm clear {1}".format(phone_sn,com_package_name))

    return after_upgrade_version_info

#选择apk
def select_apk(directory):
    os.chdir(directory)
    apkname = [ vc for vc in os.listdir(directory) if os.path.splitext(vc)[1] == '.apk']
    print(" -> {0} : There are {1} apk file.".format(directory,len(apkname)))
    return apkname

# 手机清除工作
def cleanup(phone_sn,package):
    return os.system("adb -s {0} uninstall {1}".format(phone_sn,package))

'''
    Upgrade installation verification.
'''
def do(phone_sn,old_dir,new_dir,package):
    results = []
    old_apk,new_apk = select_apk(old_dir),select_apk(new_dir)
    #保证两个目录下apk数量相等
    onum,nnew = len(old_apk),len(new_apk)
    if onum < nnew:
        for cp in range(nnew - onum):
            new_apk[random.randrange(nnew)]
            shutil.copy(new_apk[random.randrange(nnew)],odir)
    else:
        pass

    for (oapk,napk) in zip(old_apk,new_apk):
        try:
            print("-------------------------------------------")
            cleanup(phone_sn,package)
            # install old version apk
            os.chdir(old_dir)
            oresults = install_apk(phone_sn,oapk,package)[:2]
        except:
            print(" Unistall old Apk Fail")

        try:
            # install new version apk
            os.chdir(new_dir)
            nresults = install_apk(phone_sn,napk,package)
            print(" -> This is {0} apk".format(new_apk.index(napk) + 1 ))
        except:
            print(" Install New Apk Fail")
        else:
            #随机monkey事件，检验新app的是否可以正常使用
            run_events(phone_sn)

        results.append(oresults + nresults)
    return results

#手机安装前检查
apk_check_before_upgrade(phone_sn,com_package_name)

#执行测试
test_results = do(phone_sn,old_version_catalogue,new_version_catalogue,com_package_name)
print(test_results)

#测试结果存放目录
os.chdir(script_dir)
with open('upgrade&install_testResult.csv','wb') as f:
    w = csv.writer(f)
    w.writerow(["OldVersionName","old upgrade to New","NewApk","Install_Status","VersionCode","VersionName","LastUpdateTime"])
    w.writerows(test_results)

print(" \n -> Test Result is writing :< upgrade&install_testResult.csv >.\n")
