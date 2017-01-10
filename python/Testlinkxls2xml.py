#!/usr/bin/env python
# _ * _ coding:utf-8 _ * _
__author__ = 'Jormon'

import xlrd
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

    def readxls(self):
        """读取excel中用例"""
        global error_info

        #判断用例模板是否正确
        error_temp=self.xls_template_check()
        if error_temp==[]:
            pass
        else:
            error_info=error_temp
            return None

        #Excel列数、行数
        col=self.cols
        row=self.rows
        i=0
        testcase=[]#用于存放转化好的测试用例
        while i < row-1:

            data1=data2=data3={}
            tem_data1=tem_data2=tem_data3=""

            i+=1
            caseid=[]

            #读取用例ID并将用例ID放入到一个列表中
            cid=self.table.cell_value(i,0)
            caseid.append(cid)


            #读取关键字
            data1["keyword"]=self.keyword(i)

            #读取测试名称
            data1["testname"]==self.testName(i)

            #读取路径
            data1["path"]=self.path(i)

            #读取用例性质
            data1["propertys"]=self.propertys(i)

            #读取重要性
            data1["importance"]=self.importance(i)

            #读取测试概述
            data1["summary"]=self.summary(i)

            #读取前置条件
            data1["preconditions"]=self.preconditions(i)

            tem_data1=tem_head(data1)


            #读取编写人
            data3["writer"]=self.writer(i)

            #读取测试方式
            data3["testtype"]=self.testType(i)

            #读取状态
            data3["teststatus"]=self.testStatus(i)

            tem_data2=tem_other(data2)

            while True:
                #读取Excel中的步骤名称/测试步骤/期望结果/测试方式
                #读取 步骤名称
                data3["step_numbers"]=self.stepNum()

                #读取测试步骤
                data3["actions"]=self.testSteps(i)

                #读取期望结果
                data3["expectedresults"]=self.exceptResults(i)

                #读取测试方式
                data3["execution_type"]=self.testType(i)

                tem_data3+=tem_steps(data3)

                #判断是否有用例ID，有ID则读取测试用例信息，不存在表示当前行为上一行的一个步骤
                i+=1
                if self.table.cell_value(i,0)=="" and i < row :
                    continue
                else:
                    break
            #整合测试用用例
            tem_data=tem_data1+tem_data2+tem_data3
            #将测试用例存放到testcase=[{caseid:tem_data},{caseid:tem_data},{caseid:tem_data}]
            testcase.append(dict([caseid,tem_data]))

        return testcase





    def xls_template_check(self):
        '''检查Excel测试用例的模板是否正确'''

        xtemp=[u"用例编号",u"关键字",u"测试名称",u"路径",u"用例性质",u"重要性",u"测试概述",u"前置条件",u"步骤名称",u"测试步骤",u"预期结果",u"编写人",u"测试方式",u"状态"]
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


    ##################################################################################################################
    ###读取Excel测试用例的各个字段####################################################################################
    ###################################################################################################################
    def caseID(self,i):
        '''用例编号'''
        global error_info
        case_id=self.table.cell_value(i,0)
        if cid=="":
            error_info.append("第"+str(i+1)+"行【用例编号】未填写\n")
        return case_id.encode("utf-8")

    def keyword(self,i):
        '''关键字'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        keywd = self.table.cell_value(i,1)
        if keywd=="":
            error_info.append("第"+str(i+1)+"行【关键字】未填写\n")
        return keywd.encode("utf-8")

    def testName(self,i):
        '''测试名称'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        tname=self.table.cell_value(i,2)
        if tname=="":
            error_info.append("第"+str(i+1)+"行【测试名称】未填写\n")
        return tname.encode("utf-8")

    def path(self,i):
        '''路径'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        path=self.table.cell_value(i,3)
        if path=="":
            error_info.append("第"+str(i+1)+"行【路径】未填写\n")
        return path

    def propertys(self,i):
        '''用例性质'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        pro=self.table.cell_value(i,4)
        if pro=="":
            error_info.append("第"+str(i+1)+"行【用例性质】未填写\n")
        return pro.encode("utf-8")

    def importance(self,i):
        ''' 重要性'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        imp = self.table.cell_value(i,5)

        dimp = {u'最高':4,u'高':3,u'中':2,u'低':1}

        if imp in dimp:
            importance=dimp[imp]
        else:
            error_info.append("第"+str(i+1)+"行【重要性】填写有误或未填写！\n")
            importance=None

        return importance


    def summary(self,i):
        ''' 测试概述'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        sumy = self.table.cell_value(i,6)
        if sumy=="":
            error_info.append("第"+str(i+1)+"行【测试概述】未填写\n")
        return sumy.encode("utf-8")


    def preconditions(self,i):
        '''前置条件'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        pp=self.table.cell_value(i,7)
        if pp=="":
            error_info.append("第"+str(i+1)+"行【前置条件】未填写\n")
        p=pp.splitlines()
        pre=u'<br/>'.join(p)
        return pre.encode("utf-8")

    def stepNum(self,i):
        ''' 步骤名称'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        num = self.table.cell_value(i,8)
        if num=="":
            error_info.append("第"+str(i+1)+"行【步骤名称】未填写\n")
        return num.encode("utf-8")

    def testSteps(self,i):
        ''' 测试步骤 '''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        sp = self.table.cell_value(i,9)
        if sp=="":
            error_info.append("第"+str(i+1)+"行【测试步骤】未填写\n")

        s=sp.splitlines()
        step=u'<br/>'.join(s) #添加换行


        return step.encode("utf-8")

    def exceptesults(self,i):
        ''' 期望结果'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        ex=self.table.cell_value(i,10)
        if ex=="":
            error_info.append("第"+str(i+1)+"行【期望结果】未填写\n")

        e=ex.splitlines()
        exre=u'<br/>'.join(e)
        return exre.encode("utf-8")

    def writer(self,i):
        '''编写人'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        wri = self.table.cell_value(i,11)
        if wri=="":
            error_info.append("第"+str(i+1)+"行【编写人】未填写\n")

        return wri.encode("utf-8")

    def testType(self,i):
        ''' 测试方式'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        ttype = self.table.cell_value(i,12)
        return ttype.encode("utf-8")

    def testStatus(self,i):
        ''' 状态'''
        global error_info
        case_id=self.table.cell_value(i,0)#用例ID

        ts=self.table.cell_value(i,13)
        return ts.encode("utf-8")

    ###################################################################################################################
    #####Xml用例的格式模板#############################################################################################
    ###################################################################################################################
    def tem_head(self,data):
        template1="""
     <testcase name="%(testname)s">\r
       <keywords>\r
            <keyword name="%(keyword)s" />\r
       </keywords>\r
       <importance><![CDATA[%(importance)s]]></importance>\r
       <summary><![CDATA[%(summary)s]]></summary>\r
       <preconditions><![CDATA[%(preconditions)s]]></preconditions>\r
       """
        return template%data

    def tem_step(self,data):
        template="""
        <steps>\r
         <step>\r
                  <step_number><![CDATA[%(step_number)s]]></step_number>\r
                  <actions><![CDATA[%(actions)s]]></actions>\r
                  <expectedresults><![CDATA[%(expectedresults)s]]></expectedresults>\r
                 <execution_type><![CDATA[1]]></execution_type>\r
         </step>\r
       </steps>\r
       """
        return template % data

    def tem_other(self):
        template="""
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
       </custom_fields>\r
     </testcase>\r
     """

        return template % data

path=u"C:\Users\jormo\Desktop\CP.xls"
xls=Xls2xml(path)
xls.readxls()

######################################################################################################################
#####图形界面 ########################################################################################################
######################################################################################################################


class Tk_TestlinkConvert(object):
    def __init__(self):
        self.filename="" #存放选择文件的路径

        self.root = Tk()
        self.root.title("TestlinkConvert_V20161231")
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


