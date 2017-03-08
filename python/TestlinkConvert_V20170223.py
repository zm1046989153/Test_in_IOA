#_*_ coding:utf-8 _*_
import xlrd
import time
import sys,os
import win32ui
from Tkinter import *
'''
reload(sys)
sys.setdefaultencoding('utf-8')'''

error_info=[]

class Xls2xml(object):
    def __init__(self,path):
        try:
            data=xlrd.open_workbook(path,formatting_info = True, encoding_override="utf-8")
        except IOError:
            print u"选择的文件格式有误，请选择xls文件"
            os._exit(0)#终止程序执行
               
        self.table=data.sheets()[0]
        
        self.cols=self.table.ncols #读取列数
        self.rows=self.table.nrows #读取行数

        #用字典cols_dict将列数和对应读取函数关联
        self.cols_dict={'caseid':self.caseID,'keyword':self.keyword,'testname':self.testName,'path':self.path,'propertys':self.propertys,'importance':self.importance,'summary':self.summary,
                   'preconditions':self.preconditions,'stepnum':self.stepNum,'teststeps':self.teststeps,'exceptresults':self.exceptresults,'writer':self.writer,'testtype':self.testType,'teststatus':self.testStatus,'steps':self.steps,'phonetype':self.phonetype}

    def xls_template_check(self):
        '''检查Excel测试用例的模板是否正确'''

        xtemp=[u"用例编号",u"关键字",u"测试名称",u"路径",u"用例性质",u"重要性",u"测试概述",u"前置条件",u"步骤名称",u"测试步骤",u"预期结果",u"编写人",u"测试方式",u"状态",u"手机类型"]
        error_temp=[]
        try:
            for i in range(14):
                if self.table.cell_value(0,i)==xtemp[i]:
                    pass
                else:
                    error_temp.append(u"第"+str(i+1)+u"列"+u"应为【"+xtemp[i]+u"】\n")
                    
        except IndexError:
            error_temp.append(u"Excel用例模板应为14列，请确认!!!")

        return error_temp
            
        
        

    def caseID(self,i):
        '''用例编号'''
        global error_info
        cid=self.table.cell_value(i,0)
        if cid=="":
            error_info.append("第"+str(i+1)+"行【用例编号】未填写\n")
        return 'caseID',cid.encode("utf-8")

    def keyword(self,i):
        '''关键字'''
        global error_info
        keywd = self.table.cell_value(i,1)
        if keywd=="":
            error_info.append("第"+str(i+1)+"行【关键字】未填写\n")
        return 'keyword',keywd.encode("utf-8")

    def testName(self,i):
        '''测试名称'''
        global error_info
        tname=self.table.cell_value(i,2)
        if tname=="":
            error_info.append("第"+str(i+1)+"行【测试名称】未填写\n")
        return 'testname',tname.encode("utf-8")

    def path(self,i):
        '''路径'''
        global error_info
        path=self.table.cell_value(i,3)
        if path=="":
            error_info.append("第"+str(i+1)+"行【路径】未填写\n")
        return 'path',path

    def propertys(self,i):
        '''用例性质'''
        global error_info
        pro=self.table.cell_value(i,4)
        if pro=="":
            error_info.append("第"+str(i+1)+"行【用例性质】未填写\n")
        return 'property',pro.encode("utf-8")

    def importance(self,i):
        ''' 重要性质'''
        global error_info

        imp = self.table.cell_value(i,5)
        
        dimp = {u'最高':4,u'高':3,u'中':2,u'低':1}
        
        if imp in dimp:
            importance=dimp[imp]
        else:
            error_info.append("第"+str(i+1)+"行【重要性】填写有误或未填写！\n")
            importance=None

        return 'importance',importance


    def summary(self,i):
        ''' 测试概述'''
        global error_info
        sumy = self.table.cell_value(i,6)
        if sumy=="":
            error_info.append("第"+str(i+1)+"行【测试概述】未填写\n")
        return 'summary',sumy.encode("utf-8")

    def preconditions(self,i):
        '''前置条件'''
        global error_info
        pp=self.table.cell_value(i,7)
        if pp=="":
            error_info.append("第"+str(i+1)+"行【前置条件】未填写\n")
        p=pp.splitlines()
        pre=u'<br/>'.join(p)
        return 'preconditions',pre.encode("utf-8")

    def stepNum(self,i):
        ''' 步骤名称'''
        global error_info
        num = self.table.cell_value(i,8)
        if num=="":
            error_info.append("第"+str(i+1)+"行【步骤名称】未填写\n")
        return 'step_number',num.encode("utf-8")
    def teststeps(self,i):
        ''' 测试步骤 '''
        global error_info
        sp = self.table.cell_value(i,9)
        if sp=="":
            error_info.append("第"+str(i+1)+"行【测试步骤】未填写\n")
            
        s=sp.splitlines()
        step=u'<br/>'.join(s) #添加换行

            #else:print u"测试步骤过多!!!"

        return 'actions',step.encode("utf-8")

    def exceptresults(self,i):
        ''' 期望结果'''
        global error_info
        ex=self.table.cell_value(i,10)
        if ex=="":
            error_info.append("第"+str(i+1)+"行【期望结果】未填写\n")
        
        e=ex.splitlines()
        exre=u'<br/>'.join(e)
        return 'expectedresults',exre.encode("utf-8")

    def writer(self,i):
        '''编写人'''
        global error_info
        wri = self.table.cell_value(i,11)
        if wri=="":
            error_info.append("第"+str(i+1)+"行【编写人】未填写\n")
            
        return 'writer',wri.encode("utf-8")

    def testType(self,i):
        ''' 测试方式'''
        global error_info
        ttype = self.table.cell_value(i,12)
        return 'testType',ttype.encode("utf-8")

    def testStatus(self,i):
        ''' 状态'''
        global error_info
        ts=self.table.cell_value(i,13)
        return 'testStatus',ts.encode("utf-8")

    def phonetype(self,i):
        '''手机类型'''
        global error_info
        pt=self.table.cell_value(i,14)
        #print pt
        if pt in [u"安卓",u"IOS",u"公用"]:
            return 'phonetype',pt.encode("utf-8")
        elif  pt=="":
            return "phonetype",u"公用".encode("utf-8")
        else:
            error_info.append("第"+str(i+1)+"行【手机类型】填写有误!!!"+"只能填写：安卓、IOS、公用\n")
            return "phonetype",u"公用".encode("utf-8")

    def steps(self,i):
        '''将步骤名称/步骤/期望结果/执行方式一起存放'''
        steps=[]
        j=i
        #step=step+self.table.cell_value(i+1,9)
        steps=[dict(self.stepNum(j)),dict(self.teststeps(j)),dict(self.exceptresults(j)),dict(self.testType(j))]
        while j<self.rows:
            j+=1
            if  not self.table.cell_value(j,0):
                steps.append([dict(self.stepNum(j)),dict(self.teststeps(j)),dict(self.exceptresults(j)),dict(self.testType(j))])
                continue
            else:
                break
        #以字典形式存放到列表中
        return steps

    def excel_read(self):
        
        "读取excel中用例"
        global error_info
        
        #判断用例模板是否正确
        error_temp=self.xls_template_check()
        if error_temp==[]:
            pass
        else:
            error_info=error_temp
            
            return None
            
        
        cols=self.cols #读取列数
        rows=self.rows #读取行数
        cols_dict=self.cols_dict #读取用例
        test_case=[]#用于存储读取到的用例
        steps=[]#用于存储步骤
        #print rows
        #rows=220
        i=0
        while i < rows-1:
            case=[]
            i+=1
            #通过Case ID判断当前行是否为一条测试用例，若ID不存在则当前行为用例的一个步骤
            #if not cols_dict['caseid'](i)[1]:
                #print i
             #   continue
            #else:pass
            #定义要读取的信息
            read_cols=['caseid','keyword','path','testname','propertys','importance','summary','preconditions','writer','teststatus','stepnum','teststeps','exceptresults','testtype','phonetype']
            for fuc in read_cols:#分别读取每条用例每一列的信息，通过字典col_dict读取
                case.append(cols_dict[fuc](i))
                #print cols_dict[fuc](i)
                #print i,fuc
                #case=[(字段名称，值),(字段名称，值),(字段名称，值)]
            #for tt in case:
            test_case.append(dict(case))#test_case=[{第一条用例case ID:XX,testname:XX,...},{第二条用例},{第三条用例}]
        #print k
        return test_case

def case_template(data):
    template="""
     <testcase name="%(testname)s">\r
       <keywords>\r
            <keyword name="%(keyword)s" />\r
       </keywords>\r
       <importance><![CDATA[%(importance)s]]></importance>\r
       <summary><![CDATA[%(summary)s]]></summary>\r
       <preconditions><![CDATA[%(preconditions)s]]></preconditions>\r
       <steps>\r
         <step>\r
                  <step_number><![CDATA[%(step_number)s]]></step_number>\r
                  <actions><![CDATA[%(actions)s]]></actions>\r
                  <expectedresults><![CDATA[%(expectedresults)s]]></expectedresults>\r
                 <execution_type><![CDATA[1]]></execution_type>\r
         </step>\r
       </steps>\r
       <status><![CDATA[1]]></status>\r
       <execution_type><![CDATA[1]]></execution_type>\r
       <custom_fields>\r
         <custom_field>\r
             <name><![CDATA[编写人]]></name>\r
             <value><![CDATA[%(writer)s]]></value>\r
         </custom_field>\r
         <custom_field>\r
             <name><![CDATA[用例性质]]></name>\r
             <value><![CDATA[%(property)s]]></value>\r
         </custom_field>\r
         <custom_field>
	    <name><![CDATA[手机类型]]></name>
	    <value><![CDATA[%(phonetype)s]]></value>
	</custom_field>
       </custom_fields>\r
     </testcase>\r
"""
    testcase=template % data #  将用例信息写到用例模板
    return testcase

def xml_write(case_info,path):
    '''将转化后的用例写进xml文件中case_info=[{},{},{}]'''
    if error_info==[]:
        pass
    else:
        #error_output()
        return False,path,None #有错误信息则返回打印错误信息
    xml_path=xlsToxmlPath(path)
    file=open(xml_path,'wb')
    file.write('<?xml version="1.0" encoding="utf-8"?>')
    testsuit='''
<testsuite name="%s">
  <node_order />
  <details />'''
    file.write(testsuit%'')
    casepath=[]#存放用例的路径
    casenum=len(case_info)
    for n in range(casenum):
        if case_info[n]['path'] in casepath:
            continue
        else:
            casepath.append(case_info[n]['path'])
    #casepath=list(set(casepath))#去除重复的路径

    dict_path={}
    #casepath.sort()#路径排序
    for k in casepath:
        dict_path[k]=[]

    for n in range(casenum):
        ph=case_info[n]['path']
        for k in casepath:
          if k==ph:
              dict_path[k].append(case_info[n])
              #print True
              break
          else:
              #print False
              continue
            
    k=0
    #开始将测试用例写入xml文件
    for j in casepath:
        #dict_path={key:[{test1},{test2}],key:[{test1},{test2}]}
        #casepath=[path1,path2,...]
        jts=j.split('/')
        #print jts
        for jt in jts:
            jt0=jt.encode("utf-8")
            #print testsuit%jt
            file.write(testsuit%jt0)#根据路径写入testsuit
            
        #print dict_path[j]
        tems=map(case_template,dict_path[j]) #将从excel获取的用例信息转为xml格式
        for tem in tems:#写入测试用例
            file.write(tem)
            k+=1#记录测试用例写入条数
            
        for jt in jts:
            file.write("\r\n</testsuite>\r\n")


    file.write(r"</testsuite>")
    print 'Total:'+str(k)
    file.close()
    return True,xml_path,k#返回True表示转化成功


class Tk_xls2xml():
    
    def __init__(self):
        self.filename="" #存放选择文件的路径
        
        self.root = Tk()
        self.root.title("TestlinkConvert_V20170223@By_Jormon")
        self.root.geometry("700x350")
        self.root.resizable(width=False, height=False)#设置窗体不可改变
        #self.mainloop=self.root.mainloop()
        
        frm=Frame(self.root)
        Button(frm,text=u"选择Excel文件",command=self.getPathFileName,height=5,width=38,bg="blue",font=("Arial",10)).pack(side=LEFT,fill=X,expand=1)
        Button(frm,text=u"选择Xml文件",command=self.xml_to_xls,height=5,width=38,font=("Arial",10)).pack(side=RIGHT,fill=X,expand=1)
        frm.pack(fill=BOTH,expand=1)
        
        Button(self.root,text=u"转换",command=self.xls_to_xml,width=10,height=5,font=("Arial",10)).pack(fill=X,expand=1)

        self.tx=Text(self.root,fg="red",font=("Arial",10))
        
        scrl =Scrollbar(self.root)
        scrl.pack(side=RIGHT,fill=Y)
        self.tx.configure(yscrollcommand = scrl.set)
        self.tx.pack(side=LEFT,fill=BOTH,expand=1)
        scrl["command"]=self.tx.yview

    def xml_to_xls(self):
        self.tx.insert(END,"暂无此功能!\n")
        

    def getPathFileName(self):
        '''选择Excel文件，并返回文件路径'''
        dlg = win32ui.CreateFileDialog(1) # 1 表示打开文件对话框
        #dlg.SetOFNInitialDir(r"D:/Python27") # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()

        self.filename = dlg.GetPathName()#获取选择的文件名称
        #self.tx(END,"已选择文件："+self.filename)

    def xls_to_xml(self):
        path=self.filename
        
        self.filename=""#清空之前选择的文件
        
        if path=="":
            self.tx.insert(END,"请选择Excel文件！\n")
            return False
        elif not path.split(".")[-1]=="xls":
            self.tx.insert(END,"文件格式有误，请选择xls文件!\n")
            return False
        
            
        x=Xls2xml(path)  
                
        testcase=x.excel_read() #读取excel中的用例信息
        
        #调用xml_write,返回是否转换成功，转换后的xml路径，转换的用例数
        is_error,xml_path,case_Num=xml_write(testcase,path)
        xml_path1=xml_path.decode('gbk').encode("utf-8")
        if is_error:
            case_Num_out=u"\n用例数："+str(case_Num)+"\n"
            self.tx.insert(END,"#############################\r\n\n")
            self.tx.insert(END,u"转换完成！\n")
            self.tx.insert(END,xml_path1)
            self.tx.insert(END,case_Num_out)
            self.tx.insert(END,"#############################\r\n\n")
        else:
            self.error_output() #打印错误信息
            #print 1
            
        
    def error_output(self):   
        '''打印错误信息'''
        global error_info
        
        infos=error_info
        error_info=[] #清空error_info
        print infos
        self.tx.insert(END,"\n错误信息：\n")
        for info in infos:
            self.tx.insert(END,info)
            
    
      
            

def error_output():     
    '''输入错误信息'''    
    tt=time.strftime("%Y%m%d%H%M%S",time.localtime())
    with open(u"C:\\Users\\jormo\\Desktop\\"+tt+".txt",'w') as f:
        for info in error_info:
            f.write(info)        
    os._exit(0)
    


def xlsToxmlPath(path):
    tt=time.strftime("%Y%m%d%H%M%S",time.localtime())
    path0=path.split('.')
    path0.pop()
    path1='.'.join(path0)
    
    return path1 + '_' + tt+'.xml'




def main():
    tk=Tk_xls2xml()
    mainloop()

if __name__=="__main__":
    main()

'''
path1="C:\Users\jormo\Desktop\CRM线索池.xls"
path=unicode(path1,"utf-8")
print path
x=Xls2xml(path)
testcase=x.excel_read() #读取excel中的用例信息
xml_write(testcase,path)

   ''' 


'''
case_data={
   'casename':'未购买CRM用户进入线索池',
   'keyword':"V1.0.0",
   'importance':"2",
   'summary':"验证：未购买CRM用户无法进入CRM相应功能模块，并提示用户购买",
   'preconditions':'用户未购',
   'step_number':'1',
   'actions':'1.用户登录用户中心，查看导航栏2.点击进入CRM',
   'expectedresults':'1.正常登陆用户中心，显示CRM应用',
   'writer':'陈振铭',
   'property':'正'
   }

#xml(case_template(case_data))
#print case_data
'''
