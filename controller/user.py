from flask import Blueprint
import pymysql
from config import mysql
from flask import jsonify
from flask import Blueprint
from flask import flash, request
from app import app
import jwt
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)
route_user =Blueprint(("user_page"), __name__)


app.config['SECRET_KEY']= '89g2rgrgrherh231dffggg'

@route_user.route("/")
def user():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT  * FROM  user where r_id = 1 ")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@route_user.route('/register', methods=['POST'])
def register():
 
    json = request.json
    user_id = json['user_id']
    username = json['username']
    password =json['password']
    hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
    email = json['email']
    r_id = json['r_id']
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("INSERT INTO user(user_id,username,password,email,r_id) VALUES(%s,%s,%s,%s,%s)",(user_id,username,hash_password,email,r_id))
    conn.commit()
    respone = jsonify({"message":"新增成功"})
    respone.status_code = 200
    return respone


@route_user.route('/managerLogin', methods=['POST'])
def login():
        json = request.json
        user_id= json['user_id']
        password = json['password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from user where user_id=%s and r_id = 1",user_id)
        user = cursor.fetchone()
        if user == None:
            return jsonify({"message":"帳號或密碼錯誤"})
        if user !=0:
            check_password = bcrypt.check_password_hash(user["password"].encode('utf-8'),password)
            if check_password :
               token = jwt.encode({'user_id':user['user_id'],'username':user['username']}, app.config['SECRET_KEY'])
               respone = jsonify({'token':token,"message":"登錄成功",'username':user['username'],'id':user['id']})
               return respone
            else:
                 return jsonify({"message":"密碼錯誤"})


@route_user.route('/userLogin', methods=['POST'])
def login2():
        json = request.json
        user_id= json['user_id']
        password = json['password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from user where user_id=%s and r_id = 2",user_id)
        user = cursor.fetchone()
        if user == None:
            return jsonify({"message":"帳號或密碼錯誤"})
        if user !=0:
            check_password = bcrypt.check_password_hash(user["password"].encode('utf-8'),password)
            if check_password :
               token = jwt.encode({'user_id':user['user_id'],'username':user['username']}, app.config['SECRET_KEY'])
               respone = jsonify({'token':token,"message":"登錄成功",'username':user['username'],'id':user['id']})
               return respone
            else:
                 return jsonify({"message":"密碼錯誤"})



@route_user.route('/update/<int:page_id>', methods=['GET','POST'])
def update(page_id):
    json = request.json
    user_id = json['user_id']
    username = json['username']
    password =json['password']
    hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
    email = json['email']
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("UPDATE user SET  user_id = %s,username = %s,password = %s ,email= %s where id = %s" ,(user_id,username,hash_password,email,page_id))
    conn.commit()
    respone = jsonify({"message":"更新成功"})
    respone.status_code = 200
    return respone
  

@route_user.route('/<int:page_id>')
def page(page_id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * from user where id=%s ",page_id)
    user = cursor.fetchone()
    respone = jsonify(user)
    respone.status_code = 200
    return respone

