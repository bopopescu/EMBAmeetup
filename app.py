from flask import Flask
from flask_restful import Api,Resource
from flask_restful import reqparse
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
app = Flask(__name__)
api = Api(app)
class CreateUser(Resource):
    def post(self):
        try:
            
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            cursor.callproc('sp_insertmember')

        except Error as e :
            return {'error': str(e)}
        finally:
            cursor.close()
            conn.close()




api.add_resource(CreateUser, '/CreateUser')


if __name__ == '__main__':
    app.run(debug=True)

