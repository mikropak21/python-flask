from flask import Flask, jsonify, render_template, send_from_directory, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import MySQLdb
import os
import json
import time
import datetime
import requests
import mysql.connector
from time import gmtime, strftime

app = Flask(__name__, static_url_path='')
mysql = MySQL(app)

# MySQL configurations
app.config.from_pyfile('app.cfg')

@app.route('/')
@app.route('/home')
def dashboard():
    return "Hello Sir"    

@app.route('/api/get-all', methods=["GET"])
def getAll():
    cur = mysql.connection.cursor()
    query = "select * from data_desa"
    cur.execute(query)
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/get-data/<string:nama_desa>,<string:lokasi_desa>, <int:id>', methods=["GET"])
def getData(nama_desa,lokasi_desa):
    cur = mysql.connection.cursor()
    query = "select * from data_desa where nama_desa = %s or lokasi_desa = %s or id = %s"
    cur.execute(query,(nama_desa,lokasi_desa,id,))
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/add-data', methods=["POST"])
def addData():
    nama_desa = request.form.get('nama_desa')
    lokasi_desa = request.form.get('lokasi_desa')
    id = request.form.get('id')
    mydb = mysql.connection
    cur = mydb.cursor()
    query = "INSERT INTO data_desa (nama_desa,lokasi_desa,id) VALUES (%s,%s,%s)"
    cur.execute(query,(nama_desa,lokasi_desa,id,))
    mydb.commit()
    if (mydb.commit==False):
        return "Data gagal dimasukan"
    else:
	return "Data berhasil dimasukan"

@app.route('/api/del-data/<string:nama_desa>', methods=["DELETE"])
def delData(nama_desa):
    mydb = mysql.connection
    cur = mydb.cursor()
    query = "DELETE FROM data_desa WHERE nama_desa = %s"
    sub = cur.execute(query,(nama_desa,))
    mydb.commit()
    if (sub==False):
        return "Data gagal dihapus"
    else:
	return "Data berhasil dihapus"

@app.route('/api/update/<int:id>', methods=["PUT"])
def updateData(id):
    mydb = mysql.connection
    cur = mydb.cursor()
    nama_desa = request.form.get('nama_desa')
    lokasi_desa = request.form.get('lokasi_desa')
    query = "UPDATE data_desa set nama_desa = %s, lokasi_desa = %s where id = %s"
    sub = cur.execute(query,(nama_desa,lokasi_desa,id,))
    mydb.commit()
    if (sub==False):
	return "Data gagal diupdate"
    else:
	return "Data berhasil diupdate"

if __name__ == '__main__':
    app.run(debug=False, host=app.config["HOST"])
