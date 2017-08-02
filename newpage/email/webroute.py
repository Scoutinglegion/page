__author__ = 'pushiqiang'
import MySQLdb as mysql
import json
from flask import Flask,request,render_template
import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        data = request.json
	print data
        return 'OK'
    else:
	ones =[11,22]
        print ones
        return render_template('mon.html',data=json.dumps(ones))

@app.route('/new',methods=['GET'])
def getnew():
	top=['122','43','21.2.2.2','12.31.2.1']
#	nodes=[
#	top=[{id:'10.4.42.1',type:'router',status:1},{id:'10.4.43.1',type:'switch',status:1,expand:true},{id:'10.4.44.1',type:'switch',status:1},{id:'10.4.45.1',type:'switch',status:0}];
	print top
#        [1500398347000, 992]
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

app.run(host='0.0.0.0',port=8889,debug=True)



