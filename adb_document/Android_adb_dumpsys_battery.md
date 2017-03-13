
# Android_Adb_dumpsys_battery

>手机每个硬件的耗电量是不一样的！比如屏幕就是耗电大户！其它一些元件则耗电量非常小！
> 使用android dumpsys工具可以获取电池以及电量消耗信息！
>dumpsys工具：battery、batterystatus

# 1. 电池信息
---
#### 1.1  获取手机电池信息
adb命令:```   adb shell dumpsys battery```
得到信息如下：
```
  AC powered: false
  USB powered: true
  Wireless powered: false
  status: 1            #电池状态：2：充电状态 ，其他数字为非充电状态           
  health: 2            #电池健康状态：只有数字2表示good
  present: true      #电池是否安装在机身
  level: 55             #电量: 百分比
  scale: 100
  voltage: 3977      #电池电压
  current now: -335232
  temperature: 335      #电池温度，单位是0.1摄氏度
  technology: Li-poly    #电池种类
```
#### 1.2 改变手机电池状态
>手机连接到电脑，默认为充电状态

切换手机电池为非充电状态：  ```adb shell dumpsys battery set status 1```
#### 1.3. 改变手机电量
> 改变手机电量！ 亲，这是真的 ！神奇的一刻

让手机电量显示百分百： ``` adb shell dumpsys battery set level 100```
让手机电量显示1：         ``` adb shell dumpsys battery set level 1```
# 2. 电量消耗信息
---
>关于电量，主要是通过battery-historian工具来获取。
https://github.com/google/battery-historian 

#### 2.1 获取电量消耗信息
```
获取整个设备的电量消耗信息： adb shell dumpsys batterystats  | more
获取某个apk的电量消耗信息：  adb shell dumpsys batterystats  com.Package.name | more
```
由于输出信息太多，可使用命令more 或者 less 分篇查看
输出信息如下(由于篇幅，只粘贴部分）：
```
Battery History:
    -1d04h22m36s181ms 044 20080000 status=charging health=good plug=usb temp=335 volt=3809 +plugged +sensor
    -1d04h21m27s713ms 044 640a0000 +wifi +wifi_running +wake_lock
    -1d04h21m23s278ms 044 6c0a0100 +phone_scanning phone_state=out
    -1d04h21m19s102ms 044 2c0a0100 -wake_lock
    -1d04h21m05s005ms 044 6c0a0100 +wake_lock
    -1d04h20m51s486ms 044 6d0a0100 +wifi_scan
    -1d04h20m49s211ms 044 6c0a0100 -wifi_scan
    -1d04h20m41s478ms 044 6c0a0100
    -1d04h20m31s476ms 044 6d0a0100 +wifi_scan
    -1d04h20m29s174ms 044 6c0a0100 -wifi_scan
    -1d04h20m24s353ms 044 2c0a0100 -wake_lock
    -1d04h20m21s474ms 044 6d0a0100 +wifi_scan +wake_lock
    -1d04h20m21s125ms 044 6d0a0100
    -1d04h20m16s847ms 044 2c0a0100 -wifi_scan -wake_lock
```
也可以将上述命令标准输出到一个文件，来进行分析。
+ windows ： > xxx.txt
+ Mac/Linux： > xxx.txt 

#### 2.2 将获得的数据转换为可视化的html文件
命令：```python historian.py xxx.txt > xxx.html```
Google Python脚本下载地址：https://github.com/google/battery-historian

# 3. 其他关于android电池电量优秀文章
---
1. 传输数据时避免消耗大量电量：
     http://hukai.me/android-training-course-in-chinese/connectivity/efficient-downloads/index.html
2. Android性能优化之电量篇：
    http://hukai.me/android-performance-battery/
