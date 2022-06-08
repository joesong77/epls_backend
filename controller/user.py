from flask import Blueprint
import pymysql
from config import mysql
from flask import jsonify
from flask import Blueprint
from flask import flash, request
from app import app


route_user =Blueprint(("user_page"), __name__)


@route_user.route('/login', methods=['POST'])
def login():
        _json = request.json
        _email = _json['email']
        _password = _json['password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from users where email=%s",_email)
        user = cursor.fetchone()
        if user == None:
            return jsonify({"message":"沒有這個帳號"})
        if user !=0:
            if _password == user['password']:
               respone = jsonify({"id":user['id'],"name":user['name'],"message":"登錄成功"})
               return respone
            else:
                 return jsonify({"message":"密碼錯誤"})

         