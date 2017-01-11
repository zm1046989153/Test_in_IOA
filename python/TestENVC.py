# _ * _ coding:UTF-8 _ * _

import os



base_text='''
# Copyright (c) 1993-1999 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
127.0.0.1 localhost
'''

ht={
'T10':'''
#Test Environment:T10(dns:10.10.17.93)
10.10.17.76 mx0.ioa.cn
10.10.17.77 i.ioa.cn
10.10.17.78 m0.ioa.cn
10.10.17.88 m1.ioa.cn
10.10.17.89 wf0.ioa.cn bt0.ioa.cn cd0.ioa.cn doc0.ioa.cn mm0.ioa.cn ct0.ioa.cn hr0.ioa.cn o0.ioa.cn crm0.ioa.cn
10.10.17.91 fs.ioa.cn
10.10.17.79 www.ioa.cn
10.10.17.80 login.im.ioa.cn
'''
,'T11':'''
#Test Environment:T11
10.10.17.81 mx0.ioa.cn
10.10.17.82 i.ioa.cn
10.10.17.83 m0.ioa.cn
10.10.17.83 m1.ioa.cn
10.10.17.86 wf0.ioa.cn bt0.ioa.cn cd0.ioa.cn doc0.ioa.cn mm0.ioa.cn ct0.ioa.cn hr0.ioa.cn o0.ioa.cn crm0.ioa.cn
10.10.17.94 fs.ioa.cn
10.10.17.84 www.ioa.cn
10.10.17.85 login.im.ioa.cn
'''
,
'T20':'''
#Test Environment:T20
10.10.18.7 mx0.ioa.cn
10.10.18.5 i.ioa.cn
10.10.18.8 m0.ioa.cn
10.10.18.9 m1.ioa.cn
10.10.18.2 wf0.ioa.cn bt0.ioa.cn cd0.ioa.cn doc0.ioa.cn mm0.ioa.cn ct0.ioa.cn hr0.ioa.cn o0.ioa.cn crm0.ioa.cn
10.10.18.6 fs.ioa.cn
10.10.18.3 www.ioa.cn
10.10.18.10 login.im.ioa.cn
'''
,
'T21':'''
#Test Environment:T21
10.10.18.16 mx0.ioa.cn
10.10.18.14 i.ioa.cn
10.10.18.18 m0.ioa.cn
10.10.18.19 m1.ioa.cn
10.10.18.11 wf0.ioa.cn bt0.ioa.cn cd0.ioa.cn doc0.ioa.cn mm0.ioa.cn ct0.ioa.cn hr0.ioa.cn o0.ioa.cn crm0.ioa.cn
10.10.18.15 fs.ioa.cn
10.10.18.12 www.ioa.cn
10.10.18.17 login.im.ioa.cn
'''
,
'T22':'''
#Test Environment:T22
10.10.18.26 mx0.ioa.cn
10.10.18.24 i.ioa.cn
10.10.18.28 m0.ioa.cn
10.10.18.29 m1.ioa.cn
10.10.18.21 wf0.ioa.cn bt0.ioa.cn cd0.ioa.cn doc0.ioa.cn mm0.ioa.cn ct0.ioa.cn hr0.ioa.cn o0.ioa.cn crm0.ioa.cn
10.10.18.25 fs.ioa.cn
10.10.18.22 www.ioa.cn
10.10.18.27 login.im.ioa.cn
'''
,
'T30':'''
#Test Environment:T30
10.10.18.36 mx0.ioa.cn
10.10.18.34 i.ioa.cn
10.10.18.38 m0.ioa.cn
10.10.18.39 m1.ioa.cn
10.10.18.31 wf0.ioa.cn bt0.ioa.cn cd0.ioa.cn doc0.ioa.cn mm0.ioa.cn ct0.ioa.cn hr0.ioa.cn o0.ioa.cn crm0.ioa.cn
10.10.18.35 fs.ioa.cn
10.10.18.32 www.ioa.cn
10.10.18.37 login.im.ioa.cn
'''
,
'T31':'''
#Test Environment:T31
10.10.18.46 mx0.ioa.cn
10.10.18.44 i.ioa.cn
10.10.18.48 m0.ioa.cn
10.10.18.49 m1.ioa.cn
10.10.18.41 wf0.ioa.cn bt0.ioa.cn cd0.ioa.cn doc0.ioa.cn mm0.ioa.cn ct0.ioa.cn hr0.ioa.cn o0.ioa.cn crm0.ioa.cn
10.10.18.45 fs.ioa.cn
10.10.18.42 www.ioa.cn
10.10.18.47 login.im.ioa.cn
'''
,
'T32':'''
#Test Environment:T32
10.10.18.56 mx0.ioa.cn
10.10.18.54 i.ioa.cn
10.10.18.58 m0.ioa.cn
10.10.18.59 m1.ioa.cn
10.10.18.51 wf0.ioa.cn bt0.ioa.cn cd0.ioa.cn doc0.ioa.cn mm0.ioa.cn ct0.ioa.cn hr0.ioa.cn o0.ioa.cn crm0.ioa.cn
10.10.18.55 fs.ioa.cn
10.10.18.52 www.ioa.cn
10.10.18.57 login.im.ioa.cn
'''

}


def hostWrite(testENV=''):
    '''用于切换测试环境，需提供要切换的环境名称，名称格式如：T11'''
    
    print 'Switch the environment...'

    h_file=open(r'C:\Windows\System32\drivers\etc\hosts','w') #打开host文件
    h_file.write(base_text)
    if testENV=='':
        print 'Initializing...'
        print 'Complete!!!'
        return True
        
    else:
        try:
            h_file.write(ht[testENV])#写入测试环境ip和域名
            print 'Switch To:',testENV
            #h_file.write()
            h_file.close()#关闭host文件
            
            print 'Complete!!!'
            print ht[testENV]
            return True

        except:
            print "The Environment does not exist, please confirm!!!"
            print " \n"
            print "Input again please!"
            return False
            
    
    

while True:
    testENV=raw_input('Select The Test Environment(T10\T11\T20\T21\T22\T30\T31\T32):')
    stat=hostWrite(testENV)
    
    if stat:break
    else:continue
    
#print ht
os.system("pause")
    
    

   
