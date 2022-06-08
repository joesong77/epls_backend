from flask import Blueprint
import pymysql
from config import mysql
from flask import jsonify
from flask import Blueprint
from flask import flash, request
from app import app
import json

route_commentclass =Blueprint(("commentclass_page"), __name__)
@route_commentclass.route('/')
def commitClass():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT  *  from commentclass")

    empRows = cursor.fetchall()
    respone =jsonify(empRows)
    respone.status_code = 200
    return respone


@route_commentclass.route('/<int:page_id>')
def page(page_id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT  *  from commentclass  where class_id='%s'", page_id)
    cursor2 = conn.cursor(pymysql.cursors.DictCursor)
    cursor2.execute("SELECT  *  from comment where class_id='%s'", page_id)
    empRows = cursor.fetchone()
    empRows2 = cursor2.fetchall()
    respone = jsonify({"class_id":empRows['class_id'],"title":empRows['title'],"img":empRows['img'],"rating":empRows['rating'],"comment":empRows2})
    respone.status_code = 200
    return respone




