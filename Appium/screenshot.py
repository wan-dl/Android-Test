#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

'''
建立文件夹用以存放截图
'''

if os.path.isdir('screenshot'):
    pass
else:
    os.mkdir('screenshot')