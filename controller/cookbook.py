from flask import Blueprint
import pymysql
from config import mysql
from flask import jsonify
from flask import Blueprint
from flask import flash, request
from app import app
from flask_bcrypt import Bcrypt
route_cookbook =Blueprint(("cookbook_page"), __name__)

@route_cookbook.route('/')
def cookbook():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from cookbook")
        empRows = cursor.fetchall()

        respone = jsonify(empRows)
        respone.status_code = 200
        return respone 

    except Exception as e:
        print(e)
    finally:
        cursor.close()


@route_cookbook.route('/<int:page_id>')
def page(page_id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT m.id ,m.name ,m.img  FROM meal as m LEFT JOIN cookbook ON m.c_id=cookbook.id  AND cookbook.id = %s ",page_id)
    user = cursor.fetchall()
    respone = jsonify(user)
    respone.status_code = 200
    return respone

