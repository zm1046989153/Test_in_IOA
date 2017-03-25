#_*_ coding:utf-8 _*_

#本模块用于读取配置信息

import codecs

#调用函数时候需要提供配置文件的名称，已字典形式返回配置文件中的配置信息
def getconfig(configname):
    with codecs.open("..//config//"+configname,"r","gbk") as file:
	#print file.read()
	configs = file.readlines()
	d = {}
	for config in configs:
		#去除头尾的转义字符
		info = config.rstrip()
		
                #去除配置文件中的空行和注释
		if info == "" or "#" in info:continue
		ms = info.split("=")
		#print ms
		
		#将配置信息转化为字典
		d[ms[0].strip()] = ms[1].strip()
	return d
