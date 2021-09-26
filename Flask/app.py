#!/usr/bin/env python

# Headers
import os
import re

from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask_mysqldb import MySQL
from flask import render_template

# Setting App
app = Flask(__name__)

# Configuring database App
app.config['MYSQL_HOST'] = 'hostname'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'databasename'
mysql = MySQL(app)


# Creating API
# Home Page
@app.route('/',methods=['POST','GET'])
def index():
	# Lists
	data = []
	db_connection_req = mysql.connection.cursor()
	db_connection_req.execute('select * from places')
	db_connection_req = db_connection_req.fetchall()
	for info in db_connection_req:
		data.append({'id':info[0],'place':info[1],'city':info[2],'country':info[3]})
	return render_template('index.html',data = data)

# Delete Page
@app.route('/delete',methods=['POST'])
def delete():
	if request.method == 'POST':
		info = request.form.get('title')
		print(info)
		db_connection_delreq = mysql.connection.cursor()
		db_connection_delreq.execute('delete from places where pid='+str(info))
		mysql.connection.commit()
		return redirect(url_for('index'))

# Update Page 2
@app.route('/update2',methods=['POST'])
def update2():
	if request.method == 'POST':
		pidi = request.form.get('pid')
		pinfo = request.form.get('place')
		cinfo = request.form.get('city')
		ctinfo = request.form.get('country')
		db_connection_upreq = mysql.connection.cursor()
		db_connection_upreq.execute('update places set place=%s,city=%s,country=%s where pid=%s',(pinfo,cinfo,ctinfo,pidi))
		mysql.connection.commit()
		return redirect(url_for('index'))

# Update Page
@app.route('/update',methods=['POST'])
def update():
	if request.method == 'POST':
		info = request.form.get('title')
		db_connection_upreq = mysql.connection.cursor()
		db_connection_upreq.execute('select * from places where pid='+str(info))
		data = db_connection_upreq.fetchone()
		return render_template('update.html',pidi=data)

# Main Function
if __name__ == '__main__':
	app.run()
