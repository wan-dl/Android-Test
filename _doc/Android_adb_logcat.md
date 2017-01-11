# Android logcat使用

## Android日志说明

当Android系统运行的时候，会搜集所有的系统信息。

logcat是Android系统的一个命令行工具，主要用来查看和过滤日志信息。

使用usb连接到手机设备，在电脑终端上输入 adb logcat ，android会将系统实时日志输出到终端，按 Ctrl + C结束。

## Android logcat介绍

要使用adb命令，首先需要安装Android SDK.adb命令在$ANDROID_HOME/platform-tools目录下.

安装好Android SDk并配置好环境变量后，在电脑终端执行：

`$ adb logcat`

或者进入Android手机，执行：

`$ adb shell`

`$ logcat`

## 清除日志缓冲区

清除日志，并只显示重置后的日志，命令：

` $ adb locat -c `

## 根据日志优先级过滤日志

语法：

` $ adb logcat *:# `


` V 详细日志(默认)
D 调试信息
I 正常使用时的日志信息
W 警告
E 错误
F 运行时发生的致命错误 `

所有的优先级都自动包括比它高的优先级，因此 `adb logcat *:W`包括警告、错误、致命信息。

## 使用管道，基于关键字内容进行日志过滤

比如，收集所有包括关键字"api"的日志：

` $ adb logcat | grep -i api `

关于linux管道与grep命令请自行搜索google.

## 增加日志颜色，提高日志可读性

命令：

` $ adb logcat -C`





