[toc]

# Android ADB

### 计算启动时间

```
  adb shell am start -W com.jiuai/com.jiuai.activity.MainActivity
```

### 监控crash

```
  adb shell am monitor
```

### adb dumpsys
	
参数  | 使用说明  |备注	
------|------|----------
内存	|adb shell dumpsys meminfo
CPU|	adb shell dumpsys cpuinfo
帧率|	adb shell dumpsys gfxinfo
显示|	adb shell dumpsys display
电源|	adb shell dumpsys power
电池状态	|adb shell dumpsys batterystats
电池	|adb shell dumpsys battery
闹钟|	adb shell dumpsys alarm
位置	|adb shell dumpsys location
电话信息	|adb shell dumpsys telephony.registry
wifi信息	a|db shell dumpsys wifi
通知信息	|adb shell dumpsys notification
