#!/usr/bin/env python
#coding:utf-8
__author__ = 'pushiqiang'
from flask import Flask, request
#from . import app

import json,time,traceback,hashlib
import MySQLdb as mysql
import json
from flask import Flask,request,render_template
from flask import Flask, request, url_for, redirect
import requests
from flask import send_file

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def hello():
	if request.method == 'POST':
		data = request.json
		print "This is my message"
		print data
		return redirect(url_for('/send'))
#	return render_template('login.html',data=json.dumps(ones))
	return render_template('disk.html')

@app.route('/send')
def send():
     return send_file("/var/www/html/newpage/pic.html",None,None,None)

@app.route('/new',methods=['GET'])
def getnew():
    top=[122,43,'21.2.2.2']
    print top
    return json.dumps(top)

@app.route('/url',methods=['GET','POST'])
def myhello():
    if request.method == 'POST':
        newdata = request.json 
		print newdata
	mydata = request.get_data()
	print mydata
	print str(mydata)
        return 'OK'

@qpp.route('/file',methods=['GET','POST'])
def file():
    return send_file("/var/www/html/newpage/file.html",None,None,None)	

@app.route('/mylogin', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		print "message"	
 		mydata = request.get_data()
  		print mydata
   		print str(mydata)

		return redirect(url_for('newsend'))
	return render_template('login.html', error=error)
#	return json.dumps({'code': 0, 'errmsg': "登录失败"})

@app.route('/login', methods=['GET', 'POST'])
def newlogin():
	if request.method == 'POST':
		mydata = request.get_data()
		print mydata
		print str(mydata)
		return redirect(url_for('send'))
	return render_template('login.html')


app.run(host='0.0.0.0',port=8890,debug=True)


