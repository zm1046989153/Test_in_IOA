# _ * _ coding:UTF-8 _ * _

from Tkinter import *
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



        
class Tk_changeENV(object):
    
    def __init__(self):
        self.filename="" #存放选择文件的路径
        
        self.root = Tk()
        self.root.title("ChangeENV_V20170112")
        self.root.geometry()
        self.root.resizable(width=False, height=False)#设置窗体不可改变
        #self.mainloop=self.root.mainloop()
        self.path=r'C:\Windows\System32\drivers\etc\hosts' #host文件存放路径
        #self.path=r"D:\hosts"
        
        frm=Frame(self.root)
        Label(frm,text=self.path,height=1,font=("Arial",10)).pack(fill=X,expand=1)
        
        #显示当前host文件的信息
        self.tx=Text(frm,fg="blue",font=("Arial",10))
        
        scrl =Scrollbar(frm)
        scrl.pack(side=RIGHT,fill=Y)
        self.tx.configure(yscrollcommand = scrl.set)
        self.tx.pack(fill=BOTH,expand=1)
        scrl["command"]=self.tx.yview
        
        #Text输出提示信息
        '''
        self.tx0=Text(frm,fg="red",font=("Arial",12),width=3,height=1)
        self.tx0.pack(fill=X,expand=1)'''

        #Label输出提示信息
        self.var = StringVar()
        label =Label(frm,textvariable=self.var,fg="red",font=("Arial",12),width=3,height=1)
        label.pack(fill=X,expand=1)
        
        
        frm.pack()
        #读取当前host信息并显示
        self.hostRead()
        #提示信息窗口
        

        #读要切换的环境的host信息
        
        frmb=Frame(self.root)
        Button(frmb,text=u"格式化",command=lambda:self.switch_env(env="T"),bg="red").pack(side=RIGHT,fill=X,expand=1)
        Button(frmb,text="Current",command=self.hostRead,bg="green").pack(side=RIGHT,fill=X,expand=1)
        Button(frmb,text="T20",command=lambda:self.switch_env(env="T20")).pack(side=RIGHT,fill=X,expand=1)
        Button(frmb,text="T21",command=lambda:self.switch_env(env="T21")).pack(side=RIGHT,fill=X,expand=1)
        Button(frmb,text="T22",command=lambda:self.switch_env(env="T22")).pack(side=RIGHT,fill=X,expand=1)
        Button(frmb,text="T30",command=lambda:self.switch_env(env="T30")).pack(side=RIGHT,fill=X,expand=1)
        Button(frmb,text="T31",command=lambda:self.switch_env(env="T31")).pack(side=RIGHT,fill=X,expand=1)
        Button(frmb,text="T32",command=lambda:self.switch_env(env="T32")).pack(side=RIGHT,fill=X,expand=1)
       
        frmb.pack(fill=X,expand=1)
        
        Button(self.root,text=u">>>切换>>>",command=self.hostWrite,height=3,bg="blue",font=("Arial",10)).pack(fill=X,expand=1)

        
        
        '''
        
        #切换并显示要切换环境的信息
        frm0=Frame(self.root)
        Label(frm0,height=2,font=("Arial",10)).pack(fill=X,expand=1)
        frm1=Frame(frm0)
        Entry(frm1,font=("Arial",10)).pack(fill=Y,expand=1)
        Button(frm1,text=u"切换>>>",command=self.hostWrite,height=3,font=("Arial",10)).pack(fill=X,expand=1)
        frm1.pack(side=LEFT,fill=Y,expand=1)
       
        self.tx0=Text(frm0,fg="red",font=("Arial",10))
        scr0 =Scrollbar(frm0)
        scr0.pack(side=RIGHT,fill=Y)
        self.tx0.configure(yscrollcommand = scr0.set)
        self.tx0.pack(side=LEFT,fill=BOTH,expand=1)
        scr0["command"]=self.tx0.yview
        frm0.pack(side=RIGHT)'''


    def switch_env(self,env):
        #显示选择的要切换的环境

        #清空文本框显示内容
        self.tx.delete(1.0,END)
        
        #写入信息
        self.tx.insert(END,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        self.tx.insert(END,">>>>>>>>>>>>>>>>>>>>>>>>>>Switch to the Environment>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        self.tx.insert(END,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        if env=="T":
            self.tx.insert(END,"\n")
            self.tx.insert(END,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
            self.tx.insert(END,u">>>>>>>>>>>>>>>>>>>初始化host文件，切换至现网环境>>>>>>>>>>>>>\n")
            self.tx.insert(END,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        else:
            try:
                self.tx.insert(END,ht[env])
            except KeyError:
                self.tip(u"切换的环境不存在!")
                
        
         

    def hostWrite(self):
        '''写入host'''
    
        #读取Text中的host信息
        host_text=self.tx.get(1.0,END)
        
        if "Current Test Environment" in host_text:
            self.tip(u"请选择要切换的环境!")
        else:
            list_text=host_text.splitlines()
        
            try:
                with open(self.path,'w') as h_file: #打开host文件
                    h_file.write(base_text)
                    for t in list_text:
                        if ">>" in t:
                            continue
                        else:
                            h_file.write("\n")
                            h_file.write(t)
                self.tip(u"切换完成!!!")
            
            except UnicodeEncodeError:
                self.tip(u"请勿使用中文字符!!!")
      
        #self.hostRead()#重新读取host文件信息
        
        
               
    def hostRead(self):
        
        '''读取host文件中的信息'''
        self.tx.delete(1.0,END)#清空text中显示的内容
        
        try:
            with open(self.path,'r') as h_file:
                host_info=h_file.readlines()
        
            self.tx.insert(END,"***************************************************************************************************\n")
            self.tx.insert(END,"*********************************Current Test Environment****************************************\n")
            self.tx.insert(END,"***************************************************************************************************\n")
            for i in host_info:
                if '#' in i:
                    continue
                else:
                    self.tx.insert(END,i)
                    self.tx.insert(END,"\n")
        except:
            
            error_info=u"host文件不存在，请确认host文件所在路径"


    def tip(self,msg):
        
        #使用Label输入提示信息
        self.var.set(msg)
        '''
        
        self.tx0.delete(1.0,END)
        #文本框中提示
        self.tx0.insert(END,u"提示:")
        self.tx0.insert(END,msg)'''
        
        #使用提示框提示
        '''
        tk=Tk()
        tk.title(u"提示信息")
        tk.geometry("200x130")
        tk.resizable(width=False, height=False)#设置窗体不可改变
        Label(tk,text=msg).pack(fill=X,expand=1)

        Button(tk,text=u"确定",command=tk.destroy).pack()#点击确定关闭提示窗口

        Label(tk).pack()
        
        tk.mainloop()'''





        
def main():
    tk=Tk_changeENV()
    mainloop()

if __name__=="__main__":
    main()

   
