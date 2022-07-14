
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'bf82362ebc0f1a'
app.config['MYSQL_DATABASE_PASSWORD'] = '6020d5e6'
app.config['MYSQL_DATABASE_DB'] = 'heroku_6c408a4a7ba5f7b'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-06.cleardb.net'

mysql.init_app(app)