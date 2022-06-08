
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'b164a87ae7ac54'
app.config['MYSQL_DATABASE_PASSWORD'] = 'e6ba1e5e'
app.config['MYSQL_DATABASE_DB'] = 'heroku_af5809984c98317'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-05.cleardb.net'

mysql.init_app(app)