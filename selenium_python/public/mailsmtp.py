#_*_ coding:utf-8 _*_
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import getconfig
#读取配置文件信息
configname="mailconfig.txt"
info = getconfig.getconfig(configname)
#print info

#发送邮箱
sender     =   info["sender"]

#接收邮箱
receiver   =   info["receiver"]

#发送邮件的主题
subject    =   info["subject"]

#发送邮件的服务器
smtpserver =   info["smtpserver"]

#发送邮箱用户和密码
username   =   info["username"]
password   =   info["password"]


#设置邮件内容，中文需参数utf-8 ，单字节不需要
msg = MIMEText(u"您好！","plain","utf-8")
msg["Subject"] = Header(subject,"utf-8")

msg["from"] = sender
msg["to"] = receiver


smtp =smtplib.SMTP(smtpserver,25)
smtp.set_debuglevel(1)
#smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
print u"已成功发送邮件!!!"
smtp.quit()

