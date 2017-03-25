#-*-coding=utf-8 -*-

import unittest,HTMLTestRunner
import os,time
#列出某个文件夹下的所有 case,这里用的是 python，
#所在 py 文件运行一次后会生成一个 pyc 的副本
"""
caselist=os.listdir('E:\\python\\Baidutest\\test_case')
for a in caselist:
    s=a.split('.')[1] #选取后缀名为 py 的文件
    if s=='py':
    	print a
        #此处执行 dos 命令并将结果保存到 log.txt
        #os.system('E:\\python\\Baidutest\\test_case\\%s 1>>log.txt 2>&1'%a)
        #os.system('E:\\python\\Baidutest\\test_case\\baidu.py ')"""
path = os.getcwd() + "\\test_case"
#print path
caselist = os.listdir(path)
for a in caselist:
    s = a.split(".")[1]
    if s == "py":
        #print a
        pass
def creatsuite():
    testunit = unittest.TestSuite()
    #discover方法定义
    discover = unittest.defaultTestLoader.discover(path,
                                                   pattern = "test*.py",
                                                   top_level_dir = None)
    #print discover

    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            #print testunit
    return testunit

alltestname = creatsuite()
#print alltestname

filename = ".//report//"+time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))+u"测试报告.html"
fb=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream = fb,
	                  title = u"测试报告",
	                  description = u"用例执行情况:"
	                   )
#执行测试
runner.run(alltestname)
