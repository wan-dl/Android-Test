
# Monkey测试

Monkey是android Sdk自带的一个工具，用于模拟随机事件

### Monkey运行业内标准：

  final release前，Monkey跑完的总次数应为25W次，其结果里不允许有nullPointException出现.
  
### 本脚本说明：

  核心是adb命令，通过python脚本处理，减少工作量。
