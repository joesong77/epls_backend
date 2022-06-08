from flask import Blueprint
import pymysql
from config import mysql
from flask import jsonify
from flask import Blueprint
from flask import flash, request
from app import app


route_comment =Blueprint(("comment_page"), __name__)
@route_comment.route('/')
def comment():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT  * FROM  comment ")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@route_comment.route('/add', methods=['POST'])
def add():
    json = request.json
    name = json['name']
    text =json['text']
    rating=json['rating']
    class_id =json['class_id']
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("INSERT INTO comment(name,text,rating,class_id) VALUES(%s, %s,%s,%s)",(name,text,rating,class_id))
    conn.commit()
    respone = jsonify({"message":"新增成功"})
    respone.status_code = 200
    return respone





