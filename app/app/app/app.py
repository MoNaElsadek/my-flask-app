from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'rootpassword')
db_name = os.getenv('DB_NAME', 'testdb')

@app.route('/')
def hello():
    return "Hello, Ansible and Docker Compose!"

@app.route('/db')
def db_test():
    try:
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
        return f"Connected to database: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

