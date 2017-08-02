#coding:utf-8
import os

       
mystr='username=admin&email=2916639@qq.com&passwd=123456&phone=18810919149'

new=mystr.split('&')

print new

msg=''
newmsg=[]
for msg in new:
	print msg
	msg=msg.split('=')[1]
	newmsg.append(msg)

print newmsg

