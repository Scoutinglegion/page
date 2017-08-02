#!/usr/bin/env python
#coding:utf-8

__author__ = 'pushiqiang'
from flask import Flask, request
#from . import app

import  util
import json,time,traceback,hashlib
import MySQLdb as mysql
import json
from flask import Flask,request,render_template
from flask import Flask, request, url_for, redirect
import requests
from flask import send_file

db = mysql.connect(user='root',passwd='',host='127.0.0.1',db='network',charset='utf8')
db.autocommit(True)
c = db.cursor()

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def hello():
	if request.method == 'POST':
		data = request.json
		print "This is my message"
		print data
#		return redirect(url_for('send'))
		return redirect('http://121.201.29.78:81/newpage/monitor.html')
#	return send_file("http://121.201.29.78:81/newpage/log.html",None,None,None)
#	return render_template('login.html',data=json.dumps(ones))
	return render_template('login.html')

@app.route('/send')
def send():
	return send_file("/var/www/html/newpage/log.html",None,None,None)

@app.route('/url',methods=['GET','POST'])
def myurl():
	if request.method == 'POST':
		newdata = request.json
		print newdata
		mydata = request.get_data()
		print mydata
		print str(mydata)
	return render_template('mon.html')

@app.route('/log',methods=['GET','POST'])
def log():
	return '''
			<html>
			<body>
<h1 style="color:white;">日志</h1>
<p  style="color:white;font-size:16px;"> 1 | 02/16/2017 | 00:04:33 | Power Supply #0xc9 | Failure detected () | Asserted</p>
<p></p>
	<p  style="color:white;font-size:16px;"> 1 | 02/16/2017 | 00:04:33 | Power Supply #0xc9 | Failure detected () | Asserted</p>
			</body>
			</html>
		'''

@app.route('/picture',methods=['GET'])
def picture():
	return render_template('picture.html')

@app.route('/new',methods=['GET'])
def mynew():
	top=['12.2.1.1','44.2.12.4']
	print top
	return json.dumps(top)

@app.route('/monitor',methods=['GET','POST'])
def monitor():
	sql=''
	if request.method == 'POST':
		data = request.json
		try:
			sql="insert into stat(host,mem_free,mem_usage,mem_total,load_avg,time) values ('%s',%d,%d,%d,'%s',%d)" % (data['Host'],data['MemFree'],data['MemUsage'],data['MemTotal'],data['LoadAvg'],int(data['Time']))
			ret = c.execute(sql)
		except mysql.IntegrityError:
			pass
		return 'OK'
	else:
		c.execute('select time,mem_usage from stat')
		ones = [[i[0]*1000,i[1]] for i in c.fetchall()]
		print ones
		return render_template('topic.html',data=json.dumps(ones))

@app.route('/updata',methods=['GET'])
def getnew():
	c.execute('select time,mem_total from stat order by id desc limit 1')
	v = c.fetchone()
	top = [v[0]*1000,v[1]]
	print top
	return json.dumps(top)

#@app.route('/passage',methods=[])

@app.route('/idc', methods=['GET', 'POST'])
def newlogin():
	if request.method == 'POST':
		data = request.json
		print "This is my message"
		mydata = request.get_data()
		print mydata
		new=list(mydata.split('&'))
		msg=''
		newmsg=[]
		for msg in new:
			print msg
			msg=msg.split('=')[1]
			newmsg.append(msg)
			print newmsg
			try:
				sql = "insert into message(username,email,passwd,phone) values ('%s','%s','%s','%s')" % (str(newmsg[0]),newmsg[1],newmsg[2],newmsg[3])
				ret = c.execute(sql)
			except mysql.IntegrityError:
				pass
		return redirect(url_for('send'))
	return render_template('IDC.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
#		session['username'] = request.form['username']
		return redirect(url_for('send'))
	return render_template('login.html')
app.run(host='0.0.0.0',port=8890,debug=True)


