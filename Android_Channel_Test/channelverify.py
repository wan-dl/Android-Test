#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__ = "youxian_Tester <sx.work@outlook.com> 2016-04-13"
__vserion__ = "v1.0"

''' 
环境依赖Java,python2.7(需要安装requests/pandas库)

通过反编译android apk，获取AndroidManifest.xml文件中的渠道号等各项key信息
'''

import os,sys
import shutil
import re
import requests
import csv
import time
import random
from pandas import DataFrame,Series
import pandas as pd

#设置安卓渠道版本所在目录,ApkTool可不设
#version_catalogue = r"E:\Android App\file"
version_catalogue = str(raw_input(" \n -> Please input App Channel catalogue: "))
ApkTool = r"D:\Android\apktool.jar"
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
apktool_download_url = 'https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.1.0.jar'

#存放测试结果
script_dir = os.getcwd()

try:
    if os.path.isdir(version_catalogue):
    	vapk = [ cv for cv in os.listdir(version_catalogue) if os.path.splitext(cv)[1] == '.apk' ]
        if len(vapk) !=0:	
    	    print(" -> Total: \033[1;37;42m {0} \33[0m Apk. ".format(len(vapk)))
        else:
	        print(" -> No has ApkFile.")
	        raise NameError
except (NameError,OSError,IOError):
    print(" -> Error: Please check File PATH.")
    sys.exit()
else:
    os.chdir(version_catalogue)

#拷贝或下载apktool.jar反编译工具
if os.path.exists(os.path.join(version_catalogue,'apktool.jar')):
    print(" ->{0} Has found a decompiler apktool.jar.\n".format(version_catalogue))
elif os.path.isfile(ApkTool):
    shutil.copy(ApkTool,version_catalogue)
else:
    with open('apktool.jar','wb') as atool:
        print(" -> The Computer is not exists apktools.jar,Will begining Download Apktools.jar......")
        atool.write(requests.get(apktool_download_url).content)

start_time = time.time()

#反编译android apk
def decompiler(vdir):
    vapk = [ cv for cv in os.listdir(vdir) if os.path.splitext(cv)[1] == '.apk' ]
    print(" -> The Path has found {0} channel version,is in decomopiling,Please wait.....\n".format(len(vapk))) 
    for idx,apk in enumerate(vapk):
        channeldir,extension = os.path.splitext(apk)
        if os.path.isdir(channeldir):
            pass
        else:
            print(" -> The \033[1;37;44m {0} \33[0m Apk is processing : {1}".format(idx,apk))
            os.popen('java -jar apktool.jar d -s {0}'.format(apk))
    reverse_apk_folder = [ opf for opf in os.listdir(vdir) if os.path.isdir(opf) ]
    print("-------------------------------------------------------------------")
    print(" -> {0} Finish Apk decompiling.".format(now))
    print(" -> Total: \033[1;32;44m {0} \33[0m Apk Floder. ".format(len(reverse_apk_folder)))
    return vapk,reverse_apk_folder

#处理AndroidManifest.xml文件
def handling(filename,text):
    textual_value = ""
    with open(filename,'r+') as m:
        line = [ line.strip() for line in m.readlines() if text in line ]
        for n in line:
            value = n.split('=')[2]
            #使用strip过滤"/>//--等特殊字符
            textual_value = value.strip('"/>// --')
    return textual_value

#遍历反编译后的apk文件夹，通过AndroidManifest.xml文件获取渠道号
def get_apk_umeng_value(reverse_folder):
    #设置要查找的文本
    text_umeng_channel = "UMENG_CHANNEL"
    text_umeng_appkey = "UMENG_APPKEY"
    text_umeng_message_secret = "UMENG_MESSAGE_SECRET"
    text_easemob_appkey = "EASEMOB_APPKEY"
    text_amap = "com.amap.api.v2.apikey"

    umeng_channel = []
    umeng_appkey = []
    umeng_message_secret = []
    easemob_appkey = []
    amap = []

    for rfn in reverse_folder:
        manifest = os.path.join(version_catalogue,rfn,'AndroidManifest.xml')
        #友盟渠道号
        umeng_channel.append(handling(manifest,text_umeng_channel))
        #友盟appkey
        umeng_appkey.append(handling(manifest,text_umeng_appkey))
        #友盟UMENG_MESSAGE_SECRET
        umeng_message_secret.append(handling(manifest,text_umeng_message_secret))
        #环信
        easemob_appkey.append(handling(manifest,text_easemob_appkey))
        #高德地图
        amap.append(handling(manifest,text_amap))
    return umeng_channel,umeng_appkey,umeng_message_secret,easemob_appkey,amap

#随机取签名
def get_apk_signature(reverse_folder):
    cert_path = "original//META-INF"
    cert = [ os.path.join(version_catalogue,folder,cert_path,'JIUAI.RSA') for folder in reverse_folder ]
    num = random.randint(0,len(cert))
    return os.popen('keytool.exe -printcert -v -file {0}'.format(cert[num])).read()

#验证app签名
apkname,reverse_folder = decompiler(version_catalogue)
with open(script_dir + "//signature.txt",'wb') as s:
    signature_info = get_apk_signature(reverse_folder)
    s.writelines(signature_info)


#输出测试结果：将apk渠道号写入csv文件
def output_test_results():

    #获取apk名称和友盟渠道号
    apkname,reverse_folder = decompiler(version_catalogue)
    umeng_channel_value,umeng_appkey_value,umeng_message_secret_value,easemob_appkey_value,amap_value = get_apk_umeng_value(reverse_folder)
    
    #判断apk名称和友盟渠道值是否对应
    judge_results = []
    for x,y in zip(umeng_channel_value,apkname):
       if x in y:
            t = 'True'
            judge_results.append(t)
       else:
            f = 'False'
            judge_results.append(f)

    test_result = {"APKNAME":apkname,"UMENG_CHANNEL":umeng_channel_value,"CHANNEL_RESULTS":judge_results, \
                "UMENG_APPKEY":umeng_appkey_value,"UMENG_MESSAGE_SECRET":umeng_message_secret_value,\
                "EASEMOB_APPKEY":easemob_appkey_value,"AMAP":amap_value}
    frame = DataFrame(test_result,columns=["APKNAME","UMENG_CHANNEL","CHANNEL_RESULTS","UMENG_APPKEY",
                    "UMENG_MESSAGE_SECRET","EASEMOB_APPKEY","AMAP"])
    print(frame)

    channel_verify_results = zip(apkname,umeng_channel_value,judge_results,\
            umeng_appkey_value,umeng_message_secret_value,easemob_appkey_value,amap_value)

    #将结果写入csv文件
    os.chdir(script_dir)
    with open('Channel_testResult.csv','wb') as f:
        w = csv.writer(f)
        w.writerow(["APKNAME","UMENG_CHANNEL","CHANNEL_RESULTS","UMENG_APPKEY",
                    "UMENG_MESSAGE_SECRET","EASEMOB_APPKEY","AMAP"])
        w.writerows(channel_verify_results)
    
    print(" \n -> Test Result is writing :< Channel_testResult.csv >.\n")
    return channel_verify_results,w

output_test_results()

#打印签名信息
print(signature_info)

end_time = time.time()
print(" -> Running Time is: \033[1;37;42m {0} \33[0m".format(end_time-start_time))
  
os.system("pause")
