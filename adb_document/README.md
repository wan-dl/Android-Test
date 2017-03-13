[toc]

# Android ADB

### 计算启动时间

```
 $ adb shell am start -W com.jiuai/com.jiuai.activity.MainActivity
```


## adb shell pm


### adb shell pm list packages

```
系统应用 $ adb shell pm list packages -s	

第三方应用 $ adb shell pm list packages -3

$ adb shell pm list packages -f

包名以及安装来源 $ adb shell pm list packages -i

禁用的应用 $ adb shell pm list packages -d

可用的应用 $ adb shell pm list packages -e
```

### 安装应用

```
adb shell pm install <PackageName>
```

### 列出应用信息

```
adb shell pm dump <PackageName>
```

### 授予权限

```
 adb shell pm grant <包名>  <权限名>
```

### 撤销应用权限

```
adb shell pm revoke PackAge <权限名称>
```
### 清除手机应用数据

```
adb pm clear
```

### 列出所有硬件信息

```
adb shell pm list features
```

### 列出系统上所有的用户

```
adb shell pm list user
```

## adb shell am

### 结束应用

```
adb shell am force-stop
```

### 停止进程

```
adb shell am kill-all
```

### 发送文本

```
   adb shell input text HELLO
```

### 发送按键事件

```
   adb shell input keyevent 3
```

### 模拟触摸事件

```
adb shell input tap 1000 800
```

### 模拟长按事件

```
adb shell input tap 1000 800 1000 800 2000
```

### 模拟滑动事件

```
adb shell input swipe 1000 800 100 800
```

### 监控crash

```
  adb shell am monitor
```

## adb shell dumpsys

> adb shell dumpsys services

参数  | 使用说明  |备注	
------|------|----------
包信息| adb shell dumpsys package
网络连接| adb shell dumpsys connectivity
网络策略	| adb shell dumpsys netpolicy
网络状态	| adb shell dumpsys netstats
网络管理	| adb shell dumpsys network_management
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
