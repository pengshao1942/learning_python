#!/usr/bin/env python
#coding:utf8
import os
import time
import smtplib
from email.mime.text import MIMEText
from email import Utils
import socket
 
def sendmail(to,subject,content):
    msg = MIMEText(content)
    lable_pwd="cmstop666"
    msg['from'] = 'cmstop666@163.com'
    msg['to'] = to
    msg['subject'] = subject
    msg['date'] = Utils.formatdate(localtime=1)
    msg['message-id'] = Utils.make_msgid()
 
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect("smtp.sina.com:25")
        try:
            smtpObj.login("smtp.163.com",lable_pwd)
            me = "cmstop666@163.com"
            smtpObj.sendmail(me,to,msg.as_string())
            print ("Congratulations !Your mail have been sended Success !")
        except smtplib.SMTPAuthenticationError.smtplib.SMTPException:
            print ("Login failed ,Please check the username/password.")
        finally:
            try:
                smtpObj.close()
            except smtplib.SMTPException:
                pass
    except smtplib.SMTPException.e:
        print ("Error: unable to send email %s" % e)
 
def check_server(f):
    try:
        fo = open(f)
 
        for line in fo:
            now = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            line = line.rstrip('\n')
            print ('正在检测%s的80端口是否正常 %s:......' % (line,now))
            try:
                s.connect((line,80))
                print ("地址%s检测正常" % line)
            except socket.error.e:
                print ("地址%s检测挂啦" % line)
                sc = 'The web server %s is down '% line
                cc = 'The web server %s is down at %s' % (line,now)
                sendmail('shaopeng@cmstop.com',sc,cc)
            finally:
                s.close()
    except IOError.e:
        print ("error: %s" % e)
    finally:
        try:
            fo.close()
        except IOError.e:
            print ("error : %s" % e)
 
if __name__=='__main__':
    check_server('D:/workspace/studd/company_list')
