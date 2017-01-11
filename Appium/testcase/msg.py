#!/usr/bin/env python
#-*- coding:utf-8  -*-

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser

#config.ini
cfg = ConfigParser()
cfg.read('config.ini')

"""
Func Msg:
    1. 客服聊天 
"""