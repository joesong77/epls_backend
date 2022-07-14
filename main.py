from flask import Blueprint
from app import app
from controller.user import route_user
from controller.personnel import route_personnel
from controller.cookbook import route_cookbook

import os

@app.route("/")
def hello_world():
    return "Hello, Flask!"

app.register_blueprint(route_user,url_prefix='/api/user') #register_blueprint方法將user.py註冊到app應用程式，
app.register_blueprint(route_personnel,url_prefix='/api/personnel')
app.register_blueprint(route_cookbook,url_prefix='/api/cookbook')

if __name__ == "__main__":
    
     app.run(debug=True, host='0.0.0.0', port=3000)