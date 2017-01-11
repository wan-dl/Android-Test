
#Python Appium Api

####  应用安装、删除 

1.检查应用是否已经安装

`driver.is_app_installed("com.packagename")`

2.应用安装

`driver.install_app('/path/com.packagename.apk')`

3.卸载应用

`driver.remove_app('com.packagename.apk')`


#### 应用操作相关

1.启动应用

`driver.launch_app()`

2.关闭应用

`driver.close_app();`

3.重置应用

`driver.reset()`

4.把当前应用放到app后台

`driver.background_app(10)`

#### 文件操作相关

1.从设备中拉出文件

`driver.pull_file('path/filename')`

2.向设备推送文件

`data = "some data for the file"
 path = "/data/file.txt"
 driver.push_file(path,data.encode('base64'))`

#### 屏幕相关

1.锁定屏幕 

`drvier.lock(10)`

2.屏幕滑动

`driver.swipe(75,500,75,0,0.8)`

3.屏幕缩放

`driver.pinch(element=e1)`

4.屏幕触摸

`action = TouchAction(driver)
action.press(element=e1,x=10,y=10).release().perform()`

####  键盘相关

1.在ios上收起 键盘

`driver.hide_keyboard()`

2.发送键盘事件

`driver.keyevent(176)`

#### 设备相关

1.摇晃设备

`driver.shake()`

#### 应用上下文

1.列出所有的可用上下文

`driver.contexts`

2.列出当前上下文

`driver.current_context`

3.将上下文切换到默认上下文

`driver.switch_to.context(None)`

4.应用的字符串

`driver.app_strings`


#### Activity 相关

1.获得activity

`driver.current_activity`
