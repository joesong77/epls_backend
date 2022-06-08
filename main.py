from flask import Blueprint
from app import app
from controller.user import route_user

from controller.commentclass import route_commentclass

from controller.comment import route_comment
import os

@app.route("/")
def hello_world():
    return "Hello, Flask!"

app.register_blueprint(route_user,url_prefix='/api/user') #register_blueprint方法將user.py註冊到app應用程式，

app.register_blueprint(route_commentclass,url_prefix='/api/commentclass') #register_blueprint方法將user.py註冊到app應用程式，
app.register_blueprint(route_comment,url_prefix='/api/comment') 

if __name__ == "__main__":
     port=int(os.environ.get('PORT',5000))
     app.run(debug=True, port=port)