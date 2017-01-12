# android

> 注意：脚本运行的环境依赖于：java、android adb、apktool.jar、python2.7以及部分python第三方库！

#### 1.脚本说明

######	1.1 获取android apk友盟渠道号

> 国内市场上有许许多多的应用市场，常见的有：百度、360、腾讯应用宝、豌豆荚等，其他手机厂家如小米、华为、魅族、三星等都有自己的应用市场，林林总总有上百家！
每次发版验证渠道号的工作量就不小！希望自动去获取apk的友盟渠道号，并自动进行校验。

apk的渠道号一般在AndroidManifest.xml文件中，将apk反编译即可得到<渠道号>。
我们使用apktool.jar工具。
```
    java -jar apktool.jar d -f name.apk
```
输出结果如下：
```
E:\Android App>java -jar apktool.jar d -f name.apk
I: Using Apktool 2.1.0 on name.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: C:\Users\Administrator\apktool\framework\1.apk
I: Regular manifest package...
I: Decoding file-resources...
W: Cant find 9patch chunk in file: "drawable-xxxhdpi-v4/details_rectangle_pinkage.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-xxxhdpi-v4/personcenter_sign_in_bg.9.png". Renaming it to *.png.
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```
[apktool.jar 下载地址](https://bitbucket.org/iBotPeaches/apktool/downloads/)

反编译成功后，得到AndroidManifest.xml。

具体代码见[channelverity.py](https://github.com/J-test/Android/blob/master/channelverify.py)

输出结果如下：
```
-------------------------------------------------------------------
 -> 2016-05-29 10:37:04 Finish Apk decompiling.
 -> Total: 23 Apk Floder.
                                       ApkName   Umeng_Channel Results
0   com.xxxxxx_1.1.3-android_market-release.apk  android_market    True
1            com.xxxxxx_1.1.3-anzhi-release.apk           anzhi    True
2            com.xxxxxx_1.1.3-baidu-release.apk           baidu    True
3           com.xxxxxx_1.1.3-chuizi-release.apk          chuizi    True
4           com.xxxxxx_1.1.3-huawei-release.apk          huawei    True
5           com.xxxxxx_1.1.3-jifeng-release.apk          jifeng    True
6            com.xxxxxx_1.1.3-jinli-release.apk           jinli    True
7            com.xxxxxx_1.1.3-kupai-release.apk           kupai    True
8             com.xxxxxx_1.1.3-letv-release.apk            letv    True
9        com.xxxxxx_1.1.3-lianxiang-release.apk       lianxiang    True
10           com.xxxxxx_1.1.3-meizu-release.apk           meizu    True
11          com.xxxxxx_1.1.3-mumayi-release.apk          mumayi    True
12            com.xxxxxx_1.1.3-oppo-release.apk            oppo    True
13              com.xxxxxx_1.1.3-pp-release.apk              pp    True
14         com.xxxxxx_1.1.3-sanxing-release.apk         sanxing    True
15           com.xxxxxx_1.1.3-sogou-release.apk           sogou    True
16         com.xxxxxx_1.1.3-tengxun-release.apk         tengxun    True
17            com.xxxxxx_1.1.3-vivo-release.apk            vivo    True
18       com.xxxxxx_1.1.3-wandoujia-release.apk       wandoujia    True
19          com.xxxxxx_1.1.3-xiaomi-release.apk          xiaomi    True
20     com.xxxxxx_1.1.3-yingyonghui-release.apk     yingyonghui    True
21     com.xxxxxx_1.1.3-_360shouzhu-release.apk     _360shouzhu    True
22      com.xxxxxx_1.1.3-_91zhushou-release.apk      _91zhushou    True

 -> Test Result is writing :< Channel_testResult.csv >.

Running Time is: 19.3949999809

```
##### 2. adb shell dumpsys
> adb shell dumpsys命令可得到app的基本信息.包括包信息、cpu、内存、电量、wifi、页面启动时间.
	
 1. [ Android debug dumpsys ](https://source.android.com/devices/tech/debug/dumpsys.html)
 2. [ Android Testing performance ](https://developer.android.com/training/testing/performance.html)

