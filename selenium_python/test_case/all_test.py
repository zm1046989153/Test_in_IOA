#coding=utf-8

import unittest,HTMLTestRunner
import time
#导入要测试的文件
import baidu,youdao

testunit = unittest.TestSuite()

#将测试用例加入到测试容器（套件）中

testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))

#执行测试套件
#runner=unittest.TextTestRunner()
#runner.run(testunit)
filename = "..//report//"+time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))+u"测试报告.html"
fb=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream = fb,
	                  title = u"测试报告",
	                  description = u"用例执行情况:"
	                   )
#执行测试
runner.run(testunit)