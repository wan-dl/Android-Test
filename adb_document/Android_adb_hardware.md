# Android adb 获取手机软件硬件信息

### 获取android系统属性

```
	adb shell getprop  

```

参数说明	| 命令
--------|-----------
手机序列号	| adb shell getprop ro.serialno
手机CID号	| adb shell getprop ro.carrier
系统版本号	| adb shell getprop ro.build.version.release


### 获取手机SN

```
	adb get-serialno
```

### 获取屏幕分辨率

```
	adb shell wm size
```

### 获取内核信息

```
	adb shell demsg
```

