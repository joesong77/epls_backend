from flask import Blueprint
import pymysql
from config import mysql
from flask import jsonify
from flask import Blueprint
from flask import flash, request
from app import app
from flask_bcrypt import Bcrypt
route_personnel =Blueprint(("personnel_page"), __name__)

@route_personnel.route('/<int:page_id>')
def personnel(page_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from user where r_id=%s",page_id)
        empRows = cursor.fetchall()

        respone = jsonify(empRows)
        respone.status_code = 200
        return respone 

    except Exception as e:
        print(e)
    finally:
        cursor.close()
