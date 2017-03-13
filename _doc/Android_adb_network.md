#Android adb 网络信息查询

### adb shell dumpsys 网络服务

有4个跟网络相关的。分别为：

说明		| 命令							| 备注
--------|-------------------------------|-------------
网络状态	| adb shell dumpsys netstats	|
网络连接	| adb shell dumpsys connectivity|
网络策略	| adb shell dumpsys netpolicy	|
网络管理	| adb shell dumpsys network_management|

### 通过adb命令开启或关闭WiFi

```
  adb shell svc wifi enable 开启
  
  adb shell svc wifi disable  关闭
```
