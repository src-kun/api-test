#! usr/bin/python 
#coding=utf-8

import logging  
import os  
import time

#项目路径
log_path = os.path.split(os.path.realpath(__file__))[0] + '/'

#获取当前日期作为文件名
def getFiltName():
	ISOTIMEFORMAT='%Y-%m-%d'
	return time.strftime( ISOTIMEFORMAT, time.localtime())
	
def getLogger(lg = 'bloblastLog'): 

	# 创建一个log,可以考虑如何将它封装  
	log = logging.getLogger(lg)  
	log.setLevel(logging.INFO)  
	  
	# 创建一个handler，用于写入日志文件
	fh = logging.FileHandler(os.path.join(log_path + getFiltName() + '.log'))
	fh.setLevel(logging.INFO)

	# 再创建一个handler，用于输出到控制台  
	ch = logging.StreamHandler()  
	ch.setLevel(logging.INFO)  
	  
	# 定义handler的输出格式
	formatter = logging.Formatter('%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - %(levelname)s - %(message)s')  
	fh.setFormatter(formatter)  
	ch.setFormatter(formatter)  
	  
	# 给log添加handler  
	log.addHandler(fh)  
	log.addHandler(ch)  
	  
	# test  
	#log.error('hello world, i\'m log helper in python, may i help you')  
	return log
logger = getLogger()