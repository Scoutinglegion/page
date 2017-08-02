__author__ = 'pushiqiang'
import MySQLdb as mysql
import json
from flask import Flask,request,render_template

app = Flask(__name__)

db = mysql.connect(user='root',passwd='',host='127.0.0.1',db='falcon',charset='utf8')
db.autocommit(True)
c = db.cursor()


@app.route('/monitor',methods=['GET','POST'])
def hello():
    sql = ''
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
        return render_template('mon.html',data=json.dumps(ones))

@app.route('/updata',methods=['GET'])
def getnew():
    c.execute('select time,mem_total from stat order by id desc limit 1')
    v = c.fetchone()
    top = [v[0]*1000,v[1]]
    print top
#        [1500398347000, 992]
    return json.dumps(top)


if __name__=='__main__':

	app.run(host='0.0.0.0',port=8888,debug=True)


