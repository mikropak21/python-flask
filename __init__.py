from flask import Flask, jsonify, render_template, send_from_directory, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import MySQLdb
import os
import json
import time
import datetime
import requests
from time import gmtime, strftime

app = Flask(__name__, static_url_path='')
mysql = MySQL(app)

# MySQL configurations
app.config.from_pyfile('app.cfg')

@app.route('/')
@app.route('/home')
def dashboard():
    return "hello"

@app.route('/api/get-id')
def getId():
    cur = mysql.connection.cursor()
    query = "select * from data_desa"
    cur.execute(query)
    data = cur.fetchall()
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=False, host=app.config["HOST"])
