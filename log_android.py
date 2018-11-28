#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import sys
import os
from logging.handlers import RotatingFileHandler
from kivy.logger import Logger as logger
import platform 
# 在外部存储创建呃文件夹名称
APP_NAME = 'kivy'
# 日志名称
LOG_NAME = 'kivy.log'
# 创建LOG目录
sys_os = platform.system()
RUN_DIR = os.getcwd()
# 外部存储路径
DATA_DIR = os.path.join('storage', 'emulated', '0', APP_NAME)
if sys_os=='Windows':
	# 如果是Windows测试环境使用运行目录
	DATA_DIR = RUN_DIR
else:
	if not os.path.exists(DATA_DIR):
		os.mkdir(DATA_DIR)
LOG_DIR = os.path.join(DATA_DIR, 'logs')
if not os.path.exists(LOG_DIR):
	os.mkdir(LOG_DIR)
# LOG文件目录
LOG_PATH = os.path.join(LOG_DIR, LOG_NAME)
# 创建Handler
standardFormatter = logging.Formatter('%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s')
FileHandler = RotatingFileHandler(LOG_PATH, maxBytes=20*1024*1024, backupCount=5)
FileHandler.setLevel(logging.INFO)
FileHandler.setFormatter(standardFormatter)
logger.addHandler(FileHandler)
logger.error(sys_os)
class Stdout(object):
	'''
		标准输出流
	'''
	def write(self, message):
		if message!='\n':
			logger.warning(message)		
class Stderr(object):
	'''
		标准错误流
	'''
	_message = ''
	def write(self, message):
		self.message = message
			
	def set_message(self, value):
		self._message += value
		if value=='\n':
			logger.error(self.message)
			self._message = ''
	
	def get_message(self):
		return self._message
	
	message = property(get_message, set_message)

sys.stdout = Stdout()
sys.stderr = Stderr()
